import re
import sys
for line in sys.stdin:
 line=line.rstrip()
 if bool(re.search('Music',line)) == True:
  alma = line.split(' ')
  print (alma[0],'-',alma[15])
 if bool(re.search('snap',line)) == True:
  alma = line.split(' ')
  print (alma[1],'-',alma[14])

