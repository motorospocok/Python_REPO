#This script creates Ipdatabase file for RadioNode elements
#User and psw is taken by secadm command so, make sure that you have privileges to execute these commands in ENM\

import enmscripting

f = open('ipdatabase', 'a+')

#Creating empty arrays for the data
ne_name = []
ne_ip = []
ne_user = []
ne_psw = []

session = enmscripting.open('<ENM Launcher URL>').with_credentials(enmscripting.UsernameAndPassword('<user name>','<password>'))
command = 'cmedit get *  ComConnectivityInformation=1 ipAddress -t -netype=RadioNode'
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
