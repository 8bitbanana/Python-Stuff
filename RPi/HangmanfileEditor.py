# Hangman File Editor
# By Ethan Crooks
# for use with the Hangman game

global workfile, version, indev

workfile = 0

version = '1.0'
indev = True

if indev == True:
    version = version + ' (dev)'

def ni():
    print('Not implemented.')

def main():
    print()
    print('Welcome to the Hangman File editor!')
    print('                 ' + version)
    print()
    startinput()

def startinput():
    print('Type 1 for a new file, 2 to continue one or')
    print('3 to exit.')
    a = input('>>> ')
    if a == '1':
        ni()
    elif a == '2':
        ni()
    elif a == '3':
        pass
    else:
        print('Invalid imput. Type 1, 2 or 3.')
        startinput()

def createfile():
    print('Type in what you want the file to be called.')
    a = input('>>> ')
    print()
    print('Set file name as ' + a + '?')
    b = input('(y/n) >>> ')
    if b.lower == 'n':
        print()
        createfile()
    elif b.lower != 'y':
        print('Taking ' + b + ' as a no.')
        print()
        createfile()
    workfile = a
    print()
    print('Creating file...')
    f = open('wordfiles/'+workfile,'w')
    f.write('')
    f.close()
    print('Checking file...')
    f = open('wordfiles/'+workfile,'r')
    try:
        f.read()
    except IOError:
        print('IOError - Exiting...')
        pass
    print('File created!')
    




main()
