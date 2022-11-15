#Simple program to make difference on two files
#It checks the content and if the content not found un file then print it to result.txt
import sys

path1 = str(sys.argv[1])
path2 = str(sys.argv[2])

file1 = open(path1, 'r')
Lines = file1.readlines()
for line in Lines:
    alma = line.strip()
    file2 = open(path2, 'r')
    Lines2 = file2.readlines()
    found = 'no'
    for line in Lines2:
        korte = line.strip()
        if korte == alma:
            print(alma," found")
            found = 'yes'
    if found == 'no':
        print(alma, 'not found write to result file')
        alma = alma + '\n'
        file3 = open('/home/tnt/result.txt','a')
        file3.write(alma)
        file3.close()





