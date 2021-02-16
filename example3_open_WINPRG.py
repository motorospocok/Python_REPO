# This program opens Two applications
# Notepad opens, TotalCMD already running

from pywinauto.application import Application
import pywinauto.mouse as mouse
import pywinauto.keyboard as keyboard

app2 = Application().start(r"C:\Program Files (x86)\Notepad++\notepad++.exe")
app = Application().connect(path=r"C:\totalcmd\TOTALCMD64.EXE")

# Brings Notepad++ foreground and File new
dlg2 = app2.window(title_re=".*Notepad.*")
dlg2.menu_select("File -> New	Ctrl+N")

# Brings TotalCmd foreground
dlg = app.window(title_re=".*Commander.*")
dlg.menu_select("Fájl -> Becsomagolás")
dlg.set_focus()
mouse.click(coords=(445, 585))

# Brings Notepad++ foreground again
dlg2 = app2.window(title_re=".*Notepad.*")
dlg2.menu_select("Window -> Windows...")

