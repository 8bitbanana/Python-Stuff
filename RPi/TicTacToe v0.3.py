# Noughts and Crosses for Python (v0.3)
# Main code by Mike Cook. Edited by Ethan Crooks.

import random

board = [ ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ' ]
wins = [ [0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]

def swapPlayer(player): #Swaps players
    if player == 'X' :
        player = 'O'
    else:
        player = 'X'
    return player

def getMove(player):
    global board
    correct_number = False
    while correct_number == False :
        square = input('Which square shall an '+ player +' go in? ')
        try: 
            square = int(square)
        except:
            square = -2
        square -= 1 # make input number match internal numbers
        if square >= 0 and square < 10 : # number in range
            if board[square] == ' ' : # if it is blank
                board[square] = player
                correct_number = True
            else:
                print ('Square already occupied, try again.')
        else:
            print ('Incorrect square, try again.')

def wipeBoard() :       #Wipe the board
    global board
    for square in range(0,len(board)):
        board[square] = ' '


def printBoard():       #Print the board
    print()
    print('-------------')
    print('| '+board[0]+' | '+board[1]+' | '+board[2]+' |')
    print('-------------')
    print('| '+board[3]+' | '+board[4]+' | '+board[5]+' |')
    print('-------------')
    print('| '+board[6]+' | '+board[7]+' | '+board[8]+' |')
    print('-------------')
    print()

def canMove():          #See if a move can be made
    move = False
    for square in range(0, len(board)):
        if board[square] == ' ':
            move = True
    return move

def checkWin(player):   #Check if a player has won
    win = False
    for test in wins :
        count = 0
        for squares in test :
            if board[squares] == player :
                count +=1
        if count == 3 :
            win = True
    return win

def playerturn():
    a = random.randint(0,1)
    if a == 0:
        return 'X'
    elif a == 1:
        return 'O'
    else:
        return 'X'

def play() :             #Play the game!
    print ()
    print (' ================================ ')
    print (' |Noughts and Crosses for Python| ')
    print (' ================================ ')
    print ('       Two player version')
    print ()
    print ()
    printBoard()
    while True :
        wipeBoard()
        player_turn = playerturn()
        while checkWin(swapPlayer(player_turn)) == False and canMove() == True :
            getMove(player_turn)
            printBoard()
            player_turn = swapPlayer(player_turn)
        if checkWin(swapPlayer(player_turn)):
            print ('Player ',swapPlayer(player_turn),' wins!')
            print ('>>>New game<<<')
            wipeBoard()
            printBoard()
        else:
            print ("It's a draw!")
            print ('>>>New game<<<')
            wipeBoard()
            printBoard()

if __name__ == '__main__':
    play()
