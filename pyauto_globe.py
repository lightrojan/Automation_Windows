import pyautogui

globe = pyautogui.locateOnScreen('C://Users//tiongzhongcheng//github//Automation_Windows//globe.png')
pyautogui.click(globe,grayscale=True)
print(globe)
