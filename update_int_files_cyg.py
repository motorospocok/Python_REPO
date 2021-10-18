#Support pywin program for 6631 FFI project
#This version was tested under cygwin environment

import os
import re
import sys

path1='/home/ETHTOJA/6631FFI/' #set the working directory
int_ip_oam='10.244.89.216'
int_ip_gw='10.244.89.217'
int_vid = '3001'

param_file = open(path1+'FFI_parameters.txt')
old_site_name = sys.argv[1]
new_site_name = old_site_name +'x'
file_list1 = os.listdir(path1+'1\\'+ old_site_name)
os.mkdir(path1+'1/' + new_site_name)


for line in param_file:
    if old_site_name in line:
        site_data = line.split(':')
new_fp = '>'+site_data[4]+'<'                 #New FP looks like >new_fp<
old_oam = site_data[1]
old_gw = site_data[2]
old_vid = site_data[3]

param_file.close()

for file_sites in file_list1:
    old_path = path1+'1/'  + old_site_name + '/'+ file_sites
    new_path = path1+'1/'  + new_site_name + '/'+ file_sites
    source_file = open(old_path)  # open the old file
    target_file = open(new_path, 'w')  # open a new file
    for line in source_file:
        y='ManagedElement='+old_site_name
        z='ManagedElement='+new_site_name
        if y in line: #If old site name found replace it with SiteNameX
            x = line.replace(y,z)
            line = x
            no_change_flag = 0
        if 'fingerprint' in line: #Also if Fingerprint found replace it with the new FP
            x = re.sub(r'>{1}.*?<', new_fp, line) #Simple replace was boring I was practicing regex :)
            line = x
            no_change_flag = 0
        if old_oam in line: #Change OAM address to the temporary OAM address
            x = line.replace(old_oam, int_ip_oam)
            line = x
            no_change_flag = 0
        if old_gw in line:
            x = line.replace(old_gw, int_ip_gw) #Change default router adddress to the temporary default router address
            line = x
            no_change_flag = 0
        if old_vid in line:
            x = line.replace(old_vid, int_vid) #Change the vlan id as well
            line = x
            no_change_flag = 0
        target_file.write(line)

    source_file.close()
    target_file.close()