import pyautogui
from time import sleep
sleep(5)
for i in range(0,4):
    pyautogui.write('Hello',interval = 0.25)
    pyautogui.press('enter')

