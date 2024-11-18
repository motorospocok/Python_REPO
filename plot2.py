import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox

# CSV-fájl beolvasása
file_name = '1.csv'
data = pd.read_csv(file_name, sep=',')

# Grafikon készítése
def plot_graph():
    plt.figure(figsize=(10, 6))
    plt.plot(data['Frequency [kHz]'], data['Power [dbm]'], marker='o', linestyle='-')
    plt.title('Frequency vs Power')
    plt.xlabel('Frequency [kHz]')
    plt.ylabel('Power [dbm]')
    plt.grid(True)
    plt.show()

# Funkció a frekvencia keresésére
def get_power():
    try:
        frequency = float(entry.get())
        power = data.loc[data['Frequency [kHz]'] == frequency, 'Power [dbm]'].values[0]
        messagebox.showinfo("Eredmény", f"A {frequency} kHz frekvenciához tartozó teljesítmény: {power} dBm")
    except IndexError:
        messagebox.showwarning("Hiba", "A megadott frekvencia nem található.")
    except ValueError:
        messagebox.showwarning("Hiba", "Kérjük, egy számot adjon meg.")

# GUI ablak létrehozása
root = tk.Tk()
root.title("Frekvencia és Teljesítmény Kereső")

# Frekvencia input mező
label = tk.Label(root, text="Add meg a frekvenciát [kHz]:")
label.pack()

entry = tk.Entry(root)
entry.pack()

# Keresés gomb
button = tk.Button(root, text="Keresés", command=get_power)
button.pack()

# Grafikon gomb
plot_button = tk.Button(root, text="Grafikon megjelenítése", command=plot_graph)
plot_button.pack()

# Ablak megjelenítése
root.mainloop()