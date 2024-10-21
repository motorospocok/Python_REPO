# Bonn BUAW20 attenuator matrix Controller by ethtoja
# V 1.0 - 21th October 2024 - working very basic functions - can step the matrix remotely :)


import tkinter as tk
import socket

global connect_flag

def update_display(matrix_data):
    
    for x in range(0, 8):
        displays[x].delete(0, tk.END)
        displays[x].insert(0, str(matrix_data[x]))

def update_matrix():
    message = "*ASK\r\n"
    response = send_tcp_packet(message)
    print(response)
    response = response.replace('!ASK:', '')
    current_setup = response.split(',')

    global m0
    global m1
    global m2
    global m3
    global mode_flag
    mode_flag = current_setup[1]
    
    m0 = [current_setup[9], current_setup[15], current_setup[21], current_setup[27], current_setup[33],
          current_setup[39], current_setup[45], current_setup[51]]

    m1 = [current_setup[10], current_setup[16], current_setup[22], current_setup[28], current_setup[34],
          current_setup[40], current_setup[46], current_setup[52]]

    m2 = [current_setup[11], current_setup[17], current_setup[23], current_setup[29], current_setup[35],
          current_setup[41], current_setup[47], current_setup[53]]

    m3 = [current_setup[12], current_setup[18], current_setup[24], current_setup[30], current_setup[36],
          current_setup[42], current_setup[48], current_setup[54]]

    conn = connector_selection.get()
    if conn == 0:
        update_display(m0)
    if conn == 1:
        update_display(m1)
    if conn == 2:
        update_display(m2)
    if conn == 3:
        update_display(m3)

def send_tcp_packet(data):
    # ip = "192.168.16.210"
    ip = ip_entry.get()
    port = 23
    timeout=2
    print(data)
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        sock.settimeout(timeout)
        # Connect the socket to the server
        sock.connect((ip, port))

        # Send data
        sock.sendall(data.encode('utf-8'))

        # Receive response (optional)
        response = sock.recv(1024)
        response_decoded = response.decode('utf-8')
        print(f"Received response: {response.decode('utf-8')}")
        return response_decoded

    except socket.timeout:
        print("Socket timeout occurred")
        status_display.delete(0, tk.END)
        status_display.insert(0, "SOCKET ERROR")
        response= "!ASK:00,0,3,0,5.07,3.26,0.19,+35.6,08,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,47,37,27,60,60,56,46,36,26,60,60,55,45,35,25,60,60,54,44,34,24,60,60,53,43,33,23,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60"
    except socket.error as e:
        print(f"Socket error: {e}")

    finally:
        # Close the sock
        sock.close()

def matrix_step(connector,selected_matrix,value1):
    data = '*SAT:' + connector + ',' + selected_matrix + ',' + str(value1) + '\r\n'
    print(data)
    send_tcp_packet(data)

def LocRem():

    update_matrix()
    global connect_flag
    print('flag')
    print(connect_flag)
    if connect_flag == 0:
        connect_flag = 1
        update_matrix()
    else:
        if mode_flag == "0":
            message = "*SCT:1\r\n"
            print("kuldes", message)
            response = send_tcp_packet(message)

        if mode_flag == "1":
            message = "*SCT:0\r\n"
            print("kuldes", message)
            response = send_tcp_packet(message)

    update_matrix()

    if mode_flag == "0":
        status_display.delete(0, tk.END)
        status_display.insert(0, "Local mode")
        button_mode.config(bg="red")
    if mode_flag == "1":
        status_display.delete(0, tk.END)
        status_display.insert(0, "Remote mode")
        button_mode.config(bg="green")

def increment_matrix(number1,number2):
    
    if number2 == 0:
        value = int(displays[number1].get()) if displays[number1].get().isdigit() else 0
        if 0 <=value <60:
            if value <9:
                displays[number1].delete(0, tk.END)
                displays[number1].insert(0, "0" + str(value + 1))
            else:                
                displays[number1].delete(0, tk.END)
                displays[number1].insert(0, str(value + 1))
    else:
        displays[number1].delete(0, tk.END)
        displays[number1].insert(0, "60")
                
    value = int(displays[number1].get())
    conn = str(connector_selection.get())
    matrix_step(conn,str(number1), str(value))
        
