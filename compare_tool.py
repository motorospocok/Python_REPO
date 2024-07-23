#this tool is written to compare post and pre HC files
#V1.0 - introduction

import os
from colorama import just_fix_windows_console
from termcolor import colored
from datetime import datetime

just_fix_windows_console()


directory_path = 'C:\cygwin64\home\ETHTOJA\HC\c2'
old_prefix = 'preHC'
new_prefix = 'postHC'

def print_result(text1,text2,color1):
    print(colored(text1,"white","on_magenta"))
    print(colored(text2,"white", color1))
    print(colored("--------------------------------------------","white", "on_blue"))


def collect_and_replace_files(directory, old_prefix, new_prefix):
    # List to hold the original file names
    original_files = []
    
    # List to hold the new file names
    new_files = []
    
    # Iterate over all the files in the directory
    for file in os.listdir(directory):
        # Check if the file name starts with the old prefix
        if file.startswith(old_prefix):
            original_files.append(file)
            # Create the new file name by replacing the old prefix with the new one
            new_file_name = file.replace(old_prefix, new_prefix, 1)
            # Check if the new file exists in the directory
            if os.path.exists(os.path.join(directory, new_file_name)):
                new_files.append(new_file_name)
                print(f"Ok, file has beenfound: {new_file_name}")
            else:
                print(f"This file not found: {new_file_name}")
    
    return original_files, new_files

def read_file_to_dict(filename):
    global header_string
    data_dict = {}    
    with open(filename, 'r', encoding='utf-8') as file:
        header_string = file.readline().strip()
        for line in file:
            parts = line.strip().split(';')
            key = parts[0]
            values = set(parts[1:])
            data_dict[key] = values
    return data_dict



# Get the list of original and new files
original_files, new_files = collect_and_replace_files(directory_path, old_prefix, new_prefix)

# Print the lists of files
print("Original files with prefix '{}':".format(old_prefix))
print(original_files)
print("\nNew files with prefix '{}':".format(new_prefix))
print(new_files)


# Read both files into dictionaries
for elements in new_files:        
    elements2 = elements.replace("postHC", "preHC")
    data1 = read_file_to_dict(elements2)
    data2 = read_file_to_dict(elements)

    new_elements = {}
    no_difference_keys = []

    for key, values2 in data2.items():
        if key in data1:
            new_values = values2 - data1[key]
            if new_values:
                new_elements[key] = new_values
            else:
                no_difference_keys.append(key)
        else:
            new_elements[key] = values2

# Store results in string variables
    result_string = ""
    result_string2 = ""

    if not new_elements:
        result_string = "All site seems ok"
    else:
        for key, values in new_elements.items():
            result_string += f"New elements in {key}: {', '.join(values)}\n"
        
    if not no_difference_keys:
        result_string2 = "All site seems ok"
    else:
        result_string2 = f"Keys with no differences: {', '.join(no_difference_keys)}"

# Print the result strings
    
    header_string = 'Changes on ' + header_string
    if result_string == "All site seems ok":
        print_result(header_string,result_string,"on_green")
    else:
        print_result(header_string,result_string,"on_red")
    header_string = 'No changes on ' + header_string
    print_result(header_string,result_string2,"on_green")
    
    
    
    