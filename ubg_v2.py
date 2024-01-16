import tkinter as tk
from tkinter import ttk

class RBS:
    instances = []

    def __init__(self, name, x_coord, y_coord, start_angle, end_angle, ran_tech, arfcn, pci):
        self.name = name if name else f"Instance {len(RBS.instances) + 1}"
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.start_angle = start_angle
        self.end_angle = end_angle
        self.ran_tech = ran_tech
        self.arfcn = arfcn
        self.pci = pci
        RBS.instances.append(self)

def create_rbs_instance():
    name = name_entry.get()
    x_coord = float(x_coord_entry.get())
    y_coord = float(y_coord_entry.get())
    start_angle = float(start_angle_entry.get() if start_angle_entry.get() else 0)
    end_angle = float(end_angle_entry.get() if end_angle_entry.get() else 360)
    ran_tech = ran_tech_combobox.get()
    arfcn = int(arfcn_entry.get())
    pci = int(pci_entry.get())

    rbs_instance = RBS(name, x_coord, y_coord, start_angle, end_angle, ran_tech, arfcn, pci)
    result_label["text"] = f"RBS instance '{rbs_instance.name}' created successfully."

    # If the instance list window is open, refresh the listbox
    if 'instances_window' in globals() and instances_window.winfo_exists():
        refresh_instance_list()

def show_rbs_instances():
    global instances_window
    instances_window = tk.Toplevel(root)
    instances_window.title("RBS Instances List")

    # Create a listbox to show RBS instances with attributes
    global listbox
    listbox = tk.Listbox(instances_window, width=80, selectmode=tk.SINGLE)
    for idx, rbs_instance in enumerate(RBS.instances):
        instance_info = f"Name: {rbs_instance.name}, X={rbs_instance.x_coord}, Y={rbs_instance.y_coord}, Start Angle={rbs_instance.start_angle}, End Angle={rbs_instance.end_angle}, Tech={rbs_instance.ran_tech}, ARFCN={rbs_instance.arfcn}, PCI={rbs_instance.pci}"
        listbox.insert(tk.END, instance_info)
    listbox.pack(pady=10)

    def edit_selected_instance():
        selected_index = listbox.curselection()
        if selected_index:
            selected_index = selected_index[0]
            selected_instance = RBS.instances[selected_index]

            # Update entry fields with selected instance's parameters
            name_entry.delete(0, tk.END)
            name_entry.insert(0, selected_instance.name)

            x_coord_entry.delete(0, tk.END)
            x_coord_entry.insert(0, selected_instance.x_coord)

            y_coord_entry.delete(0, tk.END)
            y_coord_entry.insert(0, selected_instance.y_coord)

            start_angle_entry.delete(0, tk.END)
            start_angle_entry.insert(0, selected_instance.start_angle)

            end_angle_entry.delete(0, tk.END)
            end_angle_entry.insert(0, selected_instance.end_angle)

            ran_tech_combobox.set(selected_instance.ran_tech)

            arfcn_entry.delete(0, tk.END)
            arfcn_entry.insert(0, selected_instance.arfcn)

            pci_entry.delete(0, tk.END)
            pci_entry.insert(0, selected_instance.pci)

            result_label["text"] = f"Editing instance '{selected_instance.name}'"

    def delete_selected_instance():
        selected_index = listbox.curselection()
        if selected_index:
            selected_index = selected_index[0]
            selected_instance = RBS.instances[selected_index]
            RBS.instances.pop(selected_index)
            listbox.delete(selected_index)
            result_label["text"] = f"Deleted instance '{selected_instance.name}'"

    # Create buttons to edit and delete the selected instance
    edit_button = ttk.Button(instances_window, text="Edit Selected Instance", command=edit_selected_instance)
    edit_button.pack(pady=5)

    delete_button = ttk.Button(instances_window, text="Delete Selected Instance", command=delete_selected_instance)
    delete_button.pack(pady=10)

    generate_button = ttk.Button(instances_window, text="Generate", command=generate_curl_command)
    generate_button.pack(pady=10)

    # Bind double left mouse button click to edit_selected_instance function
    listbox.bind('<Double-1>', lambda event=None: edit_selected_instance())

