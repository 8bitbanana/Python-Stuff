# Calculator v0.2
# By Ethan Crooks
import math

def getnumbs():
    global numb1
    global numb2
    global function
    numb1 = input(' Type first number  | ')
    numb2 = input(' Type second number | ')
    function = input(' Type a to add, s to subtract, m to multiply or d to divide or m for more | ')
    if function == 'm':
        function = input(' Type 2 for squaring or 3 for cubing. (will use first number) | ')
    numb1 = int(numb1)
    numb2 = int(numb2)

def gettotal():
    global total
    if function == 'a':
        total = numb1 + numb2
    elif function == 's':
        total = numb1 - numb2
    elif function == 'm':
        total = numb1 * numb2
    elif function == 'd':
        if numb2 == 0:
            total = 'Infinity'
        else:
            total = numb1 / numb2
    elif function == '2':
        total = numb1 * numb1
    elif function == '3':
        total = numb1 * numb1 * numb1
    else:
        print('[ERROR] - ' + function + ' is not a valid function!')
        start()

def tryagain():
    again = input('Would you like to go again? (y/n) | ')
    if again == 'y' or again == 'Y':
        again = True
    elif again == 'n' or again == 'N':
        again = False
    else:
        print('[ERROR] - ' + again + ' is not a valid input')
        print(" Type 'y' to go again, or type 'n' to exit")
        tryagain()
    return again
    

def start():
    print()
    print('Calculator v0.2 - Ctrl + C to quit')
    print('Made by Ethan Crooks')
    print()
    getnumbs()
    gettotal()
    print()
    if function == 'a':
        print(' ' + str(numb1) + ' + ' + str(numb2) + ' = ' + str(total))
    elif function == 's':
        print(' ' + str(numb1) + ' - ' + str(numb2) + ' = ' + str(total))
    elif function == 'm':
        print(' ' + str(numb1) + ' x ' + str(numb2) + ' = ' + str(total))
    elif function == 'd':
        print(' ' + str(numb1) + ' / ' + str(numb2) + ' = ' + str(total))
    elif function == '2':
        print(' ' + str(numb1) + ' squared is ' + str(total))
    elif function == '3':
        print(' ' + str(numb1) + ' cubed is ' + str(total))
    if tryagain() == True:
        print()
        print()
        print('---')
        print()
        print()
        start()
    else:
        print('Exiting...')
        
        

start()
    
