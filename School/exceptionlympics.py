import time

points = 0
count = 0

result = 'Error'

hitarray = [
    'Miss!',
    'Miss!',
    'Miss!',
    'Miss!',
    'Miss!',
    'Close!',
    'Close!',
    'Close!',
    'So close!',
    'Good shot!',
    'So close!!',
    'Close!',
    'Close!',
    'Close!',
    'Miss!',
    'Miss!',
    'Miss!',
    'Miss!',
    'Miss!'
    ]

hitdict = {
    'Close!':'|',
    'So close!':'[',
    'So close!!':']',
    'Good shot!':'O',
    'Miss!':'-'
    }

pointsdict = {
    'Close!':10,
    'So close!':30,
    'So close!!':30,
    'Good shot!':100,
    'Miss!':1
    }

while True:
    print('3...',end='')
    time.sleep(0.5)
    print('2...',end='')
    time.sleep(0.5)
    print('1...',end='')
    time.sleep(0.5)
    print('GO!')
    print('Hit Ctrl+C at the right time!')
    print('',end='')
    try:
        while True:
            for x in hitarray:
                result = x
                print(hitdict[result],end='')
                time.sleep(0.01)
            print()
    except KeyboardInterrupt:
        print('\n\n')
        print(result)
        print()
        points_add = pointsdict[result]
        print('+'+str(points_add))
        points+=points_add
        count+=1
        print('Total - '+str(points)+' points \n     in '+str(count)+' tries')
        print()
    try:
        a=input('Hit Ctrl+C to go again')
    except KeyboardInterrupt:
        pass
