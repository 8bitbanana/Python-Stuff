descfile = 'descriptions.txt'

def parse_file(file): # Takes a filename
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

def main(): # Main function - takes nothing, returns nothing.
    all_items = parse_file(descfile)
    while True:
        user_items = get_user_input(all_items)
        total_price = calculate_total_price(user_items)
        print_receipt(user_items, total_price)

main()
