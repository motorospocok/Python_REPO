# Ulsa post processor file
# Just made several ULSA capture CSV in one directory after start this application and select the directory
# After merging the average values into one CSV file the graph can be displayed / plotted 
# v1.0 - first  working version
# v1.1 - Added graph title, legend and color parameters

import os
import pandas as pd
import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt
from tkinter import messagebox

global version
version = "v1.1"

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
    
def plot_graph():
    directory = entry.get()
    conn = int(connector_selection.get())
    line_style = ['-',':']
    data_file_name = os.path.join(directory, 'average_values.csv')    
    data1 = pd.read_csv(data_file_name, sep=',')
    plt.figure(figsize=(10, 6))
    label_1 = str(graph_legend1_entry.get())
    title_1 = str(graph_title_entry.get())
    color_1 =str(spinbox_graphColor.get())
    
    # Első oszlop: Power1 [dbm]
    plt.plot(data1['Frequency [kHz]'], data1['Average Power [dbm]'], marker=',', linestyle=line_style[conn], color=color_1, label=label_1)
    
    # Második oszlop: Power2 [dbm]
    #plt.plot(data['Frequency [kHz]'], data1['Power2 [dbm]'], marker=',', linestyle=':', color='red', label='Power2 [dbm]')
    
    plt.title(title_1)
    plt.xlabel('Frequency [kHz]')
    plt.ylabel('Power [dbm]')
    plt.grid(True)
    plt.legend()  # Megjeleníti a jelmagyarázatot
    max_value = int(entry_max.get())
    min_value = int(entry_min.get())
    plt.ylim(min_value,max_value)
    plt.show()

# Fő ablak létrehozása
root = tk.Tk()
title_text1 = "ULSA post proFessor :) " + version + " by Toja"
root.title(title_text1)
root.geometry("380x350")
root.resizable(False, False)

connector_selection = tk.IntVar()

label_1 = tk.Label(root, text="Working Directory")
label_1.place(x=10,y=10)

entry_var = tk.StringVar()
entry_var.trace_add("write", enable_ok_button)  # Figyel az Entry mező változásaira
entry = tk.Entry(root, width=35, justify='center', bg='white', fg='black',textvariable=entry_var)
entry.place(x=120,y=10)

file_button = tk.Button(root, text="Select directory", command=select_file)
file_button.place(x=130,y=45)

merge_button = tk.Button(root, text="Merge CSV files", command=merge_csv, state=tk.DISABLED)
merge_button.place(x=130,y=75)

label_max = tk.Label(root, text="Max value of Y-axis")
label_max.place(x=10,y=105)

entry_max = tk.Entry(root, width=15)
entry_max.place(x=150,y=105)
entry_max.insert(0, "-90")

label_min = tk.Label(root, text="Max value of Y-axis")
label_min.place(x=10,y=135)

entry_min = tk.Entry(root, width=15)
entry_min.place(x=150,y=135)
entry_min.insert(0, "-150")

radio_button1 = tk.Radiobutton(root, text="Line graph style", variable=connector_selection, value=0, bg="gray64")
radio_button1.place(x=10,y=165)

radio_button2 = tk.Radiobutton(root, text="Dot graph style", variable=connector_selection, value=1, bg="gray64")
radio_button2.place(x=150,y=165)

graph_title_label = tk.Label(root, text="Graph Title")
graph_title_label.place(x=10,y=195)

graph_title_entry = tk.Entry(root, width=35)
graph_title_entry.place(x=150,y=195)
graph_title_entry.insert(0, "ULSA spectrum on average")

graph_legend1_label = tk.Label(root, text="Graph legend No.1: ")
graph_legend1_label.place(x=10,y=225)

graph_legend1_entry = tk.Entry(root, width=35)
graph_legend1_entry.place(x=150,y=225)
graph_legend1_entry.insert(0, "ULSA average result [dbm]")

graph_color_label = tk.Label(root, text="Color of graph No 1.: ")
graph_color_label.place(x=10,y=255)

spinbox_graphColor = tk.Spinbox(root, values=("blue", "red", "green", "purple", "cyan", "black", "yellow"))
spinbox_graphColor.place(x=150,y=255)

plot_button = tk.Button(root, text="Plot Graph", command=plot_graph, state=tk.DISABLED)
plot_button.place(x=130,y=300)

# Fő ciklus
root.mainloop()