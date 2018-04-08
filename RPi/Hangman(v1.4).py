# Hangman v1.3
# By Ethan Crooks. Initial code by Simon Monk

import random, time
from glob import glob

# Variable init and File directories
afile = 'missingno'
dirfile = 'savefiles/wordfile.txt'
dirhelpfile = 'savefiles/help.txt'
helplist = ''
dirdifffile = 'savefiles/diffi.txt'
dirpfile = 'savefiles/pselect.txt'
difficulty = '1'
playerchoice = '1'
pguess = '1'
pword = '2'
p_rotate = False
firstgo = True

# File Info
version = '1.4'
indev = False
toadd = ['None.']

if indev == True:
    devstartup()

def devstartup():
    print('This version of Hangman has been marked as in development.')
    print('Expect bugs.')
    prtin()
    print('[TO ADD]')
    for x in range(0,len(toadd)):
        print(toadd[x])

def prosessfile(a):
    return a

def getmainfile():
    global afile
    global dirfile
    try:
        f = open(dirfile)
        afile = f.read()
        f.close()
    except IOError:
        print('Cannot find system save file.')
        print('Creating new system save file...')
        f = open(dirfile,'w')
        f.write('MISSINGNO')
        f.close()
        print('Checking to see if file has been created...')
        readfile = 'xxx'
        f = open(dirfile,'r')
        readfile = f.read()
        f.close()
        if readfile == 'MISSINGNO':
            print('Successful')
        else:
            print('Save file read unsuccessful')
            print('Please create a file named wordfile.txt in ~/savefiles')
        print('ALL SAVE DATA HAS BEEN LOST')
        print('Please type in the directory of the words file:')
        a = input('>>> ')
        afile = a
        try:
            f = open(dirfile,'w')
            f.write(a)
            f.close()
        except IOError:
            print()
        print("Directory set to '" + afile + "'")
        print()

def writemainfile(s):
    global afile
    try:
        f = open(dirfile,'w')
        f.write(s)
        f.close()
        afile = s
    except IOError:
        afile = s

def getfile():
    global afile
    global words
    prosessfile(afile)
    try:
        f = open(afile)
        words = f.read().splitlines()
        f.close()
        print("Using file '" + afile + "' - Successfully found")
        getdescription()
    except IOError:
        words = ['chicken', 'dog', 'cat', 'mouse', 'frog', 'cow', 'pig', 'rabbit','[desc]','ANIMALS','Different animals, the default word list.']
        print("Could not find file '" + afile + "', using default setup instead.")
        print('Change file directory in settings.')
        getdescription(True)

guessed_letters = ''

def getdescription(default=False):
    if default == False:
        try:
            q = words.index('[desc]')
            title = words[q+1]
            desc = words[q+2]
            words.remove('[desc]')
            words.remove(desc)
            words.remove(title)
            print()
            print(title)
            print(desc)
        except:
            print()
            print('UNKNOWN FILE')
            print('Could not find title or description.')
    else:
        print()
        print('ANIMALS')
        print('A list of serveral farm animals.')
        
def clearscreen():
    for x in range(0,50):
        print()

def pick_a_word():
    global words
    word_position = random.randint(0, len(words) - 1)
    a = words[word_position]
    return a.lower()

def pick_a_word2p():
    print('Player ' + pword + ', please type a word')
    print('Player ' + pguess + ', please go away.')
    print()
    a = input('>>> ')
    a = processwordinput(a)
    clearscreen()
    print('Bring player ' + pguess + ' back.')
    return a

def processwordinput(word):
    legitinputs = ('qwertyuiopasdfghjklzxcvbnm')
    print('Processing word...')
    wlist = list(word)
    toberemoved = ''
    for x in range(0,len(wlist)):
        a = legitinputs.find(wlist[x])
        if a == -1:
            toberemoved = toberemoved + wlist[x]
    list(toberemoved)
    print('Removing invalid inputs...')
    for x in range(0,len(toberemoved)):
        wlist.remove(toberemoved[x])
    print('Recontructing word...')
    wordnew = ''
    for x in range(0,len(wlist)):
        wordnew = wordnew + wlist[x]
    print('Word reconstructed as "' + wordnew + '"')
    time.sleep(2)
    return wordnew.lower()
        

