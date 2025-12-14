import pyautogui
import time
import pygetwindow as gw
import main

# 2s = 9 blocks
# 0.2s = 1 block
b = main.liczba_stowaniarek

# height and width on active window
win = gw.getActiveWindow()

print(win.width)
print(win.height)


def walk(x, key):
    x = x * .23

    pyautogui.keyDown(key)
    time.sleep(x)
    pyautogui.keyUp(key)

    
def walkAlong():
    walk(b, 'w')

def walkRight():
    walk(.4, 'd')
    
def walkBackward():
    walk(b, 's')

def walkLeft():
    walk(.4, 'a')
    
def walking():
    walkAlong()
    walkRight()
    walkBackward()
    walkLeft()