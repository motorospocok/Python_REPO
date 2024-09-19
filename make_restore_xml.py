#!/usr/bin/python3

import os

def get_directories(path, user_input):
    directories = []
    try:
        # Walk through the directory
        for entry in os.scandir(path):
            if entry.is_dir():
                if user_input == 'all' or user_input in entry.name:
                    directories.append(entry.name)
    except Exception as e:
        print(f"An error occurred: {e}")
    return directories

def get_files(path, user_input):
    files = []
    try:
        # Walk through the directory
        for entry in os.scandir(path):
            if entry.is_file():
                if user_input == 'all' or user_input in entry.name:
                    files.append(entry.name)
    except Exception as e:
        print(f"An error occurred: {e}")
    return files


def template_read(file_name):
    try:
    	with open(file_name, 'r') as file:
        	template_content = file.read()
    except FileNotFoundError:
    	print("template.xml file not found. Make sure the file exists in the same directory as this script.")
    	exit(1)
    return template_content

def print_and_select(array_to_print):
    print('----------------------------------------------------------------------------------------------')
    for index, element in enumerate(array_to_print, start=0):
    	print(f"{index}. {element}")
    print('----------------------------------------------------------------------------------------------')
    user_input = input("Enter the selection number ")
    user_input = int(user_input)
    selected_element = array_to_print[user_input]
    return selected_element

# Directory path
path1 =['/home/demo/sftp/sw','/home/demo/sftp/backups']
template1 =['/home/demo/sftp/templates/recovery_template.xml']

# Get the list of directories

print('----------------------------------------------------------------------------------------------')
user_input = input("Enter 'all' to store all directories or a specific string to filter directories: ").strip()
sw_dirs = get_directories(path1[0],user_input)

print('----------------------------------------------------------------------------------------------')
user_input = input("Enter 'all' to store all files or a specific string to filter files: ").strip()
backup_files = get_files(path1[1], user_input)
print(' ')
selected_backup = print_and_select(backup_files)
selected_sw = print_and_select(sw_dirs)

# Print the directories
#print('----------------------------------------------------------------------------------------------')
#print("Directories:", sw_dirs)
#print("Backup files:", backup_files)
#print('----------------------------------------------------------------------------------------------')
#print(' ')

template_content1 = template_read(template1[0])
modified_content = template_content1.replace("backup_here", selected_backup).replace("sw_here", selected_sw)

new_file_name = input("Enter the new file name (with extension): ").strip()
new_file_name = '/home/demo/sftp/xmls/' + new_file_name

with open(new_file_name, 'w') as new_file:
    new_file.write(modified_content)

print(' ')
print('----------------------------------------------------------------------------------------------')
print(f"Modified content has been written to {new_file_name}")
print('----------------------------------------------------------------------------------------------')
print('Now you use the lmt laptop for recovery')
print(' ')
print('Host:  169.254.2.1')
print('Username: demo')
print('Password: demo12')
print(f"Site Installation File: {new_file_name}")
print('----------------------------------------------------------------------------------------------')

