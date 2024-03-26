import os
from colorama import just_fix_windows_console
from termcolor import colored
just_fix_windows_console()

directory = "."  # Directory containing the log files
pre_alarms = []
pre_alarms2 = []

post_alarms = []
post_alarms2 = []

#Handling additonal alarm check
def handling_special(alarm_string):
 ai_index = alarm_string.find("TimeoutExpired")
 if ai_index != -1:  # Check if "TimeoutExpired:" is found in the string
    alarm_string = alarm_string[:ai_index]
 return(alarm_string)
 


for filename in os.listdir(directory):
    if "pre_alarms.txt" in filename:
        with open(os.path.join(directory, filename), "r") as file:
            for line in file:
                if "ManagedElement" in line:
                    pre_alarms.append(line.strip())
                    cut_off_parts = ';'.join(line.split(';')[2:-2])
                    ai_index = cut_off_parts.find("AI:")
                    if ai_index != -1:  # Check if "AI:" is found in the string
                        cut_off_parts = cut_off_parts[:ai_index]
                    cut_off_parts = handling_special(cut_off_parts)
                    pre_alarms2.append(cut_off_parts.strip())

print("Lines containing 'ManagedElement':")
for line in pre_alarms:
    print(line)
print("--------")
for line in pre_alarms2:
    print(line)
    
for filename in os.listdir(directory):
    if "post_alarms.txt" in filename:
        with open(os.path.join(directory, filename), "r") as file:
            for line in file:
                if "ManagedElement" in line:
                    post_alarms.append(line.strip())
                    cut_off_parts = ';'.join(line.split(';')[2:-2])
                    ai_index = cut_off_parts.find("AI:")
                    if ai_index != -1:  # Check if "AI:" is found in the string
                        cut_off_parts = cut_off_parts[:ai_index]
                    cut_off_parts = handling_special(cut_off_parts)
                    post_alarms2.append(cut_off_parts.strip())
                    
for line in post_alarms:
    print(line)
print("--------")
for line in post_alarms2:
    print(line)
set_pre_alarms = set(pre_alarms2)
set_post_alarms = set(post_alarms2)

difference1 = set_pre_alarms - set_post_alarms
difference2 = set_post_alarms - set_pre_alarms

print("--------")
print(difference1)
print(difference2)
if difference2 == set():
 print("No new alarms")
else:
 print("New alarm list")
 print(colored(difference2,'white','on_red'))
if difference1 != set():
 print("The following alarms are ceased:")
 print(colored(difference1, 'white', 'on_green'))


