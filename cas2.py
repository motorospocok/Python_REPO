#This short PyAuto script is written for the atomate the logon
#Needs to give the button coordinates correctly, also need to run with administrative rights

import pyautogui
import time

password = "<put_your_LAN_psw>"
password2 = "<put_your_CAS_psw>"

tvar = input("Please move the Ivanti window on the laptop display upper right corner ")



def enter_characers(text_to_write):
 text_to_write_array = []
 text_to_write_array = [char for char in text_to_write]
 for char in text_to_write_array:  
  pyautogui.press(char)


pyautogui.click(button="left",x=1846, y=262) #coordinates of the first Reca2B EXT button
time.sleep(3)
pyautogui.click(button="left",x=1217, y=871)  #coordinates of the Proceed button
pyautogui.press('t')
time.sleep(1)

for _ in range(5):
 pyautogui.press('down')

time.sleep(1)

pyautogui.click(button="left",x=1047, y=963) #coordinates of the Proceed button

time.sleep(1)

enter_characers(password)
time.sleep(1)

pyautogui.press('enter')

otp = input("Please input your OTP auth psw and press enter when the Ivanti windows is ready for it: ")
pyautogui.click(button="left",x=1003, y=918)

enter_characers(otp)
pyautogui.press('enter')

tvar = input("Please wait until the first VPN connection ESTABLIHES, when finished press ENTER ")
pyautogui.click(button="left",x=1831, y=161) #coordinates of Magyar Telekom CAS
time.sleep(3)
#pyautogui.click(button="left",x=966, y=238) #coordinates of PSW  filed

time.sleep(2)

enter_characers(password2)
 
pyautogui.press('enter')
