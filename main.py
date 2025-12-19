import threading
import time
import pyautogui
import walk
import gui
import universal

running = False

def start(b, x):
    global running
    if running:
        return
    running = True

    def loop():
        time.sleep(2)
        
        

        while running:
            pyautogui.mouseDown(button='left')
            walk.walking(b)
            pyautogui.mouseUp(button='left')
            universal.command(x)
            
       

    threading.Thread(target=loop, daemon=True).start()

def stop():
    global running
    running = False


if __name__ == "__main__":
    gui.run(start, stop)