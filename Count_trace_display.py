import re
import sys
import os
import time

counter_value = []
counter_list = []
counter_collection = []


def counter_collection(c_name,c_value):
 if c_name in counter_list:
     x = counter_list.index(c_name)
     counter_value[x] = counter_value[x] + c_value
 else:
     counter_list.append(c_name)
     counter_value.append(c_value)
 #print('vegul')
 
 print("\r", counter_list,counter_value,end = '')
 #print(counter_list)
 #print(counter_value)


for line in sys.stdin:
       if bool(re.search('D.h:48',line)) == True:
         full_content = re.search('Counter:.*steps.*,',line).group() #Counter: kezdodo ;s steps_akarmi vesszovel a vegen masolasa 
         step_counter = re.search('steps.*,',line).group() #steps es , jel kozott rakja a valtozoba
         step = re.search(r'[0-9]',step_counter).group() #csak szamok masolasa a valtozoba
         step_value = int(step)
         counter_name = re.search(r'(?<=::)\w+',line).group() #  EUtranCellFDD::pmRrcConnEstabSucc(id=266568) ebbol lesz pmRrcConnEstabSucc         
         counter_collection(counter_name,step_value)
