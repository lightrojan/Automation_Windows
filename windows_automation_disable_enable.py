# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 17:00:33 2020

@author: zhong

Disable/Enable Test for 2.4G/5G
"""

import os 
import ctypes, sys
from time import sleep
import time
from urllib.request import urlopen

true_count = 0
false_count = 0

def internet_on(): #check for internet connectivity
    try:
        response = urlopen('https://www.google.com/', timeout=10)
        return True
    except: 
        return False

def enable():
    os.system('netsh interface set interface "Wi-Fi" enabled')

def disable():
    os.system('netsh interface set interface "Wi-Fi" disabled')
    
def status():
    os.system('netsh interface show interface | findstr /C:”Wi-Fi” /C:”Name”')
    
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    assert internet_on() == True, 'Not connected' #Error checking
    
    for i in range(0,10):
        print("Disabling card...")
        disable()
        status()
        sleep(5)
        if internet_on() == False:
            print("Enabling card...")
            enable()
            status()
            sleep(5)
            if internet_on() == True:
                true_count +=1
            else:
                false_count +=1
        i += 1
        print('True Count:' + str(true_count))
        print('False Count:' + str(false_count))
        sleep(5)

else:
    # Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
    exit()
