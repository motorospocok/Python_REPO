# Bonn BUAW20 attenuator matrix Controller by ethtoja
# v1.0 - 21st October 2024 - working very basic functions - can step the matrix remotely :)
# v1.1 - 21st October 2024 - multiple button selection
# v1.2 - 22th October 2024 - added FileMenu, re-designed GUI, possible to store info entry content
# v1.3 - 29th October 2024 - added continous increasing and decreasing function
# v1.4 - 4th November 2024 - added cell info popup window, currently only LTE cells work

import tkinter as tk
from tkinter import filedialog, messagebox
import socket
from tktooltip import ToolTip
from tkinter import Toplevel

global connect_flag

def update_display(matrix_data):
    
    for x in range(0, 8):
        displays[x].delete(0, tk.END)
        displays[x].insert(0, str(matrix_data[x]))

def update_matrix():
    message = "*ASK\r\n"
    response = send_tcp_packet(message)    
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
        status_display.insert(0, "CAN NOT CONNECT")
        status_display.config(bg="red2")
        response = "!ASK:00,0,3,0,5.07,3.26,0.19,+35.6,08,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,47,37,27,60,60,56,46,36,26,60,60,55,45,35,25,60,60,54,44,34,24,60,60,53,43,33,23,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60"
    except socket.error as e:
        print(f"Socket error: {e}")

    finally:
        # Close the sock
        sock.close()

def matrix_step(connector,selected_matrix,value1):
    data = '*SAT:' + connector + ',' + selected_matrix + ',' + str(value1) + '\r\n'    
    send_tcp_packet(data)

def LocRem():
    global stop_blinking
    stop_blinking = True
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
            response = send_tcp_packet(message)

        if mode_flag == "1":
            message = "*SCT:0\r\n"            
            response = send_tcp_packet(message)

    update_matrix()

    if mode_flag == "0":
        status_display.config(bg="yellow",fg="black")
        status_display.delete(0, tk.END)
        status_display.insert(0, "Local mode")
        button_mode.config(bg="red")
    if mode_flag == "1":
        status_display.config(bg="green",fg="white")
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
    check_boxes = [checkbox1_var.get(),checkbox2_var.get(),checkbox3_var.get(),checkbox4_var.get(),checkbox5_var.get(),checkbox6_var.get(),checkbox7_var.get(),checkbox8_var.get()]            
    if check_boxes[number1] == True:
        print("heureka")
        for x in range (0, 8):
            if check_boxes[x] and x != number1:
                value = int(displays[x].get())
                if 0 <=value <60:
                    if value <9:
                        displays[x].delete(0, tk.END)
                        displays[x].insert(0, "0" + str(value + 1))
                    else:                
                        displays[x].delete(0, tk.END)
                        displays[x].insert(0, str(value + 1))
                value = int(displays[x].get())
                conn = str(connector_selection.get())
                matrix_step(conn,str(x), str(value))
        
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
    
    check_boxes = [checkbox1_var.get(),checkbox2_var.get(),checkbox3_var.get(),checkbox4_var.get(),checkbox5_var.get(),checkbox6_var.get(),checkbox7_var.get(),checkbox8_var.get()]    
    if check_boxes[number1] == True:
        print("heureka")
        for x in range (0, 8):
            if check_boxes[x] and x != number1:
                value = int(displays[x].get())
                if 0 <value <=60:
                    if value <11:
                        displays[x].delete(0, tk.END)
                        displays[x].insert(0, "0" + str(value - 1))
                    else:                
                        displays[x].delete(0, tk.END)
                        displays[x].insert(0, str(value - 1))
                value = int(displays[x].get())
                conn = str(connector_selection.get())
                matrix_step(conn,str(x), str(value))
                   
        

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
    global check_boxes
    check_boxes = [checkbox1_var.get(),checkbox2_var.get(),checkbox3_var.get(),checkbox4_var.get(),checkbox5_var.get(),checkbox6_var.get(),checkbox7_var.get(),checkbox8_var.get()]    
    
def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text files", "*.txt"),
                                                        ("All files", "*.*")])
    if file_path:
        with open(file_path, 'w') as file:
            content = ""
            for x in range (0, 8):
                content = content + info_boxes[x].get() + ';'
            file.write(content)
        messagebox.showinfo("Info", "File saved successfully!")

