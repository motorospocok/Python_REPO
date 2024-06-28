#Auto login for CAS V1.0
#Progress bar does not work well, but it seems

import tkinter as tk
from tkinter import ttk
import threading
import pyautogui
import time

password = "A1mafeJ$7"
password2 = "Almafej323!Ad"
x_coord = [1846,1217,1047,1003,1831]
y_coord = [262,871,963,918,161]
phase = -1
progress_value = 0

def enter_characers(text_to_write):
    text_to_write_array = []
    text_to_write_array = [char for char in text_to_write]
    for char in text_to_write_array:  
        pyautogui.press(char)

def click_on_coord(step):
    x1 = x_coord[step]
    y1 = y_coord[step]
    pyautogui.click(button="left",x=x1,y=y1)


# Function to update the progress bar
def start_progress(increase=True):
    global phase
    try:
        
        current_value = progress_bar['value']

        if increase:
            target_value = min(100, current_value + progress_value)  # Ensure value doesn't exceed 100
            phase += 1
            print('Here left click')
            print(phase)
            if phase == 0:
                label.config(text='''Logging into 1st CAS''')
                time.sleep(1)
                click_on_coord(0)
                time.sleep(3)
                click_on_coord(1)
                time.sleep(1)
                pyautogui.press('t')
                time.sleep(1)
                for _ in range(5):
                    pyautogui.press('down')
                time.sleep(1)
                click_on_coord(2)
                time.sleep(1)
                enter_characers(password)
                time.sleep(1)
                pyautogui.press('enter')
                label2.config(text='''Please input your OTP auth psw and press the Button when the Ivanti asks for it''')
                label.config(text='''Waiting for OTP...''')
                progress_bar['value'] = 35
            if phase == 1:
                label.config(text='''Establishing first VPN...''')
                otp = entry.get()
                time.sleep(1)
                click_on_coord(3)
                enter_characers(otp)
                pyautogui.press('enter')
                label2.config(text='''Please wait until the first VPN connection is ESTABLISHED, when finished press Button''')
                progress_bar['value'] = 70
                
            if phase == 2:
                label.config(text='''Building up second VPN...''')
                time.sleep(1)
                click_on_coord(4)
                time.sleep(5)   
                enter_characers(password2)
                pyautogui.press('enter')
                label2.configure(text='''Now you should be connected to the CAS, next button press closes this appilcation''', fg="white", bg="green")
                label.config(text='''program end''')
                progress_bar['value'] = 100
                
            if phase == 3:
                global top_level
                root.destroy()

        else:
            target_value = max(0, current_value - 10)  # Ensure value doesn't go below 0
            print('here')
            
            phase -= 1
            print(phase)
            if phase == 1:
                label.config(text='''Reverted back to 2nd VPN establishment''')
                label2.config(text='''Press button again to attempt the 2nd VPN again''')
            if phase == -1:
                label.config(text='''Reverted back to 1st VPN establishment''')
                label2.config(text='''Press button again to attempt the 1st VPN again''')
                             

        while current_value != target_value:
            if increase:
                current_value += 30
            else:
                current_value -= 1
            progress_bar['value'] = current_value
            #label.config(text=f"Progress: {current_value}%")
            root.update_idletasks()
            time.sleep(0.10)

    except ValueError:
        label.config(text="Please enter a valid number")

# Function to start progress in a separate thread
def start_progress_thread(increase=True):
    threading.Thread(target=start_progress, args=(increase,)).start()

# Create the main window
root = tk.Tk()
root.title("CAS LoginAuto")

# Create and place the entry field
entry = tk.Entry(root)
entry.pack(pady=10)

# Create and place the button
button = tk.Button(root, text="Mr Button")
button.pack(pady=10)

# Bind left-click and right-click events to the button
button.bind('<Button-1>', lambda e: start_progress_thread(increase=True))
button.bind('<Button-3>', lambda e: start_progress_thread(increase=False))

# Create and place the progress bar
progress_bar = ttk.Progressbar(root, orient='horizontal', length=300, mode='determinate')
progress_bar.pack(pady=10)

# Create and place the label
label = tk.Label(root, text="Click on Start")
label.pack(pady=10)

# Create and place the combo box
combo_values = ["Telekom", "Italy"]
combo = ttk.Combobox(root, values=combo_values)
combo.set("Select an option")  # Set the default value
combo.pack(pady=10)

label2 = tk.Label(root, text="Change keyboard to ENG and click on left button to start", fg="white", bg="black")
label2.pack(pady=10)
# Start the Tkinter event loop
root.mainloop()
