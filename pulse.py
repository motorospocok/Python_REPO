# This program doing semi-automatic login into the Telekom CAS
# V1.0


from pywinauto.application import Application
from pywinauto import application
import pywinauto.mouse as mouse
import pywinauto.keyboard as keyboard
import win32gui, win32con, win32api
import time

app = Application(backend="uia").start('C:\Program Files (x86)\Common Files\Pulse Secure\JamUI\Pulse.exe -show')
dlg = app.window(title_re=".*Pulse.*")

hwnd = win32gui.FindWindow(None, "Pulse Secure")
win32gui.MoveWindow(hwnd, 0, 0, 415, 813, True)
mouse.click(coords=(353, 535))
time.sleep(5)
dlg2 = application.findwindows.find_elements(title_re=".*reca.*")

for x in range(9):
 keyboard.send_keys('t')
mouse.click(coords=(1053, 752))
time.sleep(1)
keyboard.send_keys('ethtoja{TAB}Speter35{ENTER}')
OTP = input("Please enter OTP:\n")
mouse.click(coords=(962, 866))
keyboard.send_keys(OTP)
keyboard.send_keys('{ENTER}')
OTP = input("HIT ENTER when logged in:\n")
mouse.click(coords=(330, 632))
time.sleep(5)
keyboard.send_keys('{ENTER}')
time.sleep(0.5)
keyboard.send_keys('ethtoja{TAB}Er1css0n21!/{ENTER}')







          