def load_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"),
                                                      ("All files", "*.*")])
    if file_path:
        with open(file_path, 'r') as file:
            content = file.read()
            content2 = content.split(';')
            for x in range (0, 8):
                if content2[x] != "":
                    info_boxes[x].delete(0, tk.END)
                    info_boxes[x].insert(0, content2[x])
        messagebox.showinfo("Info", "File loaded successfully!")

def exit_program():
    root.quit()

def toggle_text():
    if not stop_blinking:
        current_color = status_display.cget("bg")
        new_color = "yellow" if current_color == "white" else "white"
        status_display.config(bg=new_color)
        root.after(200, toggle_text)  # 500 ms múlva újra meghívja a toggle_color függvényt
        
def start_increment(number1,number2):    
    global incrementing
    if not incrementing: 
        incrementing = True
        continue_increment(number1,number2)

def continue_increment(number1,number2):
    if incrementing:
        increment_matrix(number1, number2)
        root.after(100, lambda: continue_increment(number1,number2))

def stop_increment(event):
    global incrementing
    incrementing = False
    

def start_decrement(number1,number2):    
    global decrementing
    if not decrementing: 
        decrementing = True
        continue_decrement(number1,number2)

def continue_decrement(number1,number2):
    if decrementing:
        decrement_matrix(number1, number2)
        root.after(100, lambda: continue_decrement(number1,number2))

def stop_decrement(event):
    global decrementing
    decrementing = False    

def find_cell_info(input_value):
    # Inicializáljuk a listát a találatok tárolására.
    results = []
    print("kereses: ",input_value)
    
    try:
        # Megnyitjuk a cell_info.txt fájlt olvasásra.
        with open('BonnBonn_cell_info.txt', 'r') as file:
            for line in file:
                # Levágjuk a sort az új sor jelektől és a whitespace-től.
                line = line.strip()
                # A sort elválasztjuk a ',' karakter szerint.
                elements = line.split(';')              
                
                # Ellenőrizzük, hogy a második elem megfelel-e az inputnak.
                if len(elements) > 1 and elements[2] == input_value:
                    # Ha igen, adjuk hozzá a results listához a teljes sort.                    
                    result = elements
                    break
    
    except FileNotFoundError:
        print("A BonnBonn_cell_info.txt fájl nem található.")
    
    return result