def decrement_matrix(number1,number2):
    value = int(displays[number1].get()) if displays[number1].get().isdigit() else 0
    if number2 == 0:
        if 0 <value <=60:            
            if value < 11:
                displays[number1].delete(0, tk.END)
                displays[number1].insert(0, "0" + str(value - 1))
            else:
                displays[number1].delete(0, tk.END)
                displays[number1].insert(0, str(value - 1))
    else:
        displays[number1].delete(0, tk.END)
        displays[number1].insert(0, "00")
        
    value = int(displays[number1].get())
    conn = str(connector_selection.get())
    matrix_step(conn,str(number1), str(value))
        

def on_radio_button_selected():
    print(f"Connector selected: {connector_selection.get()}")
    selected_value = connector_selection.get()
    button_color_change(selected_value)
    update_matrix()

def button_color_change(code):
    colors = ["#00FF00","#3399ff","#00ffff","#ffffff"]
    if code == 0:
        hex_color = "#00FF00"
    if code == 1:
        hex_color = "#3399ff"
    if code == 2:
        hex_color = "#00ffff"
    if code == 3:
        hex_color = "#ffffff"
    
    for x in range(0, 8):
        buttons_up[x].config(bg=colors[code])
        buttons_down[x].config(bg=colors[code])
    

def toggle_checkbox():
    # Print the state of the checkbox
    value = checkbox1_var.get() + (checkbox2_var.get() * 2) + (checkbox3_var.get() * 4) + (checkbox4_var.get() * 8) + (
                checkbox5_var.get() * 16) + (checkbox6_var.get() * 32) + (checkbox7_var.get() * 64) + (
                        checkbox8_var.get() * 128)

    if checkbox1_var.get():
        print("Checkbox is checked")
    else:
        print("Checkbox is unchecked")
    print(value)


root = tk.Tk()
root.title("BonnBonn Controller V1.0")
global connect_flag
connect_flag = 0
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

button_up1 = tk.Button(root, text="Up1", command=lambda: increment_matrix(0,0), width=4, height=2)
button_up1.grid(row=3, column=2, padx=padding, pady=padding)
button_up1.bind("<Button-3>", lambda event: increment_matrix(0,1))

button_up2 = tk.Button(root, text="Up2", command=lambda: increment_matrix(1,0), width=4, height=2)
button_up2.grid(row=3, column=3, padx=padding, pady=padding)
button_up2.bind("<Button-3>", lambda event: increment_matrix(1,1))

button_up3 = tk.Button(root, text="Up3", command=lambda: increment_matrix(2,0), width=4, height=2)
button_up3.grid(row=3, column=4, padx=padding, pady=padding)
button_up3.bind("<Button-3>", lambda event: increment_matrix(2,1))

button_up4 = tk.Button(root, text="Up4", command=lambda: increment_matrix(3,0), width=4, height=2)
button_up4.grid(row=3, column=5, padx=padding, pady=padding)
button_up4.bind("<Button-3>", lambda event: increment_matrix(3,1))

button_up5 = tk.Button(root, text="Up5", command=lambda: increment_matrix(4,0), width=4, height=2)
button_up5.grid(row=3, column=6, padx=padding, pady=padding)
button_up5.bind("<Button-3>", lambda event: increment_matrix(4,1))

button_up6 = tk.Button(root, text="Up6", command=lambda: increment_matrix(5,0), width=4, height=2)
button_up6.grid(row=3, column=7, padx=padding, pady=padding)
button_up6.bind("<Button-3>", lambda event: increment_matrix(5,1))

button_up7 = tk.Button(root, text="Up7", command=lambda: increment_matrix(6,0), height=2)
button_up7.grid(row=3, column=8, padx=padding, pady=padding)
button_up7.bind("<Button-3>", lambda event: increment_matrix(6,1))

button_up8 = tk.Button(root, text="Up8", command=lambda: increment_matrix(7,0), width=4, height=2)
button_up8.grid(row=3, column=9, padx=padding, pady=padding)
button_up8.bind("<Button-3>", lambda event: increment_matrix(7,1))