def getplayers():
    global firstgo
    global playerchoice
    global pguess
    global pword
    if playerchoice != '3':
        if playerchoice == '1':
            #print('CHOOSE')
            print('Which player should guess?')
            a = input('(1/2) >>> ')
            if a == '1':
                pguess = '1'
                pword = '2'
            elif a == '2':
                pguess = '2'
                pword = '1'
            else:
                print('Not a valid input.')
                getplayersdev()
        if playerchoice == '2':
            #print('RANDOM')
            a = random.randint(1,2)
            if a == '1':
                pguess = '1'
                pword = '2'
                print('Player 1 is guessing.')
            else:
                pguess = '2'
                pword = '1'
                print('Player 2 is guessing.')
    else:
        #print('SWAP')
        if firstgo == True:
            print('Which player should guess first?')
            a = input('(1/2) >>> ')
            if a == '1':
                pguess = '1'
                pword = '2'
            elif a == '2':
                pguess = '2'
                pword = '1'
            else:
                print('Not a valid input.')
                getplayersdev()
        else:
            if pguess == '1' and pword == '2':
                pguess = '2'
                pword = '1'
            else:
                pguess = '1'
                pword = '2'


def a2play():
    global guessed_letters
    global lives_remaining
    global playerchoice
    global p_rotate
    if playerchoice == '3':
        p_rotate = True
    else:
        p_rotate = False
    guessed_letters = ''
    if difficulty == '1':
        lives_remaining = 14
    elif difficulty == '2':
        lives_remaining = 10
    elif difficulty == '3':
        lives_remaining = 8
    else:
        print('Unable to establish difficulty (setting to easy)')
        lives_remaining = 14
    print()
    getplayerfile()
    print('Player select settings = ' + playerchoice)
    print()
    getplayers()
    print()
    word = pick_a_word2p()
    print()
    while True:
        guess = get_guess(word)
        result = process_guess(guess, word)
        if result == True:
            print()
            print(word)
            print('Player ' + pguess + ' wins!')
            print()
            print('  _     _')
            print(' |O|   |O|')
            print(' |_|   |_|')
            print('     ()')
            print(' ,       ,')
            print('  `=====`')
            print()
            firstgo = False
            goagain()
            break
        if lives_remaining <= 0:
            print()
            print('Player ' + pguess + ' was hung!')
            print('  _     _')
            print(' |+|   |+|')
            print(' |_|   |_|')
            print('     ()')
            print(' _________')
            print('       |_|')
            print()
            print('The word was - ' + word)
            print('Player ' + pword + ' wins!')
            print()
            firstgo = False
            goagain()
            break

def goagain():
    global firstgo
    print('Would you like to go again?')
    a = input('(y/n) >>> ')
    if a.lower() == 'y':
        firstgo = False
        a2play()
    elif a.lower() == 'n':
        print()
        firstgo = True
        printmenu()
        startinput()
    else:
        print('Not a valid input. Type a "y" or a "n".')
        goagain()
                    

def play():
    global guessed_letters
    global lives_remaining
    guessed_letters = ''
    if difficulty == '1':
        lives_remaining = 14
    elif difficulty == '2':
        lives_remaining = 11
    elif difficulty == '3':
        lives_remaining = 7
    else:
        print('Unable to establish difficulty (setting to easy)')
        lives_remaining = 14
    getfile()
    word = pick_a_word()
    while True:
        guess = get_guess(word)
        result, display = process_guess(guess, word)
        if display == True:
            displayhangman(lives_remaining)
        if result == True:
            print()
            print(word.upper())
            print('You win!')
            print()
            print('  _     _')
            print(' |O|   |O|')
            print(' |_|   |_|')
            print('     ()')
            print(' ,       ,')
            print('  `=====`')
            print()
            printmenu()
            startinput()
            break
        if lives_remaining <= 0:
            print()
            print('You are hung!')
            print('  _     _')
            print(' |+|   |+|')
            print(' |_|   |_|')
            print('     ()')
            print(' _________')
            print('       |_|')
            print()
            print('The word was - ' + word.upper())
            print()
            printmenu()
            startinput()
            break

def get_guess(word):
    print_word_with_blanks(word)
    print('Lives remaining - ' + str(lives_remaining))
    guess = input(' Guess a letter or whole word - ')
    return guess.lower()

def process_guess(guess, word):
    legitinputs = 'qwertyuiopasdfghjklzxcvbnm'
    guess = guess.lower()
    if len(guess) > 1:
        if len(guess) != len(word):
            print()
            print("'" + guess + "' can't be a guess, it is not the right length!")
            print('Guess again.')
            return 'xxxmissingnoxxx', False
        else:
            return whole_word_guess(guess, word), True
    else:
        if legitinputs.find(guess) > -1:
            if guessed_letters.find(guess) > -1:
                print()
                print("You have already guessed the letter " + guess + '!')
                print('Guess again.')
                return 'xxxmissingnoxxx', False
        else:
            print()
            print("You can't guess a " + guess + ", it isn't a letter!")
            return 'xxxmissingnoxxx', False
        return single_letter_guess(guess, word), True