def open_lte_info(result):
    # Új ablak létrehozása
    cell_window = Toplevel(root)
    cell_window.title("LTE Cell Information")
    cell_window.geometry("300x340")

    site_label = tk.Label(cell_window, text="Site_name", bg="white")
    site_label.place(x=10,y=10)
    site_entry = tk.Entry(cell_window, width=10, font=lcd_font2, justify='center', bg=info_color_bg, fg=info_color_fg)
    site_entry.place(x=90,y=10)
        
    tech_label = tk.Label(cell_window, text="Technology", bg="white")
    tech_label.place(x=10,y=40)
    tech_entry = tk.Entry(cell_window, width=10, font=lcd_font2, justify='center', bg=info_color_bg, fg=info_color_fg)
    tech_entry.place(x=90,y=40)
    
    cell_label = tk.Label(cell_window, text="Cell name", bg="white")
    cell_label.place(x=10,y=70)
    cell_entry = tk.Entry(cell_window, width=10, font=lcd_font2, justify='center', bg=info_color_bg, fg=info_color_fg)
    cell_entry.place(x=90,y=70)
    
    PCI_label = tk.Label(cell_window, text="PCI", bg="white")
    PCI_label.place(x=10,y=100)
    PCI_entry = tk.Entry(cell_window, width=10, font=lcd_font2, justify='center', bg=info_color_bg, fg=info_color_fg)
    PCI_entry.place(x=90,y=100)
    
    TAC_label = tk.Label(cell_window, text="TAC", bg="white")
    TAC_label.place(x=10,y=130)
    TAC_entry = tk.Entry(cell_window, width=10, font=lcd_font2, justify='center', bg=info_color_bg, fg=info_color_fg)
    TAC_entry.place(x=90,y=130)
    
    BW_label = tk.Label(cell_window, text="Bandwidth", bg="white")
    BW_label.place(x=10,y=160)
    BW_entry = tk.Entry(cell_window, width=10, font=lcd_font2, justify='center', bg=info_color_bg, fg=info_color_fg)
    BW_entry.place(x=90,y=160)
    
    ArfcnDL_label = tk.Label(cell_window, text="ArfcnDL", bg="white")
    ArfcnDL_label.place(x=10,y=190)
    ArfcnDL_entry = tk.Entry(cell_window, width=10, font=lcd_font2, justify='center', bg=info_color_bg, fg=info_color_fg)
    ArfcnDL_entry.place(x=90,y=190)    
    freqDL_entry = tk.Entry(cell_window, width=10, font=lcd_font2, justify='center', bg=info_color_bg, fg=info_color_fg)
    freqDL_entry.place(x=190,y=190)
    
    ArfcnUL_label = tk.Label(cell_window, text="ArfcnUL", bg="white")
    ArfcnUL_label.place(x=10,y=220)
    ArfcnUL_entry = tk.Entry(cell_window, width=10, font=lcd_font2, justify='center', bg=info_color_bg, fg=info_color_fg)
    ArfcnUL_entry.place(x=90,y=220)
    freqUL_entry = tk.Entry(cell_window, width=10, font=lcd_font2, justify='center', bg=info_color_bg, fg=info_color_fg)
    freqUL_entry.place(x=190,y=220)
    
    band_label = tk.Label(cell_window, text="Band", bg="white")
    band_label.place(x=10,y=250)
    band_entry = tk.Entry(cell_window, width=10, font=lcd_font2, justify='center', bg=info_color_bg, fg=info_color_fg)
    band_entry.place(x=90,y=250)           
    
    enb_label = tk.Label(cell_window, text="eNodeB ID", bg="white")
    enb_label.place(x=10,y=280)
    enb_entry = tk.Entry(cell_window, width=10, font=lcd_font2, justify='center', bg=info_color_bg, fg=info_color_fg)
    enb_entry.place(x=90,y=280)
    

    # Gomb hozzáadása az új ablakhoz, amely bezárja az ablakot
    close_button = tk.Button(cell_window, text="Close", command=cell_window.destroy)
    close_button.place(x=110,y=310) 
    
    entries = [site_entry,tech_entry,cell_entry,PCI_entry,TAC_entry,BW_entry,ArfcnDL_entry,freqDL_entry,ArfcnUL_entry,freqUL_entry,band_entry,enb_entry]
    
    i = 0
    for elements in entries:
        elements.delete(0, tk.END)
        elements.insert(0, result[i])
        i = i + 1        
        

def on_info_click(event,content):
    print("itt vagyok",content)
    result = find_cell_info(content)
    if result:
        if result[1] == "LTE" or result[1] == "LTE-ESS":
            open_lte_info(result)    

root = tk.Tk()
root.title("BonnBonn Controller V1.4 by Toja")
root.geometry("635x335")
root.resizable(False, False)
stop_blinking = False
incrementing = False
decrementing = False

menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open", command=load_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_program)
menu_bar.add_cascade(label="File", menu=file_menu)
root.config(menu=menu_bar)

# Canvas létrehozása és elhelyezése
canvas = tk.Canvas(root, width=635, height=335)
canvas.place(x=0, y=0)

# Vonal rajzolása a Canvas-ra (x1, y1, x2, y2)
rectangle1 = canvas.create_rectangle(130, 95, 620, 140, fill="gray67")
rectangle2 = canvas.create_rectangle(130, 142, 620, 243, fill="gray40")
rectangle4 = canvas.create_rectangle(130, 245, 620, 275, fill="gray67")
rectangle5 = canvas.create_rectangle(5, 15, 120, 275, fill="gray67")
rectangle6 = canvas.create_rectangle(130, 280, 620, 320, fill="gray67")

ln_color = "Blue4"

line1 = canvas.create_line(165,75,165,90, fill=ln_color, width=3)
line2 = canvas.create_line(225,45,225,90, fill=ln_color, width=3)

line3 = canvas.create_line(285,75,285,90, fill=ln_color, width=3)
line4 = canvas.create_line(345,45,345,90, fill=ln_color, width=3)

line5 = canvas.create_line(405,75,405,90, fill=ln_color, width=3)
line6 = canvas.create_line(465,45,465,90, fill=ln_color, width=3)

line7 = canvas.create_line(525,75,525,90, fill=ln_color, width=3)
line8 = canvas.create_line(585,45,585,90, fill=ln_color, width=3)



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

