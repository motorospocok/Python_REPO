import enmscripting
import sys

f = open('ipdatabase', 'a+')


#Creating empty arrays for the data
ne_name = []
ne_ip = []
ne_user = []
ne_psw = []
found = 0
option = ''

def determine_nodetype():
    print('It seems no valid or missing option is given in the command line')
    print('Supported node types:')
    print('1. RadioNode')
    print('2. PowerController6610')
    print(' ')
    selection = raw_input('Please make your choice: ')
    if selection == "1":
      option1 = 'RadioNode'      
      return option1 
      found = 1
    if selection == "2":      
      print(option1)
      return option1
            
if len(sys.argv) < 2:
    option = determine_nodetype() 
else:
    option =  sys.argv[1]
    
if "RadioNode" in option or "radionode" in option or "rd" in option or "RD" in option:
    option = 'RadioNode'
    found = 1
if "6610" in option:
    option = 'Controller6610'
    found = 1

if found == 0:
    option = determine_nodetype()
    
session = enmscripting.open('<ENM Launcher URL>').with_credentials(enmscripting.UsernameAndPassword('<user name>','<password>'))
command = 'cmedit get *  ComConnectivityInformation=1 ipAddress -t -netype=' + option
cmd = session.command()
response = cmd.execute(command)
for element in response.get_output().groups()[0]:
    x = str(element[0])
    ne_name.append(x)
    y = str(element[2])
    ne_ip.append(y)
ne_list = ''
for ne_name1 in ne_name:
    ne_list += 'NetworkElement=' + ne_name1 + ','
ne_list = ne_list[:-1]
command = 'secadm credentials get --plaintext show --nodelist ' + ne_list
cmd = session.command()
response = cmd.execute(command)
for element in response.get_output().groups()[0]:
    x = str(element[0])
    y = str(element[1])
    z = str(element[2])
    if "secureUserName" in y:
        y1,y2 = y.split(":")
        z1,z2 = z.split(":")
        ne_user.append(y2)
        ne_psw.append(z2)

for ne_name1,ne_ip1,ne_user1,ne_psw1 in zip(ne_name,ne_ip,ne_user,ne_psw):
    str1 = ne_name1 + ' ' + ne_ip1 + ' ' + '-v username=' + ne_user1 + ',password=' + ne_psw1 + '\n'
    f.write(str1)
f.close()
enmscripting.close(session)

