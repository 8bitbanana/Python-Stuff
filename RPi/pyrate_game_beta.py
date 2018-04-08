from tkinter import *
import random,time

game_title = 'PYrate Game Beta'
game_desc = 'This is an beta. Some features may be unusable or unavailable.'

game_length = 5 # <- How long the game is.

def debug(msg):
    if DEBUG:
        print(msg)

DEBUG = False # <- Debug mode

grid_base = [
    ' 200',' 200','[RB]','[RB]','[PR]','[KL]',
    '1000','[PR]','3000',' 200','[KL]','1000',
    ' 200','[KL]',' 200',' 200','1000',' 200',
    '1000',' 200','5000',' 200','1000','[BK]',
    ' 200','[BM]',' 200','1000',' 200',' 200',
    '1000','1000','[x2]','3000',' 200','1000'
    ]   # SHIELD HAS BEEN REMOVED, AS UNIMPLIMENTED

# Blank Variables
grid = []
grid_p1 = []
grid_p2 = []
grid_p3 = []
grid_p4 = []
points = 0
points_p1 = 0
points_p2 = 0
points_p3 = 0
points_p4 = 0
bank = 0
bank_p1 = 0
bank_p2 = 0
bank_p3 = 0
bank_p4 = 0
robbed_points = 0
chosen_square = 'A1'
notification = ''
notification_p1 = ''
notification_p2 = ''
notification_p3 = ''
notification_p4 = ''
# ---------------

# Tkinter Reference
def ni():
    return 'Not implimented'
grid_dict = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6}
grid_dict_reverse = {0:'A',1:'B',2:'C',3:'D',4:'E',5:'F'}
square_dict = {' 200':'+200p','1000':'+1000p','3000':'+3000p','5000':'+5000p!',
              '[RB]':'Rob someones points','[KL]':'Kill someone',
               '[PR]':'Present','[SH]':'Equip Shield','[BM]':'Bomb!',
               '[x2]':'Double your score!','[BK]':'Bank your score!'}
action_dict = {' 200':'200 points have been added to your score.',
               '1000':'1000 points have been added to your score.',
               '3000':'3000 points have been added to your score.',
               '5000':'5000 points have been added to your score.',
               '[RB]':'Press continue to choose who to rob.',
               '[KL]':'Press continue to choose who to kill.',
               '[PR]':'Press continue to choose who to reward with 1000 points.',
               '[SH]':'You equiped a shield.',
               '[BM]':'Your score is now 0.',
               '[x2]':'Your score has been doubled.',
               '[BK]':'Your score has been banked.'}
info_dict = {'Rob Points':['Player ',' robbed Player ',"'s points."],
             'Kill someone':['Player ',' killed Player ','.'],
             'Present':['Player ',' gave Player ',' a present.']}
tk_info=0
info = []
target_return = 0
active_player = 2
active_power = None
# -----------------

