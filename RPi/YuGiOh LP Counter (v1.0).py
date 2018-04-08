# Yu-Gi-Oh Life Points Counter
# Ethan Crooks

import time,random

lp_p1 = 4000
lp_p2 = 4000


def ni():
    print()
    print('Not implimented')
    print()

def main():
    print()
    print('Yu-Gi-Oh Life Points Counter')
    print('                  v1.0')
    print()
    startmenu()

def startmenu():
    print('Type 1 for a new game, 2 to continue one, or')
    print('3 to exit.')
    print()
    a = input('>>> ')
    if a == '1':
        play('1')
        startmenu()
    elif a == '2':
        play('2')
        startmenu()
    elif a == '3':
        print()
        print('---')
        print()
        pass
    else:
        print()
        startmenu()

def play(state):
    global lp_p1, lp_p2
    fileexists = testfileexists()
    if fileexists == False:
        print()
        print('Error - Save file not found.')
        print('(save.txt)')
        print('Cannot continue game from save.')
        print('Switching to new file mode.')
        state = '1'
    else:
        print()
        print('File Found (save.txt)')
    if state == '1':
        lp_p1, lp_p2 = setlp()
    elif state == '2':
        lp_p1, lp_p2 = getlpfromfile()
    print()
    print('Starting...')
    print()
    playing = True
    playerwon = '1'
    while playing == True:
        print('P1 - ' + str(lp_p1))
        print('P2 - ' + str(lp_p2))
        null = input('Press enter to edit LP ')
        print()
        print('Whose to edit?')
        player = chooseplayer()
        print()
        print('Type 1 to add or 2 to deduct.')
        operator = addorminus()
        print()
        print('How many to add/deduct?')
        editlp = howmany()
        print()
        if operator == '1':
            print('Adding ' + str(editlp) + ' LP to Player ' + player + '.')
            if player == '1':
                lp_p1 = lp_p1 + editlp
            elif player == '2':
                lp_p2 = lp_p2 + editlp
        elif operator == '2':
            print('Deducting ' + str(editlp) + ' LP from Player ' + player + '.')
            if player == '1':
                lp_p1 = lp_p1 - editlp
            elif player == '2':
                lp_p2 = lp_p2 - editlp
        print()
        print('Done.')
        if fileexists == True:
            savefile(lp_p1,lp_p2)
            null = input('Press enter to save. ')
            print('Saved.')
        else:
            print()
            print('Cannot save - Error finding save file')
            print('(save.txt)')
        print()
        lp_p1 = int(lp_p1)
        lp_p2 = int(lp_p2)
        if lp_p1 <= 0:
            playerwon = '2'
            playing = False
        elif lp_p2 <= 0:
            playerwon = '1'
            playing = False
    print('GAME END!')
    print()
    print('Player ' + playerwon + ' won the game!')
    print()
    print('P1 - ' + str(lp_p1))
    print('P2 - ' + str(lp_p2))
    savefile(4000,4000)
    time.sleep(3)
    print()

def howmany():
    a = input('>>> ')
    try:
        a = int(a)
    except ValueError:
        print()
        print('Not a number!')
        howmany()
    a = int(a)
    a = abs(a)
    return a

def addorminus():
    a = input('>>> ')
    if a == '1':
        return '1'
    elif a == '2':
        return '2'
    else:
        print()
        print('Type 1 or 2.')
        addorminus()
    

def chooseplayer():
    a = input('>>> ')
    if a == '1':
        return '1'
    elif a == '2':
        return '2'
    else:
        print('Type a 1 or a 2.')
        print()
        chooseplayer()

def setlp():
    a = 4000
    b = 4000
    print()
    print('Type 1 for 4000 LP, type 2 for 8000 LP, or type')
    print('3 for a custom number of LP.')
    print()
    a = input('>>> ')
    print()
    if a == '1':
        a = 4000
        b = 4000
        print('Both set to 4000 LP')
    elif a == '2':
        a = 8000
        b = 8000
        print('Both set to 8000 LP')
    elif a == '3':
        print('How many LP do you want?')
        c = input('>>> ')
        try:
            c = int(c)
        except ValueError:
            print()
            print('Not a number!')
            setlp()
        print()
        a = c
        b = c
        print('LP set to ' + str(c) + '.')
    print()
    return a,b

def getlpfromfile():
    f = open('save.txt','r')
    file = f.read().splitlines()
    a = file[0]
    b = file[1]
    a = int(a)
    a = int(b)
    return a,b

def savefile(a,b):
    a = str(a)
    b = str(b)
    f = open('save.txt','w')
    c = a + '\n' + b
    f.write(c)

def testfileexists():
    try:
        f = open('save.txt')
        null = f.read()
        result = True
    except IOError:
        result = False
    return result
    

main()
