# Slots machine simulator
# By Ethan Crooks

import random as ra
import time as ti

# Basic program setup
global version,indef
version = '1.0'
indef = True
if indef == True:
    version = version + ' (dev)'
def ni():
    print('Not implimented')
def br():
    print()
    print('---')
    print()
def loop():
    loop()
# ---

# Variable setup
global money,bet,slot1,slot2,slot3,slotlist,prizes,jackpot,startmoney

money = 100
startmoney = 100

bet = 1

slot1 = 1

slot2 = 1

slot3 = 1

jackpot = ra.randint(10,50)

slotlist = ['(`)','BAR','777','£££','oOo','WIN','(`)','(`)','oOo','BAR','£££']

prizes = [2,4,7,6,3,1337,2,2,3,4,6]

#slotlist = ['lol']
#prizes = [1337]

prizes[5]=jackpot

if len(slotlist)!=len(prizes):
    print('ERROR! Slotlist != Prizes!')
    print('Terminating!')
    print('Wait a moment...')
    loop()
    
# ---


def main():
    print(' [Todays Jackpot = ' + str(jackpot) + 'x!]')
    print()
    print(' SLOT MACHINE SIMULATOR')
    print('              ' + version)
    print()
    startmenu()

def startmenu():
    global money,startmoney
    print('1:Play 2:Settings 3:Credits 4:Exit')
    a = input('>>> ')
    print()
    if a == '1':
        print('Starting game...')
        money=startmoney
        br()
        play()
    elif a == '2':
        settings()
    elif a == '3':
        print('By Ethan Crooks')
        print()
        startmenu()
    elif a == '4':
        loop()
    else:
        print('Type a 1, 2, 3 or 4.')
        print()
        startmenu()

def settings():
    global startmoney
    print('Settings')
    print('[1] - Set starting credits')
    print('[2] - Set spin time')
    a = input('>>> ')
    if a == '1':
        print()
        print('Set starting credits.')
        print('Current - £' + str(startmoney))
        startmoney = input('>>> ')
        startmoney = int(startmoney)
    elif a == '2':
        ni()
    else:
        settings()
    startmenu()

def play():
    global bet,money,startmoney
    printmoney()
    bet = betfunc()
    slot1, slot2, slot3 = getslots()
    print()
    null = input('PRESS ENTER TO PULL THE LEVER!')
    print()
    print('Spinning...')
    ti.sleep(ra.randint(1,1))
    printslots(slot1,slot2,slot3)
    if slot1 == slot2 and slot2 == slot3:
        print('WINNER!')
        prizemoney = prize(slot1,bet)
        print('+£'+str(prizemoney))
        money = money+prizemoney
    else:
        print('Better luck next time!')
    if money<=0:
        broke()
    br()
    play()

def printmoney():
    print('Credits - £' + str(money))

def betfunc():
    global money
    print()
    print('How much would you like to bet?')
    a = input('>>> ')
    try:
        int(a)
    except ValueError:
        print()
        print('Type a number!')
        a=0
        betfunc()
    if int(a) > money:
        print()
        print('You only have £' + str(money) + '!')
        print('Bet a smaller amount!')
        a=0
        betfunc()
    a = abs(int(a))
    a = str(a)
    print()
    print('Betting £' + a + '...')
    money-=int(a)
    return a

def getslots():
    a = ra.randint(0,len(slotlist)-1)
    b = ra.randint(0,len(slotlist)-1)
    c = ra.randint(0,len(slotlist)-1)
    d = slotlist[a]
    e = slotlist[b]
    f = slotlist[c]
    return d,e,f

def printslots(a,b,c):
    print()
    print('===============')
    print('['+str(a)+']['+str(b)+']['+str(c)+']')
    print('===============')
    print()

def prize(slot,bet):
    global money,prizes
    prize = 1337
    if slot == 'WIN':
        printjackpot()
    slotnum = getslotnumber(slot)
    print(str(slotnum))
    prize = int(prizes[slotnum])*int(bet)
    return prize

def getslotnumber(slot):
    global slotlist
    result = -1
    for x in range(0,len(slotlist)):
        if slotlist[x] == slot:
            result = x
    return result

def broke():
    print('You are out of money!')
    br()
    startmenu()

def printjackpot():
    print('========================')
    print('[       JACKPOT!       ]')
    print('========================')
    print()
main()
