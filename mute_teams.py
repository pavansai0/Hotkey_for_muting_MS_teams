import pyautogui
import time
import subprocess

subprocess.Popen(['C:\Windows\System32\SndVol.exe'])

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
