descfile = 'descriptions.txt'

# Description file is formatted like this:
#
# 34512340            <- GTIN-8 Code
# plain brackets      <- Item Description
# 0.5                 <- Price (as a float)
# ---                 <- Divider between items (for readabilty)
# 56756777
# 100mm bolts
# 0.2
# ---

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
    return items # Returns all items in a list of dictionaries

def get_user_input(): # Takes nothing
    user_inputs = []
    user_quantities = []
    print('Enter GTIN-8 numbers to purchase, or type nothing to finish')
    while True:
        print()
        print(' ########')
        a=input('-')
        if a=='':
            break
        user_inputs.append(a)
    for x in user_inputs:
        print('How much of ' + x + '?')
        a=int(input('-'))
        user_quantities.append(a)
    return user_inputs, user_quantities # Returns a list of the users inputs
                                        # and a matching list of the users
                                        # quantities

def search_for_gtin(user_inputs, user_quantities, items):
    user_items = []
    not_found = []
    for selected_item in user_inputs:
        found = False
        for searching in items:
            if selected_item == searching['gtin']:
                user_items.append(searching)
                found = True
        if not found:
            not_found.append(selected_item)
            user_quantities[user_inputs.index(selected_item)] = 0
    return user_items, user_quantities, not_found

def calculate_total_price(user_items, user_quantities): # Takes a list of the users personal items
    total_price = 0
    for current_item in user_items:
        total_price += float(current_item['price'])
    return total_price # Returns the total price as a float

def print_not_found(not_found): # Takes a list of the not found GTIN-8 codes
    if not_found!=list():
        for x in not_found:
            print('Code ' + x + ' was not found.')
        return True
    else:
        return False

def again_query(): # Takes nothing
    print('Would you like to start again?')
    again=input('(y/n) - ').lower()
    if a=='y':
        again=True
    elif a=='n':
        again=False
    else:
        print('Type y or n')
        again=again_query()
    return again # Returns boolean of users choice

def print_receipt(user_items, total_price): # Takes a list of the users
    print('===RECEIPT===')                  # personal items and a float of the
    for selected_item in user_items:        # total price
        print(selected_item['gtin']+' '+selected_item['desc']+' '+selected_item['price'])
    print('TOTAL PRICE = £' + str(total_price))

def main():
    all_items = parse_file(descfile)
    while True:
        user_inputs, user_quanitites = get_user_input()
        user_items, not_found = search_for_gtin(user_inputs, all_items)
        break
    total_price = calculate_total_price(user_items, user_quanitites)
    print_receipt(user_items, total_price)

main()
