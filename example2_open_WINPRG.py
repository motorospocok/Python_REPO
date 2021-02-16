# This program opesn TotalCommander and select Fájl -> Becsomagolás
# Uses hungarian totalcmd language setup
# Run Tested in IDLE shell P 3.9.1

from pywinauto.application import Application
import pywinauto.mouse as mouse
import pywinauto.keyboard as keyboard

app = Application().connect(path=r"C:\totalcmd\TOTALCMD64.EXE")
dlg = app.window(title_re=".*Commander.*")
dlg.menu_select("Fájl -> Becsomagolás")
dlg.set_focus()
mouse.click(coords=(445, 585))
