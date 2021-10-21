# Modified Pulse login script

from pywinauto.application import Application
from pywinauto import application

import pywinauto.mouse as mouse
import pywinauto.keyboard as keyboard
import win32gui, win32con, win32api
import time

app = Application(backend="uia").connect(title_re="Pulse Secure")
dlg = app.window(title_re=".*Pulse.*")
dlg.Button43.click() #Button 43 comming from the control ident printout
time.sleep(3)
for x in range(7):
 keyboard.send_keys('t')
mouse.click(coords=(1053, 752))
time.sleep(3)
keyboard.send_keys('*usrname*{TAB}*password*{ENTER}')
OTP = input("Please enter OTP:\n")
mouse.click(coords=(962, 866))
keyboard.send_keys(OTP)
keyboard.send_keys('{TAB}{ENTER}')
OTP = input("HIT ENTER when logged in:\n")
dlg.Button39.click()
OTP = input("Hit when ready to enter 2nd Password\n")

mouse.click(coords=(831, 707))
time.sleep(2)
keyboard.send_keys('*username*{TAB}*password*/{ENTER}')
