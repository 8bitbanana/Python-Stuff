from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import base64 as b
import itertools as i

phantomjs_exe = ".\\bin\\phantomjs.exe" # Directory of PhantomJS
username = "[redacted]"
web_delay = 2 # How long to wait after each action

last = ""
def pnd(a): # Print, but avoid duplicates
    global last
    if not a == last:
        print(a)
        last = a

# After writing this nonsense I realise it will be piss easy to get the password from this
# and at this point I don't really care. Have fun
l7="=1N{}Y=";l7=l7.format("QzM");v4=b.b64decode(b'NTQ2MTIzMDc=').decode("ascii");ln=""
exec(b.b64decode(b'[redacted]==').decode("ascii"))
def t(c, k):
    ik = i.chain.from_iterable(i.repeat(k))
    return ''.join(chr(ord(a)^ord(b)) for a, b in zip(c, ik))


print("Opening browser...",end="")
driver = webdriver.Firefox()
#driver = webdriver.PhantomJS(phantomjs_exe)
xpath = driver.find_element_by_xpath

print("done.\nOpening the website...",end="")
driver.get("http://aternos.org") # Open the aternos website
assert "Aternos" in driver.title
print("done.\nLogging in...",end="")
xpath('/html/body/nav/div[2]/div/ul/li[6]/a').click() # Click on "play" button
sleep(web_delay)
assert "Login" in driver.title

user_field = xpath('//*[@id="go-x-user"]') # Username field
pass_field = xpath('//*[@id="go-x-pw1"]') # Password field

user_field.send_keys(username) # Type in login credentials
pass_field.send_keys(t("\x6c\x65\x58\x54\x41\x42\x74\x47\x40\x53\x6a",b.b64decode(ln).decode("ascii")))
sleep(web_delay)
xpath('/html/body/div[7]/div[2]/div[1]/div[1]/form/span[2]/button').click() # Log in!
print("done.\nStarting server...\n")

# All the buttons that are not on screen are still there, just hidden and unclickable.
# Therefore they can still be taken by xpath()
start_button = xpath('//*[@id="start"]')
stop_button = xpath('//*[@id="stop"]')
confirm_button = xpath('//*[@id="confirm"]')
sleep(web_delay)

assert "Server" in driver.title

confirmed = False
# Wait in the queue, check the current state and act accordingly.
# The "state" is the class attribute of the div that encloses all the buttons
while True:
    state = xpath('/html/body/div[1]/main/section/div[3]/div[3]').get_attribute("class").strip()
    pnd("STATE = " + state.replace("server-actions ","")) # Print the current state
    if state == "server-actions offline": # Click the start button
        if confirmed:
            print("Seems offline, trying refresh")
            driver.refresh()
            sleep(web_delay)
            confirmed = False
        else:
            start_button.click()
            print("Clicking start button")
            try: # Sometimes a popup appears. Try to click it, continuing after exception
                xpath('/html/body/div[1]/main/div/div/div/header/span/i').click()
                sleep(web_delay)
                print("Clicking notification X button")
            except:
                pass
    elif state == "server-actions queueing waiting": # Wait for confirm button
        pass
    elif state == "server-actions queueing pending": # Click confirm button
        confirm_button.click()
        confirm = True
        print("Clicking confirm button")
    elif state == "server-actions queueing ready": # Wait in queue some more
        pass
    elif state == "server-actions loading": # Something is happening, notify and wait
        pass
    elif state == "server-actions online": # Server is (hopefully) up
        break
    else: # Halp
        raise Exception("Unknown state '" + state + "'")
    sleep(1)
print("Done!")
driver.quit() # Quit the browser
input()