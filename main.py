import pyautogui
import time
import walk
import keyboard

liczba_stowaniarek = (int(input('Podaj liczbe stowniarek: ')))

print("start za 2s")
time.sleep(2)

def main():
    walk.walking()
 
pyautogui.press('f8')

def on_press():
    main()

keyboard.add_hotkey("f8", on_press)
keyboard.add_hotkey("f9", )



if __name__ == '__main__':
    main()




print('koniec')