def print_word_with_blanks(word):
    display_word = ''
    for letter in word:
        if guessed_letters.find(letter) > -1:
            # letter found
            display_word = display_word + letter
        else:
            # letter not found :(
            display_word = display_word + '-'
    print()
    print(display_word)

def single_letter_guess(guess, word):
    global guessed_letters
    global lives_remaining
    if word.find(guess) == -1:
        # letter guess was incorrect
        lives_remaining = lives_remaining - 1
    guessed_letters = guessed_letters + guess
    if all_letters_guessed(word):
        return True

def all_letters_guessed(word):
    for letter in word:
        if guessed_letters.find(letter) == -1:
            return False
    return True

def whole_word_guess(guess, word):
    global lives_remaining
    if guess.lower() == word.lower():
        return True
    else:
        lives_remaining = lives_remaining - 10
        return False
    
def startinput():
    global version
    firstgo == True
    a = input('>>> ')
    if a == '1':
        playerselect()
    elif a == '2':
        settings()
    elif a == '3':
        print()
        print(' HANGMAN v' + version)
        print('By Ethan Crooks')
        print('Base code by Simon Monk')
        print()
        printmenu()
        startinput()
    elif a == '4':
        showhelp()
        printmenu()
        startinput()
    elif a == '5':
        print('Exiting...')
        print()
    elif a == 'easteregg':
        secret()
    else:
        print(a + " isn't a valid input")
        print()
        startinput()

def playerselect():
    print('One or two players?')
    a = input('(1/2) >>> ')
    if a == '1':
        print('One player.')
        play()
    elif a == '2':
        print('Two players.')
        a2play()
    else:
        print('Not a valid input - type "1" or "2"')
        playerselect()

def secret():
    print()
    print('===============')
    print('  EASTER EGG!')
    print('===============')
    print()
    printmenu()
    startinput()

def settings():
    global afile
    print()
    print('Type 1 for difficulty, 2 for words file directory, 3 for player select')
    print('or 4 for main menu.')
    b = input('>>> ')
    if b == '1':
        getdifficulty()
        settings()
    elif b == '2':
        d = fileselect()
        try:
            writemainfile(d)
            print('File written succesfully.')
        except:
            print('ERROR - File not written.')
        settings()
    elif b == '3':
        print('Change the player select settings.')
        print('Do you want random player select or a choice at the start of the round?')
        print('Type 1 for choice, 2 for random or 3 to alternate players?')
        c = input('>>> ')
        if c == '1' or c == '2' or c == '3':
            setplayerfile(c)
        else:
            print('Not a valid input. Type a 1 or 2.')
        settings()
    elif b == '4':
        print()
        printmenu()
        startinput()
    else:
        print("'" + b + "' is not a vaild input")
        settings()

def main():
    global version
    if indev == True:
        version = version + ' (dev)'
    getfiles()
    print()
    print('###############################')
    print('#| |  _   _   _   ___   _   _ #')
    print('#|_| | | | | |   | | | | | | |#')
    print('#| | |_| | | | | |   | |_| | |#')
    print('#| | | | | | |_| |   | | | | |#')
    print('###############################')
    print('                         ' + version)
    print('Welcome to Hangman!')
    printmenu()
    startinput()


def fileselect():
    print()
    files = glob('wordfiles/*.txt')
    for x in range(0,len(files)):
        show = files[x][10:]
        print('[' + str(x) + '] - ' + show)
    print()
    print('Type in number to select a file.')
    a = input('>>> ')
    try:
        a = int(a)
    except:
        print('Not a number.')
        fileselect()
    if a > -1 and a < len(files):
        print()
        show = files[a]
        print('File ' + show + ' selected.')
        return files[a]
    else:
        print('Out of range. Type a number between 1 and ' + str(len(files)) + '.')
        fileselect()

def printmenu():
    print('Type 1 to start, 2 for settings, 3 for credits, 4 for help or 5 to exit')

def showhelp():
    global helplist
    print()
    for x in range(0,len(helplist)):
        if helplist[x] == '[*]':
            print('=============')
            a = input('Press enter to continue, or type Q to quit. ')
            print('=============')
            if a.lower() == 'q':
                break
        else:
            print(helplist[x])
    print()
    time.sleep(1)

