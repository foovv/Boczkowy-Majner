import pyautogui
import time

def command(commands):
    filtered = [x for x in commands if x.strip()]

    for command in filtered:
        pyautogui.press('t')
        time.sleep(0.1) 

        pyautogui.write(command)
        time.sleep(0.05) 
        pyautogui.press('enter')
        time.sleep(0.25)

    
