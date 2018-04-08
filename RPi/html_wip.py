from urllib.request import *
import time # For timer

DEBUG = True

def debug(msg=''):
    if DEBUG == True:
        if msg == '':
            print()
        else:
            print('['+str(msg)+']')

def test_for_internet():
    timer_start = time.time()
    u = 'http://google.com'
    internet = True
    try:
        f = urlopen(u)
        f.close()
    except:
        internet = False
    timer_end = time.time() - timer_start
    timer = int(round(timer_end,3)*1000)
    debug('Internet tested in ' + str(timer) + 'ms')
    debug('Result - ' + str(internet))
    return internet

def get_raw_html(url=None,retry=False):
    timer_start = time.time()
    # err-1 - No URL specified
    # err-2 - Unknown host without http:// - Retry
    # err-3 - Unknown host with http:// - Retry
    # err-4 - Unknown host after retrys
    # done - Success
    u = url
    result = ''
    contents = ''
    if u == None or u == '' or u == 'http://':
        result = 'err-1'
    else:
        try:
            f = urlopen(u)
            contents = f.read()
            f.close()
            result = 'done'
        except:
            if retry == False:
                if url[:7] == 'http://':
                    result = 'err-3'
                else:
                    result = 'err-2'
            else:
                result = 'err-4'
    timer_end = time.time() - timer_start
    timer = int(round(timer_end,3)*1000)
    debug('Raw HTML collected in ' + str(timer) + 'ms')
    debug('Result - ' + result)
    contents_length = len(contents)
    debug('Size - ' + str(contents_length) + ' bytes.')
    return result,contents

def main():
    debug('DEBUG MODE ENABLED')
    debug()
    print('Checking internet connection...')
    internet = test_for_internet()
    cont = True
    if internet == False:
        print()
        print('Error - Cannot connect to test server.')
        print('Check internet connection.')
        cont = False
    print()
    retry = False
    while cont == True:
        if retry == False:
            print('Type URL')
            input_url = input('http://')
            url = 'http://' + input_url
            print()
            print('Opening URL ' + url)
            debug()
            result, raw_html = get_raw_html(url,False)
            raw_html = str(raw_html)
            debug()
        if result == 'err-1':
            print('Error - No URL specified.')
            print()
            retry = False
        elif result == 'err-2':
            debug()
            result, raw_html = get_raw_html('http://' + url,True)
            debug()
            retry = True
        elif result == 'err-3':
            debug()
            result, raw_html = get_raw_html(url[7:],True)
            debug()
            retry = True
        elif result == 'err-4':
            print('Error - Unknown host.')
            print()
            retry = False
        elif result == 'done':
            retry = False
            print('Sucessfully recived HTML from')
            print(url)
            if len(raw_html) > 40000:
                print()
                print('This file is very large so it')
                print('may take a long time to process.')
            #time.sleep(1)
            debug()
            result, html = process_html(raw_html) ###
            print()
            html = filter_whitespace(html,'\n')
            html = filter_whitespace(html,'\t')
            html = filter_whitespace(html,'\\n')
            html = filter_whitespace(html,'\\t')
            html = filter_whitespace(html,'\\n\t')
            html = filter_whitespace(html,'\\t\n')
            html = filter_whitespace(html,'\\n\n')
            html = filter_whitespace(html,'\\t\t')
            html = filter_whitespace(html,'\r')
            html = filter_whitespace(html,'\\r')
            html = filter_whitespace(html,'\\n\r')
            html = filter_whitespace(html,'\\t\r')
            html = filter_whitespace(html,'\\r\r')
            html = filter_whitespace(html,'\\r\n')
            html = filter_whitespace(html,'\\r\t')
            print('Printing processed html...')
            print()
            if result == 'done':
                for x in range(0,len(html)):
                    if html[x][:2] == '\\n':
                        print(html[x][2:].strip())
                    elif html[x] == '' or html[x] == '\n' or html[x] == '\t':
                        pass
                    else:
                        print(html[x].strip())
            elif result == 'err-2':
                print('No text was detected in the HTML.')
                print()
            elif result == 'err-1':
                print('Error - Blank webpage.')
            else:
                print('Error - Unknown error.')
        else:
            print('Error - Unknown error.')
            retry = False

def filter_whitespace(text,filter):
    while True:
        try:
            text.remove(filter)
        except:
            break
    return text

def process_html_stub(raw_html):
    return 'done', raw_html

def process_html_p_tags(raw_html):
    timer_start = time.time()
    # err-1 - No <p> tags detected
    # done - Sucess
    raw_html = str(raw_html)
    result = 'xxxx'
    i = 0
    loop = 0
    html_p_tags = []
    while True:
        i = raw_html.find('<p>',i)
        if i == -1:
            if loop == 0:
                result = 'err-1'
            else:
                result = 'done'
            break
        j = raw_html.find('</p>',i+1)
        temp = raw_html[i+3:j]
        temp_chunks = int(len(temp) / 60)
        temp_process = ''
        for x in range(0,temp_chunks):
            temp_process += temp[(x)*60:(x+1)*60] + '\n'
            if x == temp_chunks-1:
                temp_process += temp[(x+1)*60:]
        if temp_process == '':
            temp_process = temp
        html_p_tags.append(temp_process)
        html_p_tags.append(' ')
        loop += 1
        i += 3
    timer_end = time.time() - timer_start
    timer = int(round(timer_end,3)*1000)
    debug('HTML processed in ' + str(timer) + 'ms')
    debug('Result - ' + result)
    return result,html_p_tags

def process_html(raw_html):
    timer_start = time.time()
    result = 'xxxx'
    # err-1 - Webpage is empty
    # err-2 - No HTML tags detected
    # done - Success
    html_list = list(raw_html)
    html_list.append('')
    raw_html_list = html_list
    loop = 0
    collected_text = []
    while True:
        #debug('LOOP ' + str(loop))
        text_list = []
        text_str = ''
        try:
            html_list.index('<')
        except:
            if loop == 0:
                if len(raw_html) == 0:
                    result = 'err-1'
                else:
                    result = 'err-2'
            else:
                result = 'done'
            break
        while html_list[0] != '>':
            html_list.remove(html_list[0])
        html_list.remove(html_list[0])
        try:
            while html_list[0] != '<':
                temp = html_list.pop(0)
                text_list.append(temp)
        except:
            pass
        text_str = compile_list(text_list)
        collected_text.append(text_str)
        loop += 1
    timer_end = time.time() - timer_start
    timer = int(round(timer_end,3)*1000)
    debug('HTML processed in ' + str(timer) + 'ms')
    debug('Result - ' + result)
    debug('Loops - ' + str(loop))
    return result, collected_text

def compile_list(list_):
    string = ''
    for x in range(0,len(list_)):
        string += list_[x]
    return string
        
main()
        
