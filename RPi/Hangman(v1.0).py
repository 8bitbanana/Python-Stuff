# Hangman v0.1
# Initial code by Simon Monk, edited by Ethan Crooks

import random
file = 'missingno'
dirfile = 'savefiles/wordfile.txt'

def getmainfile():
    global file
    global dirfile
    try:
        f = open(dirfile)
        file = f.read()
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
            print('Please create a file named wordfile.txt in ~/DO NOT DELETE')
        print('ALL SAVE DATA HAS BEEN LOST')
        print('Please type in the directory of the words file:')
        a = input('>>> ')
        file = a
        try:
            f = open(dirfile,'w')
            f.write(a)
            f.close()
        except IOError:
            print()
        print("Directory set to '" + file + "'")
        print()

def writemainfile(s):
    global file
    try:
        f = open(dirfile,'w')
        f.write(s)
        f.close()
        file = s
    except IOError:
        file = s

def getfile():
    global file
    global words
    try:
        f = open(file)
        words = f.read().splitlines()
        f.close()
        print("Using file '" + file + "' - Successfully found")
        getdescription()
    except IOError:
        words = ['chicken', 'dog', 'cat', 'mouse', 'frog', 'cow', 'pig', 'rabbit','[desc]','ANIMALS','Different animals, the default word list.']
        print("Could not find file '" + file + "', using default setup instead.")
        print('Change file directory in settings.')

lives_remaining = 14
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
    lives_remaining = 14
    getfile()
    word = pick_a_word()
    while True:
        guess = get_guess(word)
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
        print('Exiting...')
        print()
    else:
        print(a + " isn't a valid input")
        print()
        startinput()

def settings():
    global file
    print()
    print('Type 1 for difficulty, 2 for words file directory or 3 to exit')
    b = input('>>> ')
    if b == '1':
        print('Difficulty not implimented yet')
        settings()
    elif b == '2':
        print('Current directory is - ' + file)
        print('Type in new directory')
        file = input('>>> ')
        writemainfile(file)
        print('Set ' + file + ' as directory')
        settings()
    elif b == '3':
        print()
        print('Type 1 to start, 2 for settings, 3 for credits or 4 to exit')
        startinput()
    else:
        print("'" + b + "' is not a vaild input")
        settings()

def main():
    print()
    print('###############################')
    print('#| |  _   _   _   ___   _   _ #')
    print('#|_| | | | | |   | | | | | | |#')
    print('#| | |_| | | | | |   | |_| | |#')
    print('#| | | | | | |_| |   | | | | |#')
    print('###############################')
    print('                         v1.0')
    print('Welcome to Hangman!')
    printmenu()
    startinput()

def printmenu():
    print('Type 1 to start, 2 for settings, 3 for credits or 4 to exit')
    
getmainfile()
main()
