
import pyautogui
import time


# 2s = 9 blocks
# 0.2s = 1 block
b = 0


def walk(x, key):
    x = x * .23

    pyautogui.keyDown(key)
    time.sleep(x)
    pyautogui.keyUp(key)

    

def walking(b):
    walk(b, 'd')
    walk(1, 's')
    walk(b, 'a')
    walk(1, 'w')