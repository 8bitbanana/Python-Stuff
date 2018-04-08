import time
import requests
import html
import re
import webbrowser
from urllib.parse import urlparse
from random import shuffle
from bs4 import BeautifulSoup as BSoup
from pprint import pprint

backup_limit = 5
filetype_blacklist = ['.png','.gif','.jpg','.jpeg','.pdf','/rss','.mp3','.mp4']
only_new_links = True

currentpage = 'https://www.xkcd.com'
pagehistory = [[currentpage]]
backup_history = []

def backup(currentpage, pagehistory,reason=''):
    print(reason,'Backing up...')
    backup_amount = 2
    while True:
        previndex = len(pagehistory)-backup_amount
        if pagehistory[previndex][1]<5:
            pagehistory[previndex][1]+=1
            currentpage = pagehistory[previndex][0]
            break
        else:
            print('Backup limit reached, backing up further...')
            backup_amount += 1
    return currentpage, pagehistory

start_time = int(time.time())

while True:
    print('Getting '+currentpage+'...')
    error = False
    for filetest in filetype_blacklist:
        if currentpage.find(filetest)!=-1:
            currentpage, pagehistory = backup(currentpage, pagehistory, 'Is a '+filetest+'.')
            error = True
            break
    if error:
        continue
    try:
        page = requests.get(currentpage)
    except KeyboardInterrupt:
        print('\n\nCancelled')
        break
    except:
        currentpage, pagehistory = backup(currentpage, pagehistory, 'Crashed.')
        continue
    raw = page.text
    scraped_links = []
    soup = BSoup(raw,'lxml')
    for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
        scraped_links.append(link.get('href'))
    print(str(len(scraped_links))+' found')
    if len(scraped_links)==0:
        currentpage, pagehistory = backup(currentpage, pagehistory)
    else:
        shuffle(scraped_links)
        currentpage = scraped_links[0]
        if currentpage == pagehistory[len(pagehistory)-1]:
            currentpage, pagehistory = backup(currentpage, pagehistory)
        if only_new_links:
            found = False
            for selected_history in pagehistory:
                while selected_history[0]==currentpage:
                    currentpage, pagehistory = backup(currentpage, pagehistory,'Seen before. ')
                    found = True
                    break
                if found:
                    break
        pagehistory.append([currentpage,0])

end_time = int(time.time())
total_time = end_time - start_time

# TODO -v

m, s = divmod(total_time, 60)
h, m = divmod(m, 60)
formatted_time = '%dh %02dm %02ds' % (h, m, s)

unique_links = []
for x in pagehistory:
    add = True
    for y in unique_links:
        if x[0]==y:
            add = False
            break
    if add:
        unique_links.append(x[0])

all_domains = []
unique_domains = []
for x in pagehistory:
    p = urlparse(x[0])
    all_domains.append(p.netloc)

for x in all_domains:
    add = True
    for y in unique_domains:
        if x==y:
            add = False
            break
    if add:
        unique_domains.append(x)

input()

print('=== FINAL STATISTICS ===')
print('Total Links - ' + str(len(pagehistory)))
print('Unique Links - ' + str(len(unique_links)))
print('Unique Domains - ' + str(len(unique_domains)))
print('Time Taken - ' + formatted_time)

input()

for x in enumerate(pagehistory):
    print('['+str(x[0])+'] - '+x[1][0])

a = input('Open which file? ')
if a != '':
    try:
        a=int(a)
        webbrowser.open(pagehistory[a][0])
    except:
        pass
