def gtincheck(gtin):
    multiply = [3,1,3,1,3,1,3,1]
    if len(gtin)!=8:
        print('Wrong length')
        return False
    gtin=list(gtin)
    for x in range(0,8):
        try:
            gtin[x]=int(gtin[x])
        except ValueError:
            print('Not a number')
            return False
    gtin_multi = []
    gtin_total = 0
    for x in range(0,8):
        gtin_multi.append(gtin[x]*multiply[x])
    for x in range(0,8):
        gtin_total+=gtin_multi[x]
    gtin_total/=10
    gtin_total_test = int(gtin_total)
    if gtin_total_test==gtin_total:
        print('Valid - '+str(gtin_total))
        return True
    else:
        print('Failed validity check - '+str(gtin_total))
        return False

while True:
    gtin=input('Enter a GTIN-8 code - ')
    result = gtincheck(gtin)
