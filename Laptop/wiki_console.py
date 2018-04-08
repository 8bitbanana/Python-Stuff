import wikipedia as wiki
import sys, os, textwrap, unicodedata

def display(string):
    string = unicodedata.normalize('NFKD', string).encode('ascii','ignore')
    string = textwrap.fill(string, 100)
    return string

def cls():
    if "idlelib" in sys.modules:
        print('\n' * 100)
        return 0
    elif os.name == 'nt':
        os.system('cls')
    elif os.name == 'posix':
        os.system('clear')
    else:
        print('\n' * 100)

def print_search(results, summary=False):
    if len(results) == 0:
        print('No results found!')
    if summary:
        print('[S] - Summary')
    for x in range(1,len(results)):
        print('[{}] - {}'.format(x, display(results[x])))

def pageselect(search_results):
    print_search(search_results)
    print()
    print('Select a page, or 0 to search again')
    selection = input('>>> ')
    if selection == '0':
        return False
    try:
        selection = int(selection)
        page_title = search_results[selection]
    except TypeError:
        print('Not a number!')
        print()
        pageselect(search_results)
    except IndexError:
        print('Out of range!')
        print()
        pageselect(search_results)
    return wiki.page(page_title)

def sectionselect(page):
    print_search(page.sections, True)
    print()
    print('Select a section, or 0 to search again')
    selection = input('>>> ')
    if selection == '0':
        return False
    if selection.upper() == 'S':
        return 'Summary'
    try:
        selection = int(selection)
        page_title = page.sections[selection-1]
    except TypeError:
        print('Not a number!')
        print()
        sectionselect(page)
    except IndexError:
        print('Out of range!')
        print()
        sectionselect(page)
    return page_title

def main():
    while True:
        cls()
        print('Python Wikipedia Console')
        print()
        user_search = input('Search Wikipedia for ')
        search_results = wiki.search(user_search)
        page = pageselect(search_results)
        if page == False:
            continue
        print(display(page.summary))
        print()
        while True:
            section = sectionselect(page)
            if section == False:
                break
            elif section == 'Summary':
                print(display(page.summary))
            else:
                print(display(page.section(section)))
            input()

if __name__ == "__main__":
    main()
