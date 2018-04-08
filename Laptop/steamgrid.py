import requests
import ast
from pprint import pprint
from tkinter import *

username = input('Enter Steam ID - ')
if username=='':
    username='[redacted]'

url = "http://steamcommunity.com/id/{}/games?tab=all".format(username)

page = requests.get(url) # Get the raw html
raw = page.text
games='blank'
for line in raw.splitlines():
    if line.find('var rgGames')!=-1: # Get the line with all the games on it
        games=line

games=games.strip() # Strip the whitespace
games=games.replace('var rgGames = [{', '') # Get rid of all the js stuff
games=games.replace('];','')
games=games.split('},{') # Get a python list of all the raw game data

parsedGames = []
for raw in games:
    cutIndex = raw.index(',"friendly') # Cut everything from friendlyURL onwards
    rawCut = raw[0:cutIndex]
    try:
        hoursindex = raw.index('"hours_forever"') # Get the hours_forever and last_played values
        hoursCut = raw[hoursindex-1:]
    except ValueError:
        hoursCut = ',"hours_forever":"0","last_played":None'
    rawDict = '{{{}{}}}'.format(rawCut,hoursCut) # Add the curly brackets
    parsedDict = ast.literal_eval(rawDict) # Parse as a python dict!
    parsedGames.append(parsedDict)
    

class MainApp:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        index = 0
        for x in parsedGames:
            Label(frame, text=x['appid']).grid(row=index,column=0)
            Label(frame, text=x['name']).grid(row=index,column=1)
            Label(frame, text=x['hours_forever']).grid(row=index,column=2)
            index+=1

root = Tk()
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT,fill=Y)
app = MainApp(root)
root.mainloop()
