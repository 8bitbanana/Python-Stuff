# Prime Finder v1.0 (dev)
# By Ethan Crooks

import math
import time

count = 1
recp = 1

def isprime(num):
    #print(str(num))
    num = float(num)
    prime = True
    if math.fmod(num,2) == 0.0:
        prime = False
    if math.fmod(num,3) == 0.0:
        prime = False
    if math.fmod(num,5) == 0.0:
        prime = False
    if math.fmod(num,7) == 0.0:
        prime = False
    if num == 2.0 or num == 3.0 or num == 5.0 or num == 7.0:
        prime = True
    if num == 1.0:
        prime = False
    #print(str(prime))
    return prime

def gettestnum():
    print('Type in number to test.')
    a = input('>>> ')
    try:
        int(a)
    except ValueError:
        print('[ValueError]')
        print('Needs to be a whole number!')
        print()
        gettestnum()
    return a

def testsingle():
    a = gettestnum()
    result = isprime(float(a))
    if result == True:
        print(a + ' is a prime!')
    else:
        print(a + " isn't a prime!")
    print()
    main()

def testall():
    global count
    global recp
    while True:
        totalcount = 1
        result = isprime(float(count))
        if result == True:
            print(str(count))
        count += 1
    if recp >= 950:
        pass
    else:
        recp += 1
        testall()


testall()
