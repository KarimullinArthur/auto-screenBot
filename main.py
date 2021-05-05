import pyautogui
import time
import os

def main(): 
    z = '0'
    name = "0.png"
    path = "./1/"
    os.mkdir(path)

    for x in range(0,50):
        pyautogui.screenshot(path+name)
        time.sleep(0.5)
        pyautogui.hotkey('pagedown')

def start():
    print("5..")
    time.sleep(1)
    
    print("4..")
    time.sleep(1)
    
    print("3..")
    time.sleep(1)
    
    print("2..")
    time.sleep(1)
    
    print("1..")
    time.sleep(1)

    print("Screen!")

start()
main()






