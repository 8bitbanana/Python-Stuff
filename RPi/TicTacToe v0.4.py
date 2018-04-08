# Noughts and Crosses for Python (v0.3)
# Main code by Mike Cook. Edited by Ethan Crooks.

import random
from random import shuffle

board = [ ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ' ]
wins = [ [0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]

def swapPlayer(player): #Swaps players
    if player == 'X' :
        player = 'O'
    else:
        player = 'X'
    return player

def generateMove():
    if win_block():
        pass
    else:
        randomMove()

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

def checkWin(player,bor):   #Check if a player has won
    win = False
    for test in wins:
        count = 0
        for squares in test:
            if bor[squares] == player:
                count += 1
        if count == 3:
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

def play() :
    printstartscreen()   #Play the game!
    printBoard()
    while True :
        wipeBoard()
        player_turn = playerturn()
        while checkWin(swapPlayer(player_turn),board) == False and canMove() == True :
            getMove(player_turn)
            printBoard()
            player_turn = swapPlayer(player_turn)
        if checkWin(swapPlayer(player_turn),board):
            print ('Player ',swapPlayer(player_turn),' wins!')
            print ('>>>New game<<<')
            wipeBoard()
            printBoard()
        else:
            print ("It's a draw!")
            print ('>>>New game<<<')
            wipeBoard()
            printBoard()

def randomMove():
    global board
    moves = list()
    for squares in range(0,len(board)):
        if board[squares] == ' ':
              moves.append(squares)
    shuffle(moves)
    board[moves[0]] = '0'
    print('My move is ' + str(moves[0]+1) + '.')

def canIwin():  # [OLD]
    global board
    testBoard = board # make a fake copy of the board
    moveMade = False
    for square in range(0,len(board)):
        if testBoard[square] == ' ' and moveMade == False:
            testBoard[square] = 'O'
            if checkWin('O',testBoard):
                board[square] = 'O'
                moveMade = True
                print('my move is ' + str(square +1) + '.')
            else:
                testBoard[square] = ' ' # retract move
    return moveMade

def win_block(): # move to win or block
    global board
    testBoard = board
    players = ['O','X']
    moveMade = False
    for moveTry in players:
        for square in range(0,len(board)):
            if testBoard[square] == ' ' and moveMade == False:
                testBoard[square] = moveTry
                if checkWin(moveTry,testBoard):
                    board[square] = 'O'
                    moveMade = True
                    print('My move is ' + str(square + 1) + '.')
                else:
                    testBoard[square] = ' ' # retract move

def canYouWin(): # [OLD]
    global board
    testBoard = board
    moveMade = False
    for square in range(0,len(board)):
        if testBoard[square] == ' ' and moveMade == False:
            testBoard[square] = 'X'
            if checkWin('X',testBoard):
                board[square] = 'O'
                moveMade = True
                print('My move is ' + str(square+1) + '.')
            else:
                testBoard[square] = ' '  #retract move
    return moveMade

def playcpu1():
    global board
    printstartscreen()
    print('Play against computer AI level 1')
    printBoard()
    while True:
        wipeBoard()
        player_turn = 'X'
        while checkWin(swapPlayer(player_turn),board) == False and canMove()== True:
            if player_turn == 'X':
                getMove(player_turn)
            else:
                randomMove()
            printBoard()
            player_turn = swapPlayer(player_turn)
        if checkWin(swapPlayer(player_turn),board):
            print('Player ' + swapPlayer(player_turn) + ' wins!')
            print()
            print('<<<NEW GAME>>>')
        else:
            print("It's a draw!")
            print()
            print('<<<NEW GAME>>>')
        print()
        wipeBoard()
        printBoard()

def playcpu2():
    global board
    printstartscreen()
    print('Play against computer AI level 2')
    printBoard()
    while True:
        wipeBoard()
        player_turn = 'X'
        while checkWin(swapPlayer(player_turn),board) == False and canMove()== True:
            if player_turn == 'X':
                getMove(player_turn)
            else:
                generateMove()
            printBoard()
            player_turn = swapPlayer(player_turn) # swaps players
        if checkWin(swapPlayer(player_turn),board):
            print('Player ' + swapPlayer(player_turn) + ' wins!')
            print()
            print('<<<NEW GAME>>>')
        else:
            print("It's a draw!")
            print()
            print('<<<NEW GAME>>>')
        print()
        wipeBoard()
        printBoard()


def printstartscreen():
    print ()
    print (' ================================ ')
    print (' |Noughts and Crosses for Python| ')
    print (' ================================ ')
    print ('       Version 0.4')
    print ()
    print ()

if __name__ == '__main__':
    playcpu2()
