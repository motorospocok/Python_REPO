import tkinter as tk

def LocRem():
    print('yeah')

def increment_display1():
    value = int(display1.get()) if display1.get().isdigit() else 0

    if 0 <= value < 60:
        display1.delete(0, tk.END)
        display1.insert(0, str(value + 1))

def increment_display2():
    value = int(display2.get()) if display2.get().isdigit() else 0

    if 0 <= value < 60:
        display2.delete(0, tk.END)
        display2.insert(0, str(value + 1))

def increment_display3():
    value = int(display3.get()) if display3.get().isdigit() else 0

    if 0 <= value < 60:
        display3.delete(0, tk.END)
        display3.insert(0, str(value + 1))
        
def increment_display4():
    value = int(display4.get()) if display4.get().isdigit() else 0

    if 0 <= value < 60:
        display4.delete(0, tk.END)
        display4.insert(0, str(value + 1))
        
def increment_display5():
    value = int(display5.get()) if display5.get().isdigit() else 0

    if 0 <= value < 60:
        display5.delete(0, tk.END)
        display5.insert(0, str(value + 1))

def increment_display6():
    value = int(display6.get()) if display6.get().isdigit() else 0

    if 0 <= value < 60:
        display6.delete(0, tk.END)
        display6.insert(0, str(value + 1))

def increment_display7():
    value = int(display7.get()) if display7.get().isdigit() else 0

    if 0 <= value < 60:
        display7.delete(0, tk.END)
        display7.insert(0, str(value + 1))

def increment_display8():
    value = int(display8.get()) if display8.get().isdigit() else 0

    if 0 <= value < 60:
        display8.delete(0, tk.END)
        display8.insert(0, str(value + 1))

def decrement_display1():
    value = int(display1.get()) if display1.get().isdigit() else 0

    if 0 < value <= 60:
        display1.delete(0, tk.END)
        display1.insert(0, str(value - 1))

def decrement_display2():
    value = int(display2.get()) if display2.get().isdigit() else 0

    if 0 < value <= 60:
        display2.delete(0, tk.END)
        display2.insert(0, str(value - 1))

def decrement_display3():
    value = int(display3.get()) if display3.get().isdigit() else 0

    if 0 < value <= 60:
        display3.delete(0, tk.END)
        display3.insert(0, str(value - 1))

def decrement_display4():
    value = int(display4.get()) if display4.get().isdigit() else 0

    if 0 < value <= 60:
        display4.delete(0, tk.END)
        display4.insert(0, str(value - 1))

def decrement_display5():
    value = int(display5.get()) if display5.get().isdigit() else 0

    if 0 < value <= 60:
        display5.delete(0, tk.END)
        display5.insert(0, str(value - 1))
        
def decrement_display6():
    value = int(display6.get()) if display6.get().isdigit() else 0

    if 0 < value <= 60:
        display6.delete(0, tk.END)
        display6.insert(0, str(value - 1))
        
def decrement_display7():
    value = int(display7.get()) if display7.get().isdigit() else 0

    if 0 < value <= 60:
        display7.delete(0, tk.END)
        display7.insert(0, str(value - 1))

def decrement_display8():
    value = int(display8.get()) if display8.get().isdigit() else 0

    if 0 < value <= 60:
        display8.delete(0, tk.END)
        display8.insert(0, str(value - 1))


def on_radio_button_selected():
    print(f"Connector selected: {connector_selection.get()}")
    selected_value = connector_selection.get()
    button_color_change(selected_value)


def button_color_change(code):
    if code == 1:
        hex_color = "#00FF00"
    if code == 2:
        hex_color = "#3399ff"
    if code == 3:
        hex_color = "#00ffff"
    if code == 4:
        hex_color = "#ffffff"

    button_up1.config(bg=hex_color)
    button_up2.config(bg=hex_color)
    button_up3.config(bg=hex_color)
    button_up4.config(bg=hex_color)
    button_up5.config(bg=hex_color)
    button_up6.config(bg=hex_color)
    button_up7.config(bg=hex_color)
    button_up8.config(bg=hex_color)
    button_down1.config(bg=hex_color)
    button_down2.config(bg=hex_color)
    button_down3.config(bg=hex_color)
    button_down4.config(bg=hex_color)
    button_down5.config(bg=hex_color)
    button_down6.config(bg=hex_color)
    button_down7.config(bg=hex_color)
    button_down8.config(bg=hex_color)

def toggle_checkbox():
    # Print the state of the checkbox
    value = checkbox1_var.get() + (checkbox2_var.get() * 2) + (checkbox3_var.get() * 4) + (checkbox4_var.get() * 8) + (checkbox5_var.get() * 16) + (checkbox6_var.get() * 32) + (checkbox7_var.get() * 64) + (checkbox8_var.get() * 128)

    if checkbox1_var.get():
        print("Checkbox is checked")
    else:
        print("Checkbox is unchecked")
    print(value)