radio_button1 = tk.Radiobutton(root, text="Connector 1", variable=connector_selection, value=0,
                               command=on_radio_button_selected, bg="#00FF00")
radio_button2 = tk.Radiobutton(root, text="Connector 2", variable=connector_selection, value=1,
                               command=on_radio_button_selected, bg="#3399ff")
radio_button3 = tk.Radiobutton(root, text="Connector 3", variable=connector_selection, value=2,
                               command=on_radio_button_selected, bg='#00ffff')
radio_button4 = tk.Radiobutton(root, text="Connector 4", variable=connector_selection, value=3,
                               command=on_radio_button_selected, bg='#ffffff')

radio_button1.place(x=15,y=20)
radio_button2.place(x=15,y=50)
radio_button3.place(x=15,y=80)
radio_button4.place(x=15,y=110)

info_color_bg = "gray23"
info_color_fg = "chartreuse"

info1 = tk.Entry(root, width=10, font=lcd_font2, justify='center', bg=info_color_bg, fg=info_color_fg)
info1.place(x=130,y=50)
info1.bind("<Double-1>", lambda event: on_info_click(event, info1.get()))

info2 = tk.Entry(root, width=10, font=lcd_font2, justify='center', bg=info_color_bg, fg=info_color_fg)
info2.place(x=185,y=20)
info2.bind("<Double-1>", lambda event: on_info_click(event, info2.get()))

info3 = tk.Entry(root, width=10, font=lcd_font2, justify='center', bg=info_color_bg, fg=info_color_fg)
info3.place(x=245,y=50)
info3.bind("<Double-1>", lambda event: on_info_click(event, info3.get()))

info4 = tk.Entry(root, width=10, font=lcd_font2, justify='center', bg=info_color_bg, fg=info_color_fg)
info4.place(x=305,y=20)
info4.bind("<Double-1>", lambda event: on_info_click(event, info4.get()))

info5 = tk.Entry(root, width=10, font=lcd_font2, justify='center', bg=info_color_bg, fg=info_color_fg)
info5.place(x=365,y=50)
info5.bind("<Double-1>", lambda event: on_info_click(event, info5.get()))

info6 = tk.Entry(root, width=10, font=lcd_font2, justify='center', bg=info_color_bg, fg=info_color_fg)
info6.place(x=425,y=20)
info6.bind("<Double-1>", lambda event: on_info_click(event, info6.get()))

info7 = tk.Entry(root, width=10, font=lcd_font2, justify='center', bg=info_color_bg, fg=info_color_fg)
info7.place(x=485,y=50)
info7.bind("<Double-1>", lambda event: on_info_click(event, info7.get()))

info8 = tk.Entry(root, width=10, font=lcd_font2, justify='center', bg=info_color_bg, fg=info_color_fg)
info8.place(x=545,y=20)
info8.bind("<Double-1>", lambda event: on_info_click(event, info8.get()))

info_boxes = [info1,info2,info3,info4,info5,info6,info7,info8]

display1 = tk.Entry(root, width=3, font=lcd_font, justify='center', bg='black', fg='light green')
display1.place(x=140,y=100)

display2 = tk.Entry(root, width=3, font=lcd_font, justify='center', bg='black', fg='light green')
display2.place(x=200,y=100)

display3 = tk.Entry(root, width=3, font=lcd_font, justify='center', bg='black', fg='light green')
display3.place(x=260,y=100)

display4 = tk.Entry(root, width=3, font=lcd_font, justify='center', bg='black', fg='light green')
display4.place(x=320,y=100)

display5 = tk.Entry(root, width=3, font=lcd_font, justify='center', bg='black', fg='light green')
display5.place(x=380,y=100)

display6 = tk.Entry(root, width=3, font=lcd_font, justify='center', bg='black', fg='light green')
display6.place(x=440,y=100)

display7 = tk.Entry(root, width=3, font=lcd_font, justify='center', bg='black', fg='light green')
display7.place(x=500,y=100)

display8 = tk.Entry(root, width=3, font=lcd_font, justify='center', bg='black', fg='light green')
display8.place(x=560,y=100)

button_up1 = tk.Button(root, text="Up1", width=4, height=2)
button_up1.place(x=145,y=145)
button_up1.bind("<Button-3>", lambda event: increment_matrix(0,1))
button_up1.bind("<ButtonPress-1>", lambda event: start_increment(0,0))
button_up1.bind("<ButtonRelease-1>", stop_increment)