# TKINTER APPLICATIONS=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
class MainApp: # App Id 1

    def get_square_text(square,grid):
        return 'Action: ' + square_dict[grid[square[0]][square[1]]]
    
    def get_action_text(square,grid):
        return '\n ' + action_dict[grid[square[0]][square[1]]] + ' \n'

    def setup():
        global grid_p1,grid_p2,_grid_p3,grid_p4,tk_info,grid,chosen_square_text,chosen_square_num,ui_label_text,info,active_power,points,points_p1,points_p2,points_p3,points_p4,bank,bank_p1,bank_p2,bank_p3,bank_p4,notification,notification_p1,notification_p2,notification_p3,notification_p4
        if tk_info == 1:
            points = points_p1
        elif tk_info == 2:
            points = points_p2
        elif tk_info == 3:
            points = points_p3
        elif tk_info == 4:
            points = points_p4
        else:
            raise Exception('Tkinter - Unknown Player ID')
        if tk_info == 1:
            bank = bank_p1
        elif tk_info == 2:
            bank = bank_p2
        elif tk_info == 3:
            bank = bank_p3
        elif tk_info == 4:
            bank = bank_p4
        else:
            raise Exception('Tkinter - Unknown Player ID')
        if tk_info == 1:
            grid = grid_p1
        elif tk_info == 2:
            grid = grid_p2
        elif tk_info == 3:
            grid = grid_p3
        elif tk_info == 4:
            grid = grid_p4
        if tk_info == 1:
            notification = notification_p1
        elif tk_info == 2:
            notification = notification_p2
        elif tk_info == 3:
            notification = notification_p3
        elif tk_info == 4:
            notification = notification_p4
        chosen_square_text = 'Chosen Square: ' + chosen_square
        chosen_square_break = [chosen_square[0],chosen_square[1]]
        chosen_square_num = [int(grid_dict[chosen_square_break[0]])-1,int(chosen_square_break[1])-1]
        points,bank = MainApp.take_action(chosen_square_num,grid,points,bank)
        MainApp.write_points(points,bank,tk_info)
        points_text = 'Points: ' + str(points)
        active_power = None
        bank_text = 'Banked: ' + str(bank) 
        ui_label_text = points_text + '\n' + bank_text + '\n\n' + chosen_square_text
        if tk_info == 1:
            grid = grid_p1
        elif tk_info == 2:
            grid = grid_p2
        elif tk_info == 3:
            grid = grid_p3
        else:
            grid = grid_p4
        if grid[int(chosen_square_num[0])][int(chosen_square_num[1])]=='[RB]':
            active_power = 'Rob Points'
        elif grid[int(chosen_square_num[0])][int(chosen_square_num[1])]=='[KL]':
            active_power = 'Kill someone'
        elif grid[int(chosen_square_num[0])][int(chosen_square_num[1])]=='[PR]':
            active_power = 'Present'
        else:
            active_power = None
        global square_text
        square_text = MainApp.get_square_text(chosen_square_num,grid)
        global action_text
        action_text = MainApp.get_action_text(chosen_square_num,grid)

    def write_points(points,bank,player):
        global points_p1,points_p2,points_p3,points_p4,bank_p1,bank_p2,bank_p3,bank_p4
        if player == 1:
            points_p1 = points
        elif player == 2:
            points_p2 = points
        elif player == 3:
            points_p3 = points
        elif player == 4:
            points_p4 = points
        if player == 1:
            bank_p1 = bank
        elif player == 2:
            bank_p2 = bank
        elif player == 3:
            bank_p3 = bank
        elif player == 4:
            bank_p4 = bank

    def take_action(chosen_square_num,grid,points,bank):
        square = grid[chosen_square_num[0]][chosen_square_num[1]]
        if square == ' 200':
            points += 200
        elif square == '1000':
            points += 1000
        elif square == '3000':
            points += 3000
        elif square == '5000':
            points += 5000
        elif square == '[BM]':
            points = 0
        elif square == '[x2]':
            points = points*2
        elif square == '[BK]':
            bank = points
            points = 0
        elif square == '[RB]' or square == '[KL]' or square == '[PR]':
            pass
        else:
            print('Error: Unknown action')
            print()
        return points,bank

    def __init__(self, master):
        MainApp.setup()
        frame = Frame(master)
        frame.pack()
        label = Label(frame, text=' ' + game_title + '\n\n By Ethan Crooks ', font='TkSmallCaptionFont')
        label.grid(row=1, column=0)
        label = Label(frame, text='Player ' + str(tk_info), font='TkCaptionFont')
        label.grid(row=0, column=1)
        label = Label(frame, text=MainApp.generate_grid(grid), font='TkFixedFont', relief=SUNKEN)
        label.grid(row=1,column=1)
        label = Label(frame, text=ui_label_text + ' ')
        label.grid(row=1,column=2)
        label = Label(frame, text=square_text)
        label.grid(row=2,column=1)
        label = Label(frame, text=action_text, relief=SUNKEN)
        label.grid(row=3,column=1)
        button = Button(frame, text='Continue',command=root.destroy)
        button.grid(row=4,column=1)
        label = Label(frame, text='\n'+notification+'\n', font='TkCaptionFont')
        label.grid(row=5,column=1)
        label = Label(frame, text=game_desc, font='TkTooltipFont')
        label.grid(row=6,column=1)


    def generate_grid(grid):
        temp_grid = ''
        temp_grid_item = 'xxxx'
        temp_grid += '   --1-----2----3----4----5----6--\n'
        for a in range(0,6):
            temp_grid_inner = ''
            for b in range (0,6):
                if b == 5:
                    temp_grid_item = '|' + grid[a][b] + '|'
                elif b == 0:
                    temp_grid_item = grid_dict_reverse[a] + ': |' + grid[a][b]
                else:
                    temp_grid_item = '|' + grid[a][b]
                temp_grid_inner += temp_grid_item
            temp_grid += temp_grid_inner + '\n'
        temp_grid += '   -------------------------------'
        return temp_grid

