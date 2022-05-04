#This short python program is written for lazy dogs
#Sets the HPQC status window to the status -given by the user

import pyautogui as py #Import pyautogui
import time #Import Time

piece = input("Enter number of test cases ")
piece = int(piece)
piece = piece - 1
choice = input("Enter what you want to set Passed,Blocked,Parked ")
username = input("Position the mouse to the first Status to be set and press ENTER")
currentMouseX,currentMouseY = py.position()


for i in range(0,piece):
    y2 = i * 28 #number 28 seems ideal now y coords increase
    y2 = currentMouseY + y2
    py.click(currentMouseX, y2)
    time.sleep(0.1)
    py.press('delete')
    time.sleep(0.1)
    py.write(choice)
    time.sleep(0.1)
    py.press('enter')

    
    