button_down1 = tk.Button(root, text="Dn1", command=lambda: decrement_matrix(0,0), width=4, height=2)
button_down1.grid(row=4, column=2, padx=padding, pady=padding)
button_down1.bind("<Button-3>", lambda event: decrement_matrix(0,1))

button_down2 = tk.Button(root, text="Dn2", command=lambda: decrement_matrix(1,0), width=4, height=2)
button_down2.grid(row=4, column=3, padx=padding, pady=padding)
button_down2.bind("<Button-3>", lambda event: decrement_matrix(1,1))

button_down3 = tk.Button(root, text="Dn3", command=lambda: decrement_matrix(2,0), width=4, height=2)
button_down3.grid(row=4, column=4, padx=padding, pady=padding)
button_down3.bind("<Button-3>", lambda event: decrement_matrix(2,1))

button_down4 = tk.Button(root, text="Dn4", command=lambda: decrement_matrix(3,0), width=4, height=2)
button_down4.grid(row=4, column=5, padx=padding, pady=padding)
button_down4.bind("<Button-3>", lambda event: decrement_matrix(3,1))

button_down5 = tk.Button(root, text="Dn5", command=lambda: decrement_matrix(4,0), width=4, height=2)
button_down5.grid(row=4, column=6, padx=padding, pady=padding)
button_down5.bind("<Button-3>", lambda event: decrement_matrix(4,1))

button_down6 = tk.Button(root, text="Dn6", command=lambda: decrement_matrix(5,0), width=4, height=2)
button_down6.grid(row=4, column=7, padx=padding, pady=padding)
button_down6.bind("<Button-3>", lambda event: decrement_matrix(5,1))

button_down7 = tk.Button(root, text="Dn7", command=lambda: decrement_matrix(6,0), width=4, height=2)
button_down7.grid(row=4, column=8, padx=padding, pady=padding)
button_down7.bind("<Button-3>", lambda event: decrement_matrix(6,1))

button_down8 = tk.Button(root, text="Dn8", command=lambda: decrement_matrix(7,0), width=4, height=2)
button_down8.grid(row=4, column=9, padx=padding, pady=padding)
button_down8.bind("<Button-3>", lambda event: decrement_matrix(7,1))

buttons_down = [button_down1,button_down2,button_down3,button_down4,button_down5,button_down6,button_down7,button_down8]
buttons_up = [button_up1,button_up2,button_up3,button_up4,button_up5,button_up6,button_up7,button_up8]
displays = [display1,display2,display3,display4,display5,display6,display7,display8]

radio_button1 = tk.Radiobutton(root, text="Connector 1", variable=connector_selection, value=0,
                               command=on_radio_button_selected, bg="#00FF00")
radio_button2 = tk.Radiobutton(root, text="Connector 2", variable=connector_selection, value=1,
                               command=on_radio_button_selected, bg="#3399ff")
radio_button3 = tk.Radiobutton(root, text="Connector 3", variable=connector_selection, value=2,
                               command=on_radio_button_selected, bg='#00ffff')
radio_button4 = tk.Radiobutton(root, text="Connector 4", variable=connector_selection, value=3,
                               command=on_radio_button_selected, bg='#ffffff')

radio_button1.grid(row=0, column=0, padx=padding, pady=padding)
radio_button2.grid(row=1, column=0, padx=padding, pady=padding)
radio_button3.grid(row=2, column=0, padx=padding, pady=padding)
radio_button4.grid(row=3, column=0, padx=padding, pady=padding)


button_mode = tk.Button(root, text="Local-Remote", command=LocRem, width=15, height=3, bg='#666699')
button_mode.grid(row=8, column=0, padx=10, pady=0)

status_display = tk.Entry(root, width=20, font=lcd_font2, justify='center', bg='white', fg='black')
status_display.grid(row=8, column=1, padx=0, pady=0)
status_display.insert(0, "<-Press to connect")

ip_label = tk.Label(root, text="Matrix IP address:", bg="white")
ip_label.grid(row=10, column=0, pady=10)
ip_entry = tk.Entry(root, width=15, font=lcd_font2, justify='center', bg='white', fg='black')
ip_entry.grid(row=10, column=1, padx=padding, pady=padding)
ip_entry.insert(0, "192.168.16.210")

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