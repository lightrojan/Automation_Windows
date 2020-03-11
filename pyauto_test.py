# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 17:31:09 2019

@author: tiongzhongcheng

Windows Testing
6.5.1 Stress Test 2.4G/5G Connection

200 runs = 2.4G 100 times, 5G 100 times
"""

import pyautogui
from time import sleep
import os
import time
from urllib.request import urlopen

def internet_on(): #check for internet connectivity
    try:
        response = urlopen('https://www.google.com/', timeout=10)
        return True
    except: 
        return False
    
path = os.getcwd() #get current working directory
screenshot_path = str(path+'/Screenshots'+'/'+str(time.strftime('%Y%m%d-%H%M%S')))
                                              
try:
    os.makedirs(screenshot_path) #create folder for screenshots
    print('Directory created')
except FileExistsError:
    print('Directory already exists')
    
pyautogui.FAILSAFE = True #false disables the fail-safe
count = 1
true_count = 0
false_count = 0

pyautogui.moveTo(3213, 2119)
pyautogui.click()
sleep(1)
pyautogui.click(3515,422)
sleep(1)
pyautogui.click(3552,691)
sleep(10)

assert internet_on() == True, 'Not connected' #Error checking

for i in range(1,201):
    print('=======Running Test Number '+str(i)+'=======')
    sleep(1)
    pyautogui.click(3559,861)
    sleep(1)
    pyautogui.click(3559,861)
    sleep(10)
    print(internet_on())
    if internet_on() == True:
        true_count +=1
    else:
        false_count +=1
        im1 = pyautogui.screenshot(screenshot_path+'/No Connection_'+str(time.strftime('%Y%m%d-%H%M%S')+'.png'))
        pyautogui.click(3559,861) #to reset the connection
    sleep(1)
    i += 1
    print('True Count:' + str(true_count))
    print('False Count:' + str(false_count))

    