root = tk.Tk()
root.title("Tkinter Example")

connector_selection = tk.IntVar()
button_size = 4
padding = 10
checkbox1_var = tk.BooleanVar()
checkbox2_var = tk.BooleanVar()
checkbox3_var = tk.BooleanVar()
checkbox4_var = tk.BooleanVar()
checkbox5_var = tk.BooleanVar()
checkbox6_var = tk.BooleanVar()
checkbox7_var = tk.BooleanVar()
checkbox8_var = tk.BooleanVar()

# GUI definitions starts here

lcd_font = ("Courier", 20, "bold")  # LCD-szerű betűtípus beállítása
lcd_font2 = ("Courier", 10, "bold")  # LCD-szerű betűtípus beállítása

info1 = tk.Entry(root, width=8, font=lcd_font2, justify='center', bg='pink', fg='black')
info1.grid(row=0, column=2, padx=padding, pady=padding)

info2 = tk.Entry(root, width=8, font=lcd_font2, justify='center', bg='pink', fg='black')
info2.grid(row=1, column=3, padx=padding, pady=padding)

info3 = tk.Entry(root, width=8, font=lcd_font2, justify='center', bg='pink', fg='black')
info3.grid(row=0, column=4, padx=padding, pady=padding)

info4 = tk.Entry(root, width=8, font=lcd_font2, justify='center', bg='pink', fg='black')
info4.grid(row=1, column=5, padx=padding, pady=padding)

info5 = tk.Entry(root, width=8, font=lcd_font2, justify='center', bg='pink', fg='black')
info5.grid(row=0, column=6, padx=padding, pady=padding)

info6 = tk.Entry(root, width=8, font=lcd_font2, justify='center', bg='pink', fg='black')
info6.grid(row=1, column=7, padx=padding, pady=padding)

info7 = tk.Entry(root, width=8, font=lcd_font2, justify='center', bg='pink', fg='black')
info7.grid(row=0, column=8, padx=padding, pady=padding)

info8 = tk.Entry(root, width=8, font=lcd_font2, justify='center', bg='pink', fg='black')
info8.grid(row=1, column=9, padx=padding, pady=padding)

display1 = tk.Entry(root, width=3, font=lcd_font, justify='center', bg='black', fg='light green')
display1.grid(row=2, column=2, padx=padding, pady=padding)

display2 = tk.Entry(root, width=3, font=lcd_font, justify='center', bg='black', fg='light green')
display2.grid(row=2, column=3, padx=padding, pady=padding)

display3 = tk.Entry(root, width=3, font=lcd_font, justify='center', bg='black', fg='light green')
display3.grid(row=2, column=4, padx=padding, pady=padding)

display4 = tk.Entry(root, width=3, font=lcd_font, justify='center', bg='black', fg='light green')
display4.grid(row=2, column=5, padx=padding, pady=padding)

display5 = tk.Entry(root, width=3, font=lcd_font, justify='center', bg='black', fg='light green')
display5.grid(row=2, column=6, padx=padding, pady=padding)

display6 = tk.Entry(root, width=3, font=lcd_font, justify='center', bg='black', fg='light green')
display6.grid(row=2, column=7, padx=padding, pady=padding)

display7 = tk.Entry(root, width=3, font=lcd_font, justify='center', bg='black', fg='light green')
display7.grid(row=2, column=8, padx=padding, pady=padding)

display8 = tk.Entry(root, width=3, font=lcd_font, justify='center', bg='black', fg='light green')
display8.grid(row=2, column=9, padx=padding, pady=padding)

button_up1 = tk.Button(root, text="Up1", command=increment_display1, width=4, height=2)
button_up1.grid(row=3, column=2, padx=padding, pady=padding)

button_up2 = tk.Button(root, text="Up2", command=increment_display2, width=4, height=2)
button_up2.grid(row=3, column=3, padx=padding, pady=padding)

button_up3 = tk.Button(root, text="Up3", command=increment_display3, width=4, height=2)
button_up3.grid(row=3, column=4, padx=padding, pady=padding)

button_up4 = tk.Button(root, text="Up4", command=increment_display4, width=4, height=2)
button_up4.grid(row=3, column=5, padx=padding, pady=padding)

button_up5 = tk.Button(root, text="Up5", command=increment_display5, width=4, height=2)
button_up5.grid(row=3, column=6, padx=padding, pady=padding)

button_up6 = tk.Button(root, text="Up6", command=increment_display6, width=4, height=2)
button_up6.grid(row=3, column=7, padx=padding, pady=padding)

button_up7 = tk.Button(root, text="Up7", command=increment_display7, width=4, height=2)
button_up7.grid(row=3, column=8, padx=padding, pady=padding)

