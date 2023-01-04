#Short python script for moshell scripting support
#This file use a source file and generates echo operation for mos script
#Usage python echo_tool <sourve file> <targe file>

import sys
try:
    file1 = open(sys.argv[1], 'r')
except:
    print("Not possible to open the source file")
else:
    print("Starting operation...")
    Lines = file1.readlines()
    count = 0
    var1 = "!echo \'"
    var2 = "\' >> replace_me.txt\r"
    file2 = open(sys.argv[2], 'a')
    for line in Lines:
        count += 1
        #strip needed to remove carrige return
        var4 = str.strip(line)
        var3 = var1 + var4 + var2
        file2.write(var3)
    file2.close()
    print("...finished.")