def gethelpfile():
    global dirhelpfile
    global helplist
    try:
        f = open(dirhelpfile, 'r')
        helplist = f.read().splitlines()
        f.close()
    except IOError:
        print('Could not find help file')
        print('(savefiles/help.txt)')
        print()

def getdifficultyfile():
    global dirdifffile
    global difficulty
    try:
        f = open(dirdifffile, 'r')
        difficulty = f.read()
        f.close()
    except IOError:
        print('Could not find difficulty file')
        print(dirdifffile)
        print()

def getplayerfile():
    global dirpfile
    global playerchoice
    try:
        f = open(dirpfile, 'r')
        playerchoice = f.read()
        f.close()
    except IOError:
        print('Could not find player choice file')
        print(dirpfile)
        print() 

def setplayerfile(p):
    global dirpfile
    global playerchoice
    try:
        f = open(dirpfile, 'w')
        f.write(p)
        f.close()
        print('Player select set as ' + p + '.')
    except IOError:
        print('Could not file player select file')
        print('(savefiles/pselect.txt)')
        print()
    playerchoice = p

def setdifficulty(d):
    global dirdifffile
    global difficulty
    try:
        f = open(dirdifffile, 'w')
        f.write(d)
        f.close()
        print('Set ' + d + ' as new difficulty')
    except IOError:
        print('Could not file difficulty file')
        print('(savefiles/diffi.txt)')
        print()
    difficulty = d

def getdifficulty():
    print('Current difficulty is '+ difficulty)
    print('Type in new difficulty (1-3)')
    tempdif = input('>>> ')
    if tempdif == '1' or tempdif == '2' or tempdif == '3':
        setdifficulty(tempdif)
    else:
        print(tempdif + ' is not a vaild input')
        getdifficulty()

def getfiles():
    getmainfile()
    gethelpfile()
    getdifficultyfile()

def displayhangman(lives):
    if lives == 11:
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print('================================')
        print()
    elif lives == 10:
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print('      -------')
        print('================================')
        print()
    elif lives == 9:
        print()
        print('         |')
        print('         |')
        print('         |')
        print('         |')
        print('         |')
        print('         |')
        print('         |')
        print('      -------')
        print('================================')
        print()
    elif lives == 8:
        print('         -------------')
        print('         |')
        print('         |')
        print('         |')
        print('         |')
        print('         |')
        print('         |')
        print('         |')
        print('      -------')
        print('================================')
        print()
    elif lives == 7:
        print('         -------------')
        print('         | /')
        print('         |/')
        print('         |')
        print('         |')
        print('         |')
        print('         |')
        print('         |')
        print('      -------')
        print('================================')
        print()
    elif lives == 6:
        print('         -------------')
        print('         | /         |')
        print('         |/')
        print('         |')
        print('         |')
        print('         |')
        print('         |')
        print('         |')
        print('      -------')
        print('================================')
        print()
    elif lives == 5:
        print('         -------------')
        print('         | /         |')
        print('         |/          O')
        print('         |')
        print('         |')
        print('         |')
        print('         |')
        print('         |')
        print('      -------')
        print('================================')
        print()
    elif lives == 4:
        print('         -------------')
        print('         | /         |')
        print('         |/          O')
        print('         |           |')
        print('         |')
        print('         |')
        print('         |')
        print('         |')
        print('      -------')
        print('================================')
        print()
    elif lives == 3:
        print('         -------------')
        print('         | /         |')
        print('         |/          O')
        print('         |           |-')
        print('         |')
        print('         |')
        print('         |')
        print('         |')
        print('      -------')
        print('================================')
        print()
    elif lives == 2:
        print('         -------------')
        print('         | /         |')
        print('         |/          O')
        print('         |          -|-')
        print('         |')
        print('         |')
        print('         |')
        print('         |')
        print('      -------')
        print('================================')
        print()
    elif lives == 1:
        print('         -------------')
        print('         | /         |')
        print('         |/          O')
        print('         |          -|-')
        print('         |          / ')
        print('         |')
        print('         |')
        print('         |')
        print('      -------')
        print('================================')
        print()
    elif lives == 0:
        print('         -------------')
        print('         | /         |')
        print('         |/          O')
        print('         |          -|-')
        print('         |          / \ ')
        print('         |')
        print('         |')
        print('         |')
        print('      -------')
        print('================================')
        print()
    else:
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print('================================')
        print()     

main()