button_up2 = tk.Button(root, text="Up2", width=4, height=2)
button_up2.place(x=205,y=145)
button_up2.bind("<Button-3>", lambda event: increment_matrix(1,1))
button_up2.bind("<ButtonPress-1>", lambda event: start_increment(1,0))
button_up2.bind("<ButtonRelease-1>", stop_increment)

button_up3 = tk.Button(root, text="Up3", width=4, height=2)
button_up3.place(x=265,y=145)
button_up3.bind("<Button-3>", lambda event: increment_matrix(2,1))
button_up3.bind("<ButtonPress-1>", lambda event: start_increment(2,0))
button_up3.bind("<ButtonRelease-1>", stop_increment)

button_up4 = tk.Button(root, text="Up4", width=4, height=2)
button_up4.place(x=325,y=145)
button_up4.bind("<Button-3>", lambda event: increment_matrix(3,1))
button_up4.bind("<ButtonPress-1>", lambda event: start_increment(3,0))
button_up4.bind("<ButtonRelease-1>", stop_increment)

button_up5 = tk.Button(root, text="Up5", width=4, height=2)
button_up5.place(x=385,y=145)
button_up5.bind("<Button-3>", lambda event: increment_matrix(4,1))
button_up5.bind("<ButtonPress-1>", lambda event: start_increment(4,0))
button_up5.bind("<ButtonRelease-1>", stop_increment)

button_up6 = tk.Button(root, text="Up6", width=4, height=2)
button_up6.place(x=445,y=145)
button_up6.bind("<Button-3>", lambda event: increment_matrix(5,1))
button_up6.bind("<ButtonPress-1>", lambda event: start_increment(5,0))
button_up6.bind("<ButtonRelease-1>", stop_increment)

button_up7 = tk.Button(root, text="Up7", width=4, height=2)
button_up7.place(x=510,y=145)
button_up7.bind("<Button-3>", lambda event: increment_matrix(6,1))
button_up7.bind("<ButtonPress-1>", lambda event: start_increment(6,0))
button_up7.bind("<ButtonRelease-1>", stop_increment)

button_up8 = tk.Button(root, text="Up8", width=4, height=2)
button_up8.place(x=565,y=145)
button_up8.bind("<Button-3>", lambda event: increment_matrix(7,1))
button_up8.bind("<ButtonPress-1>", lambda event: start_increment(7,0))
button_up8.bind("<ButtonRelease-1>", stop_increment)

button_down1 = tk.Button(root, text="Dn1", width=4, height=2)
button_down1.place(x=145,y=195)
button_down1.bind("<Button-3>", lambda event: decrement_matrix(0,1))
button_down1.bind("<ButtonPress-1>", lambda event: start_decrement(0,0))
button_down1.bind("<ButtonRelease-1>", stop_decrement)

button_down2 = tk.Button(root, text="Dn2", width=4, height=2)
button_down2.place(x=205,y=195)
button_down2.bind("<Button-3>", lambda event: decrement_matrix(1,1))
button_down2.bind("<ButtonPress-1>", lambda event: start_decrement(1,0))
button_down2.bind("<ButtonRelease-1>", stop_decrement)

button_down3 = tk.Button(root, text="Dn3", width=4, height=2)
button_down3.place(x=265,y=195)
button_down3.bind("<Button-3>", lambda event: decrement_matrix(2,1))
button_down3.bind("<ButtonPress-1>", lambda event: start_decrement(2,0))
button_down3.bind("<ButtonRelease-1>", stop_decrement)

button_down4 = tk.Button(root, text="Dn4", width=4, height=2)
button_down4.place(x=325,y=195)
button_down4.bind("<Button-3>", lambda event: decrement_matrix(3,1))
button_down4.bind("<ButtonPress-1>", lambda event: start_decrement(3,0))
button_down4.bind("<ButtonRelease-1>", stop_decrement)

button_down5 = tk.Button(root, text="Dn5", width=4, height=2)
button_down5.place(x=385,y=195)
button_down5.bind("<Button-3>", lambda event: decrement_matrix(4,1))
button_down5.bind("<ButtonPress-1>", lambda event: start_decrement(4,0))
button_down5.bind("<ButtonRelease-1>", stop_decrement)

