import pyautogui
import time
import os



time.sleep(5)

def main(): 
    z = '0'
    name = "0.png"
    path = "./1/"
    os.mkdir(path)
    for y in range(1,5):

        for x in range(0,50):
            pyautogui.screenshot(path+name)
            time.sleep(0.5)
            pyautogui.hotkey('pagedown')

main()






