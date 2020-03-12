import os
from time import sleep
import ctypes, sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    os.system('powercfg.exe /h off')
    sleep(2)
    os.system('rundll32.exe powrprof.dll,SetSuspendState sleep')