def refresh_instance_list():
    # Function to refresh the listbox in the instance list window
    listbox.delete(0, tk.END)
    for idx, rbs_instance in enumerate(RBS.instances):
        instance_info = f"Name: {rbs_instance.name}, X={rbs_instance.x_coord}, Y={rbs_instance.y_coord}, Start Angle={rbs_instance.start_angle}, End Angle={rbs_instance.end_angle}, Tech={rbs_instance.ran_tech}, ARFCN={rbs_instance.arfcn}, PCI={rbs_instance.pci}"
        listbox.insert(tk.END, instance_info)

def generate_curl_command():
    # Function to generate and display the CURL command
    instances_data = []
    for rbs_instance in RBS.instances:
        instance_data = {
            "idx": len(instances_data) + 1,
            "pci": rbs_instance.pci,
            "arfcn": rbs_instance.arfcn,
            "rat": rbs_instance.ran_tech,
            "location": {"x": rbs_instance.x_coord, "y": rbs_instance.y_coord},
            "radiation-angle": {"start-angle": rbs_instance.start_angle, "end-angle": rbs_instance.end_angle}
        }
        instances_data.append(instance_data)

    curl_command = f'curl -X POST -H "Content-type: application/json" -d "{{"antennas":{instances_data}}} $API_GW/api/radio-env/v1/rem_court1/antennas'

    curl_window = tk.Toplevel(root)
    curl_window.title("Generated CURL Command")

    text_box = tk.Text(curl_window, wrap="none", height=10, width=80)
    text_box.insert(tk.END, curl_command)
    text_box.pack(padx=10, pady=10)

# Create the main window
root = tk.Tk()
root.title("RBS Attributes Entry")

# Create and place labels and entry widgets
tk.Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
name_entry = ttk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="X Coordinate:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
x_coord_entry = ttk.Entry(root)
x_coord_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Y Coordinate:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
y_coord_entry = ttk.Entry(root)
y_coord_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Start Angle:").grid(row=3, column=0, padx=10, pady=5, sticky="e")
start_angle_entry = ttk.Entry(root)
start_angle_entry.grid(row=3, column=1, padx=10, pady=5)
start_angle_entry.insert(0, "0")  # Set default value to 0

tk.Label(root, text="End Angle:").grid(row=4, column=0, padx=10, pady=5, sticky="e")
end_angle_entry = ttk.Entry(root)
end_angle_entry.grid(row=4, column=1, padx=10, pady=5)
end_angle_entry.insert(0, "360")  # Set default value to 360

tk.Label(root, text="Random Technology:").grid(row=5, column=0, padx=10, pady=5, sticky="e")
ran_tech_values = ["LTE", "NR"]
ran_tech_combobox = ttk.Combobox(root, values=ran_tech_values)
ran_tech_combobox.grid(row=5, column=1, padx=10, pady=5)

tk.Label(root, text="ARFCN:").grid(row=6, column=0, padx=10, pady=5, sticky="e")
arfcn_entry = ttk.Entry(root)
arfcn_entry.grid(row=6, column=1, padx=10, pady=5)

tk.Label(root, text="PCI:").grid(row=7, column=0, padx=10, pady=5, sticky="e")
pci_entry = ttk.Entry(root)
pci_entry.grid(row=7, column=1, padx=10, pady=5)

# Create a button to create an RBS instance
create_button = ttk.Button(root, text="Create RBS", command=create_rbs_instance)
create_button.grid(row=8, column=0, columnspan=2, pady=10)

# Display label for result
result_label = ttk.Label(root, text="")
result_label.grid(row=9, column=0, columnspan=2, pady=5)

# Create a button to show the list of RBS instances
show_instances_button = ttk.Button(root, text="Show RBS Instances", command=show_rbs_instances)
show_instances_button.grid(row=10, column=0, columnspan=2, pady=10)

# Start the main event loop
root.mainloop()
    