button_up8 = tk.Button(root, text="Up8", command=increment_display8, width=4, height=2)
button_up8.grid(row=3, column=9, padx=padding, pady=padding)

button_down1 = tk.Button(root, text="Dn1", command=decrement_display1, width=4, height=2)
button_down1.grid(row=4, column=2, padx=padding, pady=padding)

button_down2 = tk.Button(root, text="Dn2", command=decrement_display2, width=4, height=2)
button_down2.grid(row=4, column=3, padx=padding, pady=padding)

button_down3 = tk.Button(root, text="Dn3", command=decrement_display3, width=4, height=2)
button_down3.grid(row=4, column=4, padx=padding, pady=padding)

button_down4 = tk.Button(root, text="Dn4", command=decrement_display4, width=4, height=2)
button_down4.grid(row=4, column=5, padx=padding, pady=padding)

button_down5 = tk.Button(root, text="Dn5", command=decrement_display5, width=4, height=2)
button_down5.grid(row=4, column=6, padx=padding, pady=padding)

button_down6 = tk.Button(root, text="Dn6", command=decrement_display6, width=4, height=2)
button_down6.grid(row=4, column=7, padx=padding, pady=padding)

button_down7 = tk.Button(root, text="Dn7", command=decrement_display7, width=4, height=2)
button_down7.grid(row=4, column=8, padx=padding, pady=padding)

button_down8 = tk.Button(root, text="Dn8", command=decrement_display8, width=4, height=2)
button_down8.grid(row=4, column=9, padx=padding, pady=padding)

radio_button1 = tk.Radiobutton(root, text="Connector 1", variable=connector_selection, value=1, command=on_radio_button_selected,bg="#00FF00")
radio_button2 = tk.Radiobutton(root, text="Connector 2", variable=connector_selection, value=2, command=on_radio_button_selected,bg="#3399ff")
radio_button3 = tk.Radiobutton(root, text="Connector 3", variable=connector_selection, value=3, command=on_radio_button_selected,bg='#00ffff')
radio_button4 = tk.Radiobutton(root, text="Connector 4", variable=connector_selection, value=4, command=on_radio_button_selected,bg='#ffffff')

radio_button1.grid(row=0, column=0,padx=padding, pady=padding)
radio_button2.grid(row=1, column=0,padx=padding, pady=padding)
radio_button3.grid(row=2, column=0,padx=padding, pady=padding)
radio_button4.grid(row=3, column=0,padx=padding, pady=padding)

button_mode = tk.Button(root, text="Local-Remote", command=LocRem, width=15, height=3,bg='#666699')
button_mode.grid(row=8, column=0, padx=10, pady=0)

status_display = tk.Entry(root, width=20, font=lcd_font2, justify='center', bg='white', fg='black')
status_display.grid(row=8, column=1, padx=0, pady=0)
status_display.insert(0,"<-Press to connect")

ip_label = tk.Label(root, text="Matrix IP address:",bg="white")
ip_label.grid(row=10, column=0, pady=10)
ip_entry = tk.Entry(root, width=15, font=lcd_font2, justify='center', bg='white', fg='black')
ip_entry.grid(row=10, column=1, padx=padding, pady=padding)
ip_entry.insert(0,"192.168.1.1")

checkbox1 = tk.Checkbutton(root, text="Add M1", variable=checkbox1_var, command=toggle_checkbox)
checkbox1.grid(row=5, column=2, padx=padding, pady=padding)

checkbox2 = tk.Checkbutton(root, text="Add M2", variable=checkbox2_var, command=toggle_checkbox)
checkbox2.grid(row=5, column=3, padx=padding, pady=padding)

checkbox3 = tk.Checkbutton(root, text="Add M3", variable=checkbox3_var, command=toggle_checkbox)
checkbox3.grid(row=5, column=4, padx=padding, pady=padding)

checkbox4 = tk.Checkbutton(root, text="Add M4", variable=checkbox4_var, command=toggle_checkbox)
checkbox4.grid(row=5, column=5, padx=padding, pady=padding)

checkbox5 = tk.Checkbutton(root, text="Add M5", variable=checkbox5_var, command=toggle_checkbox)
checkbox5.grid(row=5, column=6, padx=padding, pady=padding)

checkbox6 = tk.Checkbutton(root, text="Add M6", variable=checkbox6_var, command=toggle_checkbox)
checkbox6.grid(row=5, column=7, padx=padding, pady=padding)

checkbox7 = tk.Checkbutton(root, text="Add M7", variable=checkbox7_var, command=toggle_checkbox)
checkbox7.grid(row=5, column=8, padx=padding, pady=padding)

checkbox8 = tk.Checkbutton(root, text="Add M8", variable=checkbox8_var, command=toggle_checkbox)
checkbox8.grid(row=5, column=9, padx=padding, pady=padding)

root.mainloop()