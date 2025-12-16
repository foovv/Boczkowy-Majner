import pyautogui
import time
import walk
import keyboard

running = False

def start():
    global running
    if running:
        return
    running = True
    print("start za 2s")
    time.sleep(2)
    pyautogui.mouseDown(button='left')
    
    while running:
        walk.walking(b)

    pyautogui.mouseUp(button='left')

def stop():
    global running
    running = False


def main():
    print("start za 2s")
    time.sleep(2)
    walk.walking()
    print('koniec')

b = int(input("Podaj liczbe stowniarek: "))


keyboard.add_hotkey("f8", start)   # START
keyboard.add_hotkey("f9", stop)

keyboard.wait()