#Alarm check tool by Toja
#This code is written for to evalate the alarms of the health_checkV2.mos file
#Just copy all the pre and post alarms into the same directory and run for this script
#Needs to install termcolor and colorama modules

import os
from datetime import datetime



version = "V1.1"
directory = "."  # Directory containing the log files
pre_alarms = []
pre_alarms2 = []
pre_sites = []
new_alarms = []
ceased_alarms = []
site_OK = []
site_NOK = []
file_path = "result.txt"

post_alarms = []
post_alarms2 = []
post_sites = []

#Handling additonal alarm check
def handling_special(alarm_string):
    ai_index = alarm_string.find("TimeoutExpired")
    if ai_index != -1:  # Check if "TimeoutExpired:" is found in the string
        alarm_string = alarm_string[:ai_index]
    return(alarm_string)
        
def alarm_comp1():    
    set_pre_alarms = set(pre_alarms2)
    set_post_alarms = set(post_alarms2)

    set_pre_sites = set(pre_sites)
    set_post_sites = set(post_sites)

    difference1 = set_pre_alarms - set_post_alarms
    difference2 = set_post_alarms - set_pre_alarms

    difference3 = set_pre_sites - set_post_sites 
    difference4 = set_post_sites - set_pre_sites 
    with open(file_path,"w") as file:
        text1 = "---------------------------------------------------------Alarm tool " + version + "-----------------------------------------------------"
        print(text1)
        file.write(text1 + "\n")
        text1 = "Site number check"
        file.write(text1 + "\n")
        print("Site number check")
        if difference3 == set() and difference4 == set():            
            
            print(" ")
            file.write(" " + "\n")
            text1 = "Ok, same sites are checked in the pre and post check"
            file.write(text1 + "\n")
            text1 = "-----------------------------------------------------------------------------------------------------------------------------"
            file.write(text1 + "\n")            
            print("Ok, same sites are checked in the pre and post check")
            print("-----------------------------------------------------------------------------------------------------------------------------")
        if difference3 != set():            
            text1 = "The following sites are not in the post check"
            file.write(text1 + "\n")
            text1 = str(difference3)            
            text2 = text1.split("'")            
            for elements in text2:
                if elements == ", " or elements == "}" or elements == "{" :
                    text2.remove(elements)
            for elements in text2:                    
                    handling_sites("NOK",elements)

            print("The following sites are not in the post check")
            for elements in text2:
                text1 = elements
                file.write(text1 + "\n")
                print(text1)
            

        if difference4 != set():            
            text1 = "The following sites are not in the pre check"
            text1 = str(difference4)            
            text2 = text1.split("'")
            for elements in text2:
                if elements == ", " or elements == "}" or elements == "{" :
                    text2.remove(elements)
            for elements in text2:                    
                    handling_sites("NOK",elements)                             
            print("The following sites are not in the pre check")
            for elements in text2:
                text1 = elements
                file.write(text1 + "\n")
                print(text1)

        if difference4 != set() or difference3 != set():
            
            text1 = "-----------------------------------------------------------------------------------------------------------------------------"
            file.write(text1 + "\n")
            text1 = "It seems the pre and post number of sites are different!"
            file.write(text1 + "\n")
            text1 = "The analysis will give wrong results"
            file.write(text1 + "\n")
            text1 = "-----------------------------------------------------------------------------------------------------------------------------"
            file.write(text1 + "\n")
            
            print("-----------------------------------------------------------------------------------------------------------------------------")
            print('It seems the pre and post number of sites are different!')
            print('The analysis will give wrong results!')
            print("-----------------------------------------------------------------------------------------------------------------------------")
        if difference2 == set():
            text1 = "No new alarms"
            file.write(text1 + "\n")
            print("No new alarms")
        else:
            text1 = "New alarm list:"
            file.write(text1 + "\n")
            file.write(" " + "\n")
            
            print("New alarm list:")
            print(" ")
            for elements in new_alarms:
                text1 = elements
                file.write(text1 + "\n")
                file.write(" " + "\n")
                print(elements)  
                print(" ")
        if difference1 != set():
            text1 = "-----------------------------------------------------------------------------------------------------------------------------"
            file.write(text1 + "\n")
            text1 = "Ceased alarm list:"
            file.write(text1 + "\n")
            
            print("-----------------------------------------------------------------------------------------------------------------------------")
            print("Ceased alarm list:")
            for elements in ceased_alarms:
                text1 = elements
                file.write(text1 + "\n")
                file.write(" " + "\n")
                print(elements)
                print(" ")
        file.write(" " + "\n")
        text1 = "-----------------------------------------------------------------------------------------------------------------------------"
        file.write(text1 + "\n")
        print(" ")
        print("-----------------------------------------------------------------------------------------------------------------------------")
        
        text1 = "Sites with OK status:"
        file.write(text1 + "\n")
        file.write(" " + "\n")
        print("Sites with OK status:")
        print(" ")
        for elements in site_OK:
            text1 = elements
            file.write(text1 + "\n")
            print(elements)
            
        text1 = "-----------------------------------------------------------------------------------------------------------------------------"
        file.write(text1 + "\n")
        text1 = "Sites need to be checked:"
        file.write(text1 + "\n")
        
        print("-----------------------------------------------------------------------------------------------------------------------------")        
        print("Sites need to be checked:")
        print(" ")
        if not site_NOK:
            text1 = "Seems everything superb!"
            file.write(text1 + "\n")
            print("Seems everything superb!")
        else:
            for elements in site_NOK:        
                text1 = str(elements)
                file.write(text1 + "\n")
                print(text1)
        file.write(" " + "\n")
        text1 = "-----------------------------------------------------------------------------------------------------------------------------"
        file.write(text1 + "\n")
        file.write(" " + "\n")
        print(" ")
        print("-----------------------------------------------------------------------------------------------------------------------------")
        print(" ")
        current_date_time = datetime.now()
        formatted_date_time = current_date_time.strftime("%Y-%m-%d %H:%M:%S")
        time1 = "Report date: " + formatted_date_time
        print(time1)
        text1 = time1
        file.write(text1 + "\n")
        print(" ")
        file.write(" " + "\n")
        print("-----------------------------------------------------------------------------------------------------------------------------")
        text1 = "-----------------------------------------------------------------------------------------------------------------------------"
        file.write(text1 + "\n")

def alarm_comp2():
    for elements in post_alarms2:
        s1 = elements.split(";")
        s2 = s1[1].split(",")
        s1 = s2[0].split("=")
        found_flag = "no"
        for elements2 in pre_alarms2:
            if elements == elements2:
                found_flag = "yes"
        if found_flag == "no":
            new_alarms.append(elements.strip())
            handling_sites("NOK",s1[1])
            #site_NOK.append(s1[1])
            try:
                site_OK.remove(s1[1])
            except:
                print("It seems site is missed in Pre HC")
                print(s1[1])
                
    for elements in pre_alarms2:
        found_flag = "no"
        for elements2 in post_alarms2:
            if elements == elements2:
                found_flag = "yes"
        if found_flag == "no":
            ceased_alarms.append(elements.strip())
            
def handling_sites(list_type,site_name):
    if list_type == "NOK":
        insert_flag = "YES"
        for element in site_NOK:
            if site_name == element:
                insert_flag = "NO"
        if insert_flag == "YES":
            site_NOK.append(site_name)
            
 
            
#Main program starts from here    
for filename in os.listdir(directory):        
    if "pre_alarms.txt" in filename:
        f1 = filename.split("_")
        pre_sites.append(f1[0])    
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


    
for filename in os.listdir(directory):
    if "post_alarms.txt" in filename:
        f1 = filename.split("_")
        post_sites.append(f1[0]) 
        site_OK.append(f1[0]) 
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
                                        
alarm_comp2()
alarm_comp1()
answer = input("Do you want to keep 'result.txt'? (yes/no): ")
if answer.lower() == "no":
    # Check if the file exists before attempting to delete it
    if os.path.exists(file_path):
        # Delete the file
        os.remove(file_path)
        print("File 'result.txt' has been deleted.")
    else:
        print("File 'result.txt' does not exist.")
else:
    print("File is stored.")