class TargetApp: # App Id 2
    def __init__(self,master):
        global active_player,active_power
        active_player = tk_info
        frame = Frame(master)
        frame.pack()
        label = Label(frame, text='Player ' + str(active_player), font='TkCaptionFont')
        label.grid(row=0,column=0)
        label = Label(frame, text='Choose a target for ' + active_power)
        label.grid(row=1,column=0)
        if active_player != 1:
            button = Button(frame, text=' Player 1 ', command=lambda: TargetApp.quit_(1), font='TkCaptionFont')
            button.grid(row=2,column=0)
        if active_player != 2:
            button = Button(frame, text=' Player 2 ', command=lambda: TargetApp.quit_(2), font='TkCaptionFont')
            button.grid(row=3,column=0)
        if active_player != 3:
            button = Button(frame, text=' Player 3 ', command=lambda: TargetApp.quit_(3), font='TkCaptionFont')
            button.grid(row=4,column=0)
        if active_player != 4:
            button = Button(frame, text=' Player 4 ', command=lambda: TargetApp.quit_(4), font='TkCaptionFont')
            button.grid(row=5,column=0)
        label = Label(frame, text=game_desc, font = 'TkTooltipFont')
        label.grid(row=6,column=0)

    def take_action(active_power,target_player,active_player):
        global points_p1,points_p2,points_p3,points_p4,robbed_points,notification,notification_p1,notification_p2,notification_p3,notification_p4
        if active_power == 'Kill someone':
            if target_player == 1:
                points_p1 = 0
                notification_p1 = 'You were killed by Player ' + str(active_player)
            elif target_player == 2:
                points_p2 = 0
                notification_p2 = 'You were killed by Player ' + str(active_player)
            elif target_player == 3:
                points_p3 = 0
                notification_p3 = 'You were killed by Player ' + str(active_player)
            elif target_player == 4:
                points_p4 = 0
                notification_p4 = 'You were killed by Player ' + str(active_player)
        elif active_power == 'Present':
            if target_player == 1:
                points_p1 += 1000
                notification_p1 = 'Player ' + str(active_player) + ' gave you a present.'
            elif target_player == 2:
                points_p2 += 1000
                notification_p2 = 'Player ' + str(active_player) + ' gave you a present.'
            elif target_player == 3:
                points_p3 += 1000
                notification_p3 = 'Player ' + str(active_player) + ' gave you a present.'
            elif target_player == 4:
                points_p4 += 1000
                notification_p4 = 'Player ' + str(active_player) + ' gave you a present.'
        elif active_power == 'Rob Points':
            if target_player == 1:
                robbed_points = points_p1
                points_p1 = 0
                notification_p1 = 'Your points were robbed by Player ' + str(active_player)
            elif target_player == 2:
                robbed_points = points_p2
                points_p2 = 0
                notification_p2 = 'Your points were robbed by Player ' + str(active_player)
            elif target_player == 3:
                robbed_points = points_p3
                points_p3 = 0
                notification_p3 = 'Your points were robbed by Player ' + str(active_player)
            elif target_player == 4:
                robbed_points = points_p4
                points_p4 = 0
                notification_p4 = 'Your points were robbed by Player ' + str(active_player)
            if target_player == 1:
                points_p1 += robbed_points
            elif target_player == 2:
                points_p2 += robbed_points
            elif target_player == 3:
                points_p3 += robbed_points
            elif target_player == 4:
                points_p4 += robbed_points
        else:
            raise Exception('Tkinter - Unknown Power ID')

    def quit_(r):
        global info_dict,info,active_power,active_player
        TargetApp.take_action(active_power, r, active_player)
        template = info_dict[active_power]
        info_temp = template[0] + str(active_player) + template[1] + str(r) + template[2]
        info.append(info_temp)
        root.destroy()

class InfoApp: # App Id 3:
    def __init__(self,master):
        global info
        frame = Frame(master)
        frame.pack()
        label = Label(frame, text='End of turn', font='TkCaptionFont')
        label.grid(row=0,column=0)
        label = Label(frame, text='\nRecent events:')
        label.grid(row=1,column=0)
        label = Label(frame, text=InfoApp.generate_info(info),font='TkCaptionFont')
        label.grid(row=2,column=0)
        button = Button(frame, text='Continue',command=root.destroy)
        button.grid(row=3,column=0)
        label = Label(frame, text=game_desc, font = 'TkTooltipFont')
        label.grid(row=4,column=0)

    def generate_info(inf):
        temp_info = '\n'
        for x in range(0,len(inf)):
            temp_info += ' '
            temp_info += inf[x]
            temp_info += ' \n'
        if len(inf) == 0:
            temp_info += 'Nothing happened this turn.\n'
        return temp_info
        
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

def launch_tkinter(app_id, window_name, extra_info=0):
    global root
    global tk_info
    if app_id == 1:
        w = 635
        h = 300
    elif app_id == 2:
        w = 310
        h = 150
    elif app_id == 3:
        w = 400
        h = 150
    else:
        w = 1000
        h = 1000
    tk_info = extra_info
    root = Tk()
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    root.wm_title(game_title + ' - ' + window_name)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    if app_id == 1:
        app = MainApp(root)
    elif app_id == 2:
        app = TargetApp(root)
    elif app_id == 3:
        app = InfoApp(root)
    else:
        raise Exception('Tkinter - Unknown App ID')
    root.mainloop()

