from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import subprocess

def copy2clip(txt):
    cmd='echo '+txt.strip()+'|clip'
    return subprocess.check_call(cmd, shell=True)

def nextPermutation( arr):
        bPoint, n = -1, len(arr)
        for i in range(n-2,-1,-1):
            if arr[i] >= arr[i+1]: continue                   # Skip the non-increasing sequence
            bPoint = i                                        # Got our breakpoint
            for j in range(n-1,i,-1):                         # again traverse from end
                if arr[j] > arr[bPoint]:                      # Search an element greater the element present at the breakPoint.
                    arr[j], arr[bPoint] = arr[bPoint], arr[j] # Swap it
                    break                                     # We just need to swap once
            break                                             # Break this loop too
        arr[bPoint+1:] = reversed(arr[bPoint+1:])
        return arr


seed_words_test = {1:'abandon',
2:'ability',
3:'ask',
4:'asdfasdfasdf',
5:'above',
6:'absent',
7:'absorb',
8:'abstract',
9:'absurd',
10:'abuse',
11:'access',
12:'accident'}


EXTENSION_PATH = "" #enter the path to the metamask .crx file here

opt = webdriver.ChromeOptions()
opt.add_extension(EXTENSION_PATH)
driver = webdriver.Chrome(chrome_options=opt)
time.sleep(1)

#switch tabs
driver.switch_to.window(driver.window_handles[0])


#CLICK THROUGH BUTTONS:
#btn1
time.sleep(1)
elem = driver.find_element(by = By.XPATH, value = '/html/body/div[1]/div/div[2]/div/div/div/button').click()
#btn2
time.sleep(1)
elem = driver.find_element(by = By.XPATH, value = '/html/body/div[1]/div/div[2]/div/div/div[2]/div/div[2]/div[1]/button').click()
#btn3
time.sleep(1)
elem = driver.find_element(by = By.XPATH, value = '/html/body/div[1]/div/div[2]/div/div/div/div[5]/div[1]/footer/button[2]').click()


#CREATE KEYWORD STRING
count = 0
s = ''
for e in seed_words_test:
    s += " " + seed_words_test[e]
s.strip()

#COPY STRING TO CLIPBOARD:
copy2clip(s)

#CLICK ON TEXTFIELD
time.sleep(1)
elem = driver.find_element(by = By.XPATH, value= '/html/body/div[1]/div/div[2]/div/div/div[2]/form/div[1]/div[2]/div[1]/div[1]/div/input')

#PASTE CLIPBOARD TO TEXTFIELD
elem.send_keys(Keys.CONTROL + 'v')
time.sleep(2)

arr = [1,2,3,4,5,6,7,8,9,10,11,12]

looper = True

while looper:
    try:
        elem = driver.find_element(by = By.XPATH, value= '/html/body/div[1]/div/div[2]/div/div/div[2]/form/div[1]/div[3]')
        count += 1
        s = ''
        arr = nextPermutation(arr)

        for e in arr:
            s += " " + seed_words_test[e]
        s.strip()

        #COPY STRING TO CLIPBOARD:
        copy2clip(s)
        #click on textfield
        elem = driver.find_element(by = By.XPATH, value= '/html/body/div[1]/div/div[2]/div/div/div[2]/form/div[1]/div[2]/div[1]/div[1]/div/input')
        #PASTE CLIPBOARD TO TEXTFIELD
        elem.send_keys(Keys.CONTROL + 'v')

        print(s)
        print(count)

    except:
        looper = False
        print("DONE!!!" , s)
