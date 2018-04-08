import math
def gtincheck(gtin):
    multiply = [3,1,3,1,3,1,3]
    if len(gtin)!=7:
        print('Wrong length')
        return 'error'
    gtin=list(gtin)
    for x in range(0,7):
        try:
            gtin[x]=int(gtin[x])
        except ValueError:
            print('Not a number')
            return 'error'
    gtin_multi = []
    gtin_total = 0
    for x in range(0,7):
        gtin_multi.append(gtin[x]*multiply[x])
    for x in range(0,7):
        gtin_total+=gtin_multi[x]
    a=math.ceil(gtin_total/10.0)*10
    check_digit = a-gtin_total
    return check_digit

while True:
    print('                      #######')
    gtin=input('Enter a GTIN-8 code - ')
    check_digit = gtincheck(gtin)
    if check_digit!='error':
        print('Check digit is '+ str(check_digit))
        print('Complete code - '+gtin+str(check_digit))
        print()
