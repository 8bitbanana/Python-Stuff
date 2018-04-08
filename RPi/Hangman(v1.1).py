# Hangman v0.1
# Initial code by Simon Monk, edited by Ethan Crooks

import random, time
afile = 'missingno'
dirfile = 'savefiles/wordfile.txt'
dirhelpfile = 'savefiles/help.txt'
helplist = ''
dirdifffile = 'savefiles/diffi.txt'
difficulty = '1'

def prosessfile(a):
    if a.endswith('.txt') == False:
        a = a + '.txt'
    if a.find('wordfiles/') == 0:
        a.replace('wordfiles/','')
    writemainfile(a)
    return a

def getmainfile():
    global afile
    global dirfile
    try:
        f = open(dirfile)
        afile = f.read()
        f.close()
    except IOError:
        print('Cannot find system save file')
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

guessed_letters = ''

def getdescription():
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
        print('Could not find title or description')
        

def pick_a_word():
    global words
    word_position = random.randint(0, len(words) - 1)
    a = words[word_position]
    return a.lower()

def play():
    global guessed_letters
    global lives_remaining
    guessed_letters = ''
    if difficulty == '1':
        lives_remaining = 14
    elif difficulty == '2':
        lives_remaining = 10
    elif difficulty == '3':
        lives_remaining = 8
    else:
        print('Unable to establish difficulty')
        lives_remaining = 14
    getfile()
    word = pick_a_word()
    while True:
        guess = get_guess(word)
        if guess.upper() == '[DEBUG STOP]':
            printmenu()
            startinput
            break
        else:
            result = process_guess(guess, word)
        if result == True:
            print()
            print(word)
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
            print('The word was - ' + word)
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
            return 'xxxmissingnoxxx'
        else:
            return whole_word_guess(guess, word)
    else:
        if legitinputs.find(guess) > -1:
            if guessed_letters.find(guess) > -1:
                print()
                print("You have already guessed the letter " + guess + '!')
                print('Guess again.')
                return 'xxxmissingnoxxx'
        else:
            print()
            print("You can't guess a " + guess + ", it isn't a letter!")
            return 'xxxmissingnoxxx'
        return single_letter_guess(guess, word)

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
    a = input('>>> ')
    if a == '1':
        play()
    elif a == '2':
        settings()
    elif a == '3':
        print()
        print('By Ethan Crooks')
        print('Initial code by Simon Monk')
        print()
        startinput()
    elif a == '4':
        showhelp()
        printmenu()
        startinput()
    elif a == '5':
        print('Exiting...')
        print()
    else:
        print(a + " isn't a valid input")
        print()
        startinput()

def settings():
    global afile
    print()
    print('Type 1 for difficulty, 2 for words file directory or 3 to exit')
    b = input('>>> ')
    if b == '1':
        getdifficulty()
        settings()
    elif b == '2':
        print('Current directory is - ' + afile)
        print('Type in new directory')
        afile = input('>>> ')
        writemainfile(afile)
        print('Set ' + afile + ' as directory')
        settings()
    elif b == '3':
        print()
        print('Type 1 to start, 2 for settings, 3 for credits or 4 to exit')
        startinput()
    else:
        print("'" + b + "' is not a vaild input")
        settings()

def main():
    getfiles()
    print()
    print('###############################')
    print('#| |  _   _   _   ___   _   _ #')
    print('#|_| | | | | |   | | | | | | |#')
    print('#| | |_| | | | | |   | |_| | |#')
    print('#| | | | | | |_| |   | | | | |#')
    print('###############################')
    print('                         v1.1')
    print('Welcome to Hangman!')
    printmenu()
    startinput()

def printmenu():
    print('Type 1 to start, 2 for settings, 3 for credits, 4 for help or 5 to exit')

def showhelp():
    global helplist
    print()
    for x in range(0,len(helplist)):
        print(helplist[x])
    print()
    time.sleep(3)

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
        print('(savefiles/diffi.txt)')
        print()

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

main()
