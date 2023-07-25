import pyautogui

from time import sleep
sleep(5)

def draw_pyramid(rows):
    for i in range(rows):
        pyramid_row = '#' * (i + 1)
        pyautogui.typewrite(pyramid_row, interval = 0.5)
        pyautogui.press('enter')

n = int(input())
draw_pyramid(n)