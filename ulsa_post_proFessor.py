# Ulsa post processor file
# Just made several ULSA capture CSV in one directory after start this application and select the directory
# After merging the average values into one CSV file the graph can be displayed / plotted 
# v1.0 - first  working version
# v1.1 - Added graph title, legend and color parameters
# v1.2 - Added function to plot two data diagramm
# v1.2b - Some minor GUI modification
# v1.3 - Redesigned GUI and simplified plotting
# v1.4 - Added some minor changes e.g color change of legend

import os
import pandas as pd
import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt
from tkinter import messagebox
from tkinter import Toplevel

global version
version = "v1.4"

def select_file():
    # Fájl kiválasztó dialógus megnyitása, CSV fájlok szűrésével
    file_path = filedialog.askopenfilename(title="Select CSV file",
                                            filetypes=[("CSV files", "*.csv"), ("All files", "*.*")])
    if file_path:  # Ellenőrizzük, hogy választottunk-e
        directory = os.path.dirname(file_path)  # Kiválasztott fájl könyvtára
        entry_var.set(directory)  # A könyvtár elérési útját állítjuk be az Entry mezőbe
        enable_ok_button()  # Aktiváljuk az OK gombot, ha van elérési út

def enable_ok_button(*args):
    """Aktiválja vagy deaktiválja az OK gombot attól függően, hogy az Entry mező ki van-e töltve."""
    if entry_var.get():  # Ha az Entry mező nem üres
        merge_button.config(state=tk.NORMAL)
        plot_button.config(state=tk.NORMAL)
    else:
        merge_button.config(state=tk.DISABLED)  # Az OK gomb inaktív
        plot_button.config(state=tk.DISABLED)

def merge_csv():
    directory = entry.get()
    file_path = os.path.join(directory, "average_values.csv")
    if os.path.isfile(file_path):
        try:
            os.remove(file_path)  # Törölni a fájlt
            print(f"A '{file_path}' old file is deleted.")
        except Exception as e:
            print(f"Error during deleting the file: {e}")
    else:
        print(f"A '{file_path}' fájl nem található.")
    
          
    # Egy üres DataFrame létrehozása az adatok tárolására
    data = pd.DataFrame()    

    # A legtöbb fájl beolvasása a megadott könyvtárból
    for filename in os.listdir(directory):
        if filename.endswith('.csv'):
            file_path = os.path.join(directory, filename)
            # A CSV fájl beolvasása, az első sort (fejléc) kihagyva
            df = pd.read_csv(file_path, header=0)
            # Az első oszlop és a második oszlop hozzáadása a DataFrame-hez
            if data.empty:
                data = df[['Frequency [kHz]', 'Power [dbm]']]
            else:
                data = pd.concat([data, df[['Frequency [kHz]', 'Power [dbm]']]], axis=1)

    # Az adatok átlagolása a második oszlopban
    averages = data.iloc[:, 1::2].mean(axis=1).round(2)

    # Az eredeti első oszlop és az átlagok összekapcsolása új DataFrame-be
    result = pd.DataFrame({
        'Frequency [kHz]': data.iloc[:, 0],  # Az eredeti első oszlop
        'Average Power [dbm]': averages  # Az átlagok
    })
    csv_path = os.path.join(directory, "average_values.csv")
    # A fejléc kiírása és adatok kiírása egy új CSV fájlba
    result.to_csv(csv_path, index=False)

    print("The average data is calculated and written into csv file")

def color_change():
     color_1 = str(csv_entries[6].get())
     color_2 = str(csv_entries[7].get())
     print(color_1)
     print(color_2)
     csv_entries[4].config(fg=color_1)
     csv_entries[5].config(fg=color_2)
     
        
def merge_two():
    # Új ablak létrehozása
    
    checkbox1_var = tk.BooleanVar()
    checkbox2_var = tk.BooleanVar()
    mconnector_selection = tk.IntVar()
    
    merge_window = Toplevel(root)
    merge_window.title("Plot Function")
    merge_window.geometry("600x500+500+100")
    merge_window.configure(bg="gray")
    canvas = tk.Canvas(merge_window, width=600, height=500)
    canvas.place(x=0, y=0)
    line1 = canvas.create_line(0,4,600,4, fill="blue", width=2)
    line2 = canvas.create_line(0,102,600,102, fill="blue", width=2)
    line3 = canvas.create_line(0,140,600,140, fill="blue", width=2)
    line4 = canvas.create_line(0,185,600,185, fill="blue", width=2)
    line4 = canvas.create_line(0,355,600,355, fill="blue", width=2)
    
    merge_button2 = tk.Button(merge_window, text="Sum CSV file", state=tk.DISABLED) 
    merge_button2.place(x=10,y=70)
    merge_button2.bind("<Button-1>", lambda event: merge_csv2())
    
    generate_button = tk.Button(merge_window, text="Generate Merged CSV from the two files into SUM CSV ", state=tk.DISABLED) 
    generate_button.place(x=10,y=108)
    generate_button.bind("<Button-1>", lambda event: merge_csv3())
    
    merge_entry = tk.Entry(merge_window, width=70, justify='left')
    merge_entry.place(x=150,y=72)
    merge_entry.insert(0, "Waiting for generation")
    
    csv1_entry = tk.Entry(merge_window, width=70, justify='left')
    csv1_entry.place(x=150,y=12)
    csv1_entry.insert(0, "Select a CSV file")
    csv1_button = tk.Button(merge_window, text="Select 1st CSV File") 
    csv1_button.place(x=10,y=10)
    csv1_button.bind("<Button-1>", lambda event: select_csv(0))
    
    csv2_entry = tk.Entry(merge_window, width=70, justify='left')
    csv2_entry.place(x=150,y=42)
    csv2_entry.insert(0, "Select a CSV file")
    csv2_button = tk.Button(merge_window, text="Select 2nd CSV File") 
    csv2_button.place(x=10,y=40)
    csv2_button.bind("<Button-1>", lambda event: select_csv(1))
    
    mraph_title_label = tk.Label(merge_window, text="Graph Title")
    mraph_title_label.place(x=10,y=195)

    mgraph1_title_entry = tk.Entry(merge_window, width=35)
    mgraph1_title_entry.place(x=150,y=195)
    mgraph1_title_entry.insert(0, "ULSA spectrum on average")
    
    mgraph1_legend_label = tk.Label(merge_window, text="Graph legend No.1: ",bg="lightblue")
    mgraph1_legend_label.place(x=10,y=225)
    
    mcheckbox1 = tk.Checkbutton(merge_window, text="Select Graph 1", variable=checkbox1_var)
    mcheckbox1.place(x=390,y=223)

    mgraph1_legend_entry = tk.Entry(merge_window, width=35, fg="blue", bg="white")
    mgraph1_legend_entry.place(x=150,y=225)
    mgraph1_legend_entry.insert(0, "ULSA average result 1 [dbm]")

    mgraph1_color_label = tk.Label(merge_window, text="Color of graph No 1.: ", bg="lightblue")
    mgraph1_color_label.place(x=10,y=255)

    mspinbox1_graphColor = tk.Spinbox(merge_window, values=("blue", "red", "green", "purple", "cyan", "black", "yellow"), bg="lightblue",command=lambda: color_change())
    mspinbox1_graphColor.place(x=150,y=255)
    
    mgraph2_legend_label = tk.Label(merge_window, text="Graph legend No.2: ", bg="PeachPuff2")
    mgraph2_legend_label.place(x=10,y=300)

    mgraph2_legend_entry = tk.Entry(merge_window, width=35, fg="red", bg="white")
    mgraph2_legend_entry.place(x=150,y=300)
    mgraph2_legend_entry.insert(0, "ULSA average result 2 [dbm]")
    
    mcheckbox2 = tk.Checkbutton(merge_window, text="Select Graph 2", variable=checkbox2_var)
    mcheckbox2.place(x=390,y=298)

    mgraph2_color_label = tk.Label(merge_window, text="Color of graph No 2.: ", bg="PeachPuff2")
    mgraph2_color_label.place(x=10,y=330)

    mspinbox2_graphColor = tk.Spinbox(merge_window, values=("red", "blue", "green", "purple", "cyan", "black", "yellow"), bg="PeachPuff2",command=lambda: color_change())
    mspinbox2_graphColor.place(x=150,y=330)
    
    mradio_button1 = tk.Radiobutton(merge_window, text="Line graph style", variable=mconnector_selection, value=0, bg="gray64")
    mradio_button1.place(x=10,y=370)

    mradio_button2 = tk.Radiobutton(merge_window, text="Dot graph style", variable=mconnector_selection, value=1, bg="gray64")
    mradio_button2.place(x=150,y=370)
    
    mlabel_max = tk.Label(merge_window, text="Max value of Y-axis")
    mlabel_max.place(x=10,y=400)

    mentry_max = tk.Entry(merge_window, width=15)
    mentry_max.place(x=150,y=400)
    mentry_max.insert(0, "-90")

    mlabel_min = tk.Label(merge_window, text="Max value of Y-axis")
    mlabel_min.place(x=10,y=430)

    mentry_min = tk.Entry(merge_window, width=15)
    mentry_min.place(x=150,y=430)
    mentry_min.insert(0, "-150")
    
    mplot_button = tk.Button(merge_window, text="Plot Graph", command=lambda: plot_graph2(checkbox1_var,checkbox2_var,mconnector_selection))
    mplot_button.place(x=130,y=460)
        
    global mcolor_box
    mcolor_box = [mspinbox1_graphColor, mspinbox2_graphColor]
    global csv_entries
    csv_entries = [csv1_entry, csv2_entry, merge_entry, mgraph1_title_entry, mgraph1_legend_entry, mgraph2_legend_entry, mspinbox1_graphColor, mspinbox2_graphColor, mentry_max, mentry_min]
    global csv_buttons
    csv_buttons = [csv1_button, csv2_button, merge_button2, generate_button]

def plot_graph2(graph_selection1,graph_selection2,style_selection):    
    print(style_selection)
    conn = int(style_selection.get())
    line_style = ['-',':']
    data_file_name = str(csv_entries[2].get())
    print(data_file_name)
    data1 = pd.read_csv(data_file_name, sep=',')
    plt.figure(figsize=(10, 6))
    label_1 = str(csv_entries[4].get())
    label_2 = str(csv_entries[5].get())
    title_1 = str(csv_entries[3].get())
    color_1 = str(csv_entries[6].get())
    color_2 = str(csv_entries[7].get())
    
    # Első oszlop: Power1 [dbm]
    if graph_selection1.get() == 1 and graph_selection2.get() != 1:
        plt.plot(data1['Frequency [kHz]'], data1['Power1 [dbm]'], marker=',', linestyle=line_style[conn], color=color_1, label=label_1)
        
    if graph_selection1.get() == 1 and graph_selection2.get() == 1:
        plt.plot(data1['Frequency [kHz]'], data1['Power1 [dbm]'], marker=',', linestyle=line_style[conn], color=color_1, label=label_1)
        plt.plot(data1['Frequency [kHz]'], data1['Power2 [dbm]'], marker=',', linestyle=line_style[conn], color=color_2, label=label_2)
    
    # Második oszlop: Power2 [dbm]
    if graph_selection2.get() == 1 and graph_selection1.get() != 1:
        plt.plot(data1['Frequency [kHz]'], data1['Power2 [dbm]'], marker=',', linestyle=line_style[conn], color=color_2, label=label_2)
    
    
    
    plt.title(title_1)
    plt.xlabel('Frequency [kHz]')
    plt.ylabel('Power [dbm]')
    plt.grid(True)
    plt.legend()  # Megjeleníti a jelmagyarázatot
    max_value = int(csv_entries[8].get())
    min_value = int(csv_entries[9].get())
    plt.ylim(min_value,max_value)
    plt.show()
    

def select_csv(file_entry):
    file_path = filedialog.askopenfilename(title="Select CSV file",
                                            filetypes=[("CSV files", "*.csv"), ("All files", "*.*")])
    if file_path:  # Ellenőrizzük, hogy választottunk-e                
        csv_entries[file_entry].delete(0, tk.END)
        csv_entries[file_entry].insert(0, file_path)
    
    if csv_entries[0] != "Select a CSV file" and csv_entries[1] != "Select a CSV file":
        csv_buttons[2].config(state=tk.NORMAL)
        
    
def merge_csv2():
    file1 = csv_entries[0].get()
    file2 = csv_entries[1].get()
    file_path = filedialog.asksaveasfilename(title="Select CSV file",filetypes=[("CSV files", "*.csv"), ("All files", "*.*")])
    csv_entries[2].delete(0, tk.END)
    csv_entries[2].insert(0, file_path)
    csv_buttons[3].config(state=tk.NORMAL)
    
def merge_csv3():
    file1 = csv_entries[0].get()
    file2 = csv_entries[1].get()
    output_file = csv_entries[2].get()
    data1 = pd.read_csv(file1)
    data2 = pd.read_csv(file2)
    print(data1)
    print('------------')
    print(data2)
    

    combined_data = pd.DataFrame({
    'Frequency [kHz]': data1.iloc[:, 0],  
    'Power1 [dbm]': data1.iloc[:, 1],
    'Power2 [dbm]': data2.iloc[:, 1]})

# Az új fájl kiírása, a fejléc is szerepel
    combined_data.to_csv(output_file, index=False)

    print(f"Az adatok sikeresen kiírásra kerültek a {output_file} fájlba.")    


    
        
    
# Fő ablak létrehozása
root = tk.Tk()
title_text1 = "ULSA post proFessor :) " + version + " by Toja"
root.title(title_text1)
root.geometry("380x170+100+100")
root.resizable(False, False)

connector_selection = tk.IntVar()

label_1 = tk.Label(root, text="Working Directory")
label_1.place(x=10,y=10)

entry_var = tk.StringVar()
entry_var.trace_add("write", enable_ok_button)  # Figyel az Entry mező változásaira
entry = tk.Entry(root, width=35, justify='center', bg='white', fg='black',textvariable=entry_var)
entry.place(x=120,y=10)

file_button = tk.Button(root, text="Select source CSV files", command=select_file)
file_button.place(x=130,y=45)

merge_button = tk.Button(root, text="Create CSV file with average values", command=merge_csv, state=tk.DISABLED)
merge_button.place(x=130,y=75)



plot_button = tk.Button(root, text="Plot Functions", command=merge_two)
plot_button.place(x=130,y=110)

# Fő ciklus
root.mainloop()