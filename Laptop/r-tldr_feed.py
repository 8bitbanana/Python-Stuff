import webbrowser, os, textwrap, msvcrt

try:
    import praw
except ImportError:
    print("Error - the praw module, used for getting stuff from reddit, isn't")
    print("installed. Please run the following command in cmd, bash etc to install it:")
    print("pip install praw -U")
    print()
    input()
    exit()

client_id = '[redacted]'
client_secret = '[redacted]'
user_agent = '[redacted]'

reddit = praw.Reddit(client_id=client_id,client_secret=client_secret,user_agent=user_agent)
subreddit = reddit.subreddit("tldr")


def getInput(valid_raw,validate=True,exitChar="q"):
    valid=[]
    for x in valid_raw:
        valid.append(str(x))
    while True:
        letter = msvcrt.getwch()
        if letter==exitChar:
            exit()
        for check in valid:
            if check==letter:
                return letter
        if not validate:
            return ""

def cls():
    if os.name == 'nt':
        os.system('cls')
    elif os.name == 'posix':
        os.system('clear')
    else:
        print('\n' * 100)

def getSubmissions(post):
    submissions=[]
    sections = {}
    for submission in subreddit.new(limit=20):
        submissions.append(submission)
    submission = submissions[post]
    selftext_list = submission.selftext.splitlines()
    for index in range(0,len(selftext_list)):
        try:
            if selftext_list[index][0]=="#":
                if selftext_list[index].find("Something New")!=-1:
                    break
                section_title=selftext_list[index]
                section_length=0
                section=[]
                for line in selftext_list[index:]:
                    if line=="*****":
                        break
                    else:
                        section.append(line)
                        section_length+=1
                sections[section_title]=section
                index+=section_length
        except IndexError:
            pass
    return sections, submissions[0].title


def printTitle(title):
    start_index = title.index("]") + 2
    title_list = title[start_index:].split(";")
    print(title[:start_index])
    for item in title_list:
        print(" --" + item.strip())
    print()


def main():
    os.system("MODE CON LINES=60 COLS=120")
    print("/R/TLDR PYTHON VIEWER")
    print()
    print("q at any time to quit")
    print("SPACE to cycle between sections")
    print()
    print("Getting Posts...")
    sections, title = getSubmissions(0)
    group = 0
    while True:
        cls()
        printTitle(title)
        index=0
        printIndex=0
        for key in sections.keys():
            if group <= index < group+10:
                print("   [{}] - {}".format(printIndex,key))
                printIndex+=1
            else:
                print("[x] - {}".format(key))
            index+=1
        print()
        valid = list(range(len(sections.keys())))
        valid.append(" ")
        user_input = getInput(valid)
        if user_input == " ":
            group+=10
            if group>len(sections.keys()):
                group=0
            continue
        try:
            user_key = list(sections.keys())[int(user_input)+group]
        except (IndexError, ValueError, KeyError):
            continue
        cls()
        printTitle(title)
        section = sections[user_key]
        index=0
        links=[]
        for x in section:
            if x.find("[Comments]")!=-1 and x.find("[Link]")!=-1:
                comment_index = x.find("[Comments]")
                link_index = x.find("[Link]")
                dividor_index = x.find("||")
                link=x[comment_index:dividor_index]
                links.append(link)
                if len(link)>=100:
                    link=link[:97]+"...)"
                print("[{}]{}".format(index, link))
                link = x[link_index:]
                links.append(link)
                if len(link)>=100:
                    link = link[:97] + "...)"
                print("[{}]{}".format(index+1, link))
                index+=2
            elif x.find("[Comments]")!=-1 and x.find("[Link]")==-1:
                comment_index = x.find("[Comments]")
                link = x[comment_index:]
                links.append(link)
                if len(link) >= 100:
                    link = link[:97] + "...)"
                print("[{}]{}".format(index, link))
                index+=1
            elif x.find("[Comments]")==-1 and x.find("[Link]")!=-1:
                link_index = x.find("[Link]")
                link = x[link_index:]
                links.append(link)
                if len(link) >= 100:
                    link = link[:97] + "...)"
                print("[{}]{}".format(index, link))
                index+=1
            else:
                print(textwrap.fill(x,110))
        print()
        action = getInput(list(range(len(links))),validate=False)
        if action=="":
            continue
        try:
            link = links[int(action)]
            link=link.replace("[Comments](", "")
            link=link.replace("[Link](", "")
            link=link[:-1]
            webbrowser.open(link,new=2)
        except IndexError:
            continue

if __name__=="__main__":
    main()
