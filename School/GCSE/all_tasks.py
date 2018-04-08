import math # To use the math.ceil() function to round upwards

descfile = 'descriptions.txt'
stockfile = 'stock.txt'

# all_items = A list of dictioaries of all possible products, with descriptions
# stock_items = A list of dictionaries of all possible products with stock levels
# user_items = A list of dictionaries of the users persoanl products from all_items
# reorder = A list of dictionaries of the products that need to be reordered
# descfile = The directory of the product description .txt file
# stockfile = The directory of the stock levels .txt file

# TASK 1 CHECK DIGIT

def checkdigit(gtin):
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

def task1_check_main(repeat=True):
    while True:
        print('                      #######')
        gtin=input('Enter a GTIN-8 code - ')
        check_digit = checkdigit(gtin)
        if check_digit!='error':
            print('Check digit is '+ str(check_digit))
            print('Complete code - '+gtin+str(check_digit))
            print()
        if not repeat:
            break


# TASK 1 VALIDITY

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

def task1_validity_main(repeat=True):
    while True:
        gtin=input('Enter a GTIN-8 code - ')
        result = gtincheck(gtin)
        if not repeat:
            break


# TASK 2

def parse_desc_file(file): # Takes a filename
    items = []
    f = open(file)
    raw = f.read().splitlines()
    f.close()
    while True:
        try:
            a=raw[0]
        except IndexError:
            break
        gtin = raw.pop(0)
        desc = raw.pop(0)
        price = raw.pop(0)
        item = {'gtin':gtin,'desc':desc,'price':price}
        items.append(item)
        raw.remove('---')
    return items # Returns a list of dictionaries of all possible items

def get_user_input(items): # Takes a list of dictionaries of all possible items
    user_inputs = []
    user_items = []
    print('Enter GTIN-8 numbers to purchase, or type nothing to finish')
    while True:
        print()
        print(' ########')
        gtin=input('-')
        if gtin=='':
            break
        result, found_code = query_gtin(gtin,items)
        if result:
            print(found_code['desc'])
            user_inputs.append(gtin)
            user_items.append(found_code)
        else:
            print('Not found!')
    for x in range(0,len(user_inputs)):
        print('How much of ' + user_items[x]['gtin'] + '?')
        a=int(input('-'))
        user_items[x]['quant']=a
    return user_items # Returns a list of dictionaries of all of the user's
                      #                                      personal items
                      
def query_gtin(gtin,items): # Takes a gtin-8 code and a list of dictionaries
    found = False           # of all possible items
    found_code = {}
    for searching in items:
        if searching['gtin'] == gtin:
            found_code = searching
            found = True
            break
    return found, found_code # Returns if the gtin-8 code is found or not (bool)
                             # and a dictionary of the found gtin-8 code

def calculate_total_price(user_items): # Takes a list of dictionaries of the
    total_price = 0                    # user's personal items
    for current_item in user_items:
        total_price += float(current_item['price'])*float(current_item['quant'])
    return total_price # Returns the total price (float)

def print_receipt(user_items, total_price): # Takes a list of dictionaries of 
    print()                                 # the user's personal items and
    print('===RECEIPT===')                  # the total price (float)
    for selected_item in user_items:
        print(selected_item['gtin']+' '+selected_item['desc']+' £'+selected_item['price']+' x'+str(selected_item['quant']))
    print('TOTAL PRICE = £' + str(total_price))
    print() # Returns nothing

def task2_main(repeat=True): # Main function of task 2
    all_items = parse_desc_file(descfile)
    while True:
        user_items = get_user_input(all_items)
        total_price = calculate_total_price(user_items)
        print_receipt(user_items, total_price)
        if not repeat:
            break
    return user_items

# TASK 3

def parse_stock_file(file): # Takes a filename
    items = []
    f = open(file)
    raw = f.read().splitlines()
    f.close()
    while True:
        try:
            a=raw[0]
        except IndexError:
            break
        gtin = raw.pop(0)
        current = int(raw.pop(0))
        reorder = int(raw.pop(0))
        target = int(raw.pop(0))
        item = {'gtin':gtin,'current':current,'reorder':reorder,'target':target}
        items.append(item)
        raw.remove('---')
    return items # Returns a list of dictionaries of all possible items in the
                 # stock file

def update_stock_levels(stock_items, user_items):
    for x in user_items:
        for y in stock_items:
            if x['gtin']==y['gtin']:
                y['current']-=int(x['quant'])
    return stock_items

def check_stock_levels(stock_items):
    reorder=[]
    for x in stock_items:
        if x['current']<=x['reorder']:
            amount_needed = x['target']-x['current']
            reorder.append({'gtin':x['gtin'],'order':amount_needed})
    return reorder

def print_order(reorder,all_items):
    print('===ORDER===')
    blank=True
    for x in reorder:
        found, found_code = query_gtin(x['gtin'],all_items)
        print(x['gtin']+' '+found_code['desc']+' x'+str(x['order']))
        blank=False
    if blank:
        print('Nothing to order!')

def update_stock_file(user_items,file,reorder):
    f=open(file,'r')
    currentfile=f.read().splitlines()
    f.close()
    for x in user_items:
        indx=0
        for y in currentfile:
            if x['gtin']==y:
                currentfile[indx+1]=str(int(currentfile[indx+1])-x['quant'])
            indx+=1
    if len(reorder)!=0:
        for x in reorder:
            indx=0
            for y in currentfile:
                if x['gtin']==y:
                    currentfile[indx+1]=str(int(currentfile[indx+1])+x['order'])
                indx+=1
    file_str=''
    for x in currentfile:
        file_str+=x+'\n'
    f=open(file,'w')
    f.write(file_str)
    f.close()
    

def task3_main(): # Main function of task 3
    all_items = parse_desc_file(descfile)
    stock_items = parse_stock_file(stockfile)
    user_items = task2_main(False)
    stock_items = update_stock_levels(stock_items, user_items)
    reorder = check_stock_levels(stock_items)
    update_stock_file(user_items,stockfile,reorder)
    print_order(reorder,all_items)

def print_stock_file(file):
    f=open(file,'r')
    print(f.read().splitlines())
    f.close()

def main():
    print('CCA PROGRAM')
    print('     Ethan Crooks')
    while True:
        print()
        print('[1] - Check digit generation')
        print('[2] - GTIN-8 valitity check')
        print('[3] - Purchase products (without stock check)')
        print('[4] - Purchase products (with stock check)')
        print()
        a=input('>>> ')
        if a=='1':
            task1_check_main(False)
        elif a=='2':
            task1_validity_main(False)
        elif a=='3':
            task2_main(False)
        elif a=='4':
            task3_main()
            #print_stock_file(stockfile)
        else:
            print('Enter a number from 1-4')

main()