def generate_random_grid():
    global grid_base
    grid = grid_base
    random.shuffle(grid)
    temp_grid = []
    temp_grid.append(grid[0:6])
    temp_grid.append(grid[5:12])
    temp_grid.append(grid[11:18])
    temp_grid.append(grid[17:24])
    temp_grid.append(grid[23:30])
    temp_grid.append(grid[29:36])
    return temp_grid

def choose_random_square():
    global chosen_squares
    chosen_squares = ['xx']
    a = random.randint(0,5)
    b = random.randint(0,5)
    alist = ['A','B','C','D','E','F']
    blist = [1,2,3,4,5,6]
    c = alist[a] + str(blist[b])
    chosen = False
    for x in range(0,len(chosen_squares)):
        if c == chosen_squares[x]:
            chosen = True
    if chosen == True:
        choose_random_square()
    chosen_squares.append(c)
    return c

def main():
    x = True
    while x == True:
        play()
        print()
        print('Whould you like to play again?')
        print('Type a y or an n')
        a = input('\> ')
        if a.lower == 'y':
            x = True
        else:
            x = False
        print()

def play():
    global grid_p1,grid_p2,grid_p3,grid_p4,game_length,chosen_square,active_power,points_p1,points_p2,points_p3,points_p4,bank_p1,bank_p2,bank_p3,bank_p4,notification_p1,notification_p2,notification_p3,notification_p4,info
    print('Generating grids...')
    grid_p1 = generate_random_grid()
    grid_p2 = generate_random_grid()
    grid_p3 = generate_random_grid()
    grid_p4 = generate_random_grid()
    print('Clearing screen...')
    for x in range(0,45):
        print()
    print('Welcome to the PYrate game!')
    turns = 1
    while turns<=game_length:
        chosen_square = 'xx'
        chosen_square = choose_random_square()
        print('Turn ' + str(turns) + '/' + str(game_length))
        print('Chosen square = ' + chosen_square)
        print()
        print('This window is for Player 1 only!')
        null = input('Make sure no-one else can see, then press enter.')
        print()
        launch_tkinter(1,'Player 1',1)
        if active_power != None:
            launch_tkinter(2, 'Player 1',1)
        print('This window is for Player 2 only!')
        null = input('Make sure no-one else can see, then press enter.')
        print()
        launch_tkinter(1,'Player 2',2)
        if active_power != None:
            launch_tkinter(2, 'Player 2',2)
        print('This window is for Player 3 only!')
        null = input('Make sure no-one else can see, then press enter.')
        print()
        launch_tkinter(1,'Player 3',3)
        if active_power != None:
            launch_tkinter(2, 'Player 3',3)
        print('This window is for Player 4 only!')
        null = input('Make sure no-one else can see, then press enter.')
        print()
        launch_tkinter(1,'Player 4',4)
        if active_power != None:
            launch_tkinter(2, 'Player 4',4)
        turns += 1
        launch_tkinter(3,'End of turn')
        notification_p1 = ''
        notification_p2 = ''
        notification_p3 = ''
        notification_p4 = ''
        info = []
    print()
    print('THE GAME HAS FINISHED!')
    if game_length == 1:
        print('After ' + str(game_length) + ' turn, the result is...')
    else:
        print('After ' + str(game_length) + ' turns, the result is...')
    time.sleep(2)
    print('(drum roll)')
    time.sleep(random.randint(3,5)-0.5)
    points_p1 += bank_p1
    points_p2 += bank_p2
    points_p3 += bank_p3
    points_p4 += bank_p4
    if points_p1 > points_p2 and points_p1 > points_p3 and points_p1 > points_p4:
        winner = 1
    elif points_p2 > points_p1 and points_p2 > points_p3 and points_p2 > points_p4:
        winner = 2
    elif points_p3 > points_p1 and points_p3 > points_p2 and points_p3 > points_p4:
        winner = 3
    elif points_p4 > points_p1 and points_p4 > points_p2 and points_p4 > points_p3:
        winner = 4
    else:
        winner = 'tie'
    print()
    p1_win = ''
    p2_win = ''
    p3_win = ''
    p4_win = ''
    if winner == 'tie':
        print('...a tie!')
    elif winner == 1:
        print('...Player 1 wins!')
        p1_win = ' - WINNER'
    elif winner == 2:
        print('...Player 2 wins!')
        p2_win = ' - WINNER'
    elif winner == 3:
        print('...Player 3 wins!')
        p3_win = ' - WINNER'
    elif winner == 4:
        print('...Player 4 wins!')
        p4_win = ' - WINNER'
    else:
        print('...error! I mucked up somewhere!')
    print()
    print('Player 1 - ' + str(points_p1) + p1_win)
    print('Player 2 - ' + str(points_p2) + p2_win)
    print('Player 3 - ' + str(points_p3) + p3_win)
    print('Player 4 - ' + str(points_p4) + p4_win)
    print()
    null = input('Press enter to continue.')
main()
