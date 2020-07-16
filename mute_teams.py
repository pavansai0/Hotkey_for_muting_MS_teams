import pyautogui
import time
pyautogui.press('win') 
pyautogui.moveTo(204,1059)
pyautogui.click()
time.sleep(0.05)
x=0
s = pyautogui.locateOnScreen('mt.png')

while(x==0):
    if(s):
        pyautogui.moveTo(s.left,550)
        pyautogui.click()
        x=1
    else:
        pyautogui.moveTo(521,590)
        pyautogui.click()
        x=1

pyautogui.moveTo(526,187)
pyautogui.click()