button_down6 = tk.Button(root, text="Dn6", width=4, height=2)
button_down6.place(x=445,y=195)
button_down6.bind("<Button-3>", lambda event: decrement_matrix(5,1))
button_down6.bind("<ButtonPress-1>", lambda event: start_decrement(5,0))
button_down6.bind("<ButtonRelease-1>", stop_decrement)

button_down7 = tk.Button(root, text="Dn7", width=4, height=2)
button_down7.place(x=505,y=195)
button_down7.bind("<Button-3>", lambda event: decrement_matrix(6,1))
button_down7.bind("<ButtonPress-1>", lambda event: start_decrement(6,0))
button_down7.bind("<ButtonRelease-1>", stop_decrement)

button_down8 = tk.Button(root, text="Dn8", width=4, height=2)
button_down8.place(x=565,y=195)
button_down8.bind("<Button-3>", lambda event: decrement_matrix(7,1))
button_down8.bind("<ButtonPress-1>", lambda event: start_decrement(7,0))
button_down8.bind("<ButtonRelease-1>", stop_decrement)

ToolTip(button_up1, msg="Increase atteanuation,right click max 60 dB", delay=2.0)
ToolTip(button_up2, msg="Increase atteanuation,right click max 60 dB", delay=2.0)
ToolTip(button_up3, msg="Increase atteanuation,right click max 60 dB", delay=2.0)
ToolTip(button_up4, msg="Increase atteanuation,right click max 60 dB", delay=2.0)
ToolTip(button_up5, msg="Increase atteanuation,right click max 60 dB", delay=2.0)
ToolTip(button_up6, msg="Increase atteanuation,right click max 60 dB", delay=2.0)
ToolTip(button_up7, msg="Increase atteanuation,right click max 60 dB", delay=2.0)
ToolTip(button_up8, msg="Increase atteanuation,right click max 60 dB", delay=2.0)

checkbox1 = tk.Checkbutton(root, text="M1", variable=checkbox1_var, command=toggle_checkbox)
checkbox1.place(x=150,y=247)

checkbox2 = tk.Checkbutton(root, text="M2", variable=checkbox2_var, command=toggle_checkbox)
checkbox2.place(x=210,y=247)

checkbox3 = tk.Checkbutton(root, text="M3", variable=checkbox3_var, command=toggle_checkbox)
checkbox3.place(x=270,y=247)

checkbox4 = tk.Checkbutton(root, text="M4", variable=checkbox4_var, command=toggle_checkbox)
checkbox4.place(x=330,y=247)

checkbox5 = tk.Checkbutton(root, text="M5", variable=checkbox5_var, command=toggle_checkbox)
checkbox5.place(x=390,y=247)

checkbox6 = tk.Checkbutton(root, text="M6", variable=checkbox6_var, command=toggle_checkbox)
checkbox6.place(x=450,y=247)

checkbox7 = tk.Checkbutton(root, text="M7", variable=checkbox7_var, command=toggle_checkbox)
checkbox7.place(x=510,y=247)

checkbox8 = tk.Checkbutton(root, text="M8", variable=checkbox8_var, command=toggle_checkbox)
checkbox8.place(x=570,y=247)



buttons_down = [button_down1,button_down2,button_down3,button_down4,button_down5,button_down6,button_down7,button_down8]
buttons_up = [button_up1,button_up2,button_up3,button_up4,button_up5,button_up6,button_up7,button_up8]
displays = [display1,display2,display3,display4,display5,display6,display7,display8]


button_mode = tk.Button(root, text="Local-Remote", command=LocRem, width=12, height=3, bg='#666699')
button_mode.place(x=15,y=155)

status_display = tk.Entry(root, width=25, font=lcd_font2, justify='center', bg='gold', fg='black')
status_display.place(x=140,y=290)
status_display.insert(0, "Press Local-Remote First")

ip_label = tk.Label(root, text="Matrix IP address:", bg="white")
ip_label.place(x=360,y=290)
ip_entry = tk.Entry(root, width=15, font=lcd_font2, justify='center', bg='white', fg='black')
ip_entry.place(x=470,y=290)
ip_entry.insert(0, "192.168.16.210")

root.after(200, toggle_text)  # 500 ms múlva meghívja a toggle_text függvényt
root.mainloop()
