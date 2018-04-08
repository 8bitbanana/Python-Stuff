from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from getpass import getpass

phantomjs_exe = ".\\bin\\phantomjs.exe"

username = input("ENTER USERNAME - ")
if username == "":
    f = open(".\\bin\\one_cred.txt")
    cred = f.read().splitlines()
    f.close()
    username = cred[0]
    password = cred[1]
    print("Using stored username \"" + username + "\"")
else:
    print()
    print("Nothing will seem to type, but you are putting in your password anyway")
    password = getpass("ENTER PASSWORD - ")

print("Loading browser (phantomJS)...")
#driver = webdriver.Firefox()
driver = webdriver.PhantomJS(phantomjs_exe)

print("Loading msftconnecttest.com...")
xpath = driver.find_element_by_xpath

print("Logging in...")
try:
    driver.get("[redacted]")
    print("Logging in...")
    xpath('//*[@id="cmd_acceptAup"]').click()
    xpath('//*[@id="username"]').send_keys(username)
    xpath('//*[@id="password"]').send_keys(password)
    xpath('//*[@id="password"]').send_keys(Keys.RETURN)
except Exception as e:
    print(e["errormessage"])
    print("\n\n")
    print("There was an error (displayed above).")
    print("Maybe you are not connected, or are already logged in?")
    input()
    
time.sleep(5)