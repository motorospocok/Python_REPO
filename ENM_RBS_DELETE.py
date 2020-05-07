#Simple python script to execute ENM CLI commands in script server by toja
#This script uses the ENM CLI api: enmscriptiong

import enmscripting
import sys

session = enmscripting.open('<ENM Launcher URL>').with_credentials(enmscripting.UsernameAndPassword('<user name>','<password>'))
print '*********** Delete ENM Radionode by TOJA **************'

command = 'cmedit set NetworkElement=%s,PmFunction=1 pmEnabled=false'%(sys.argv[1])
terminal = session.terminal()
response = terminal.execute(command)
for line in response.get_output():
    print(line)

command = 'cmedit set NetworkElement=%s,InventorySupervision=1 active=false'%(sys.argv[1])
response = terminal.execute(command)
for line in response.get_output():
    print(line)

command = 'cmedit set NetworkElement=%s,CmNodeHeartbeatSupervision=1 active=false'%(sys.argv[1])
response = terminal.execute(command)
for line in response.get_output():
    print(line)


command = 'alarm disable %s'%(sys.argv[1])
response = terminal.execute(command)
for line in response.get_output():
    print(line)

command = 'cmedit action NetworkElement=%s,CmFunction=1 deleteNrmDataFromEnm'%(sys.argv[1])
response = terminal.execute(command)
for line in response.get_output():
    print(line)

command = 'cmedit delete NetworkElement=%s -ALL'%(sys.argv[1])
response = terminal.execute(command)
for line in response.get_output():
    print(line)
enmscripting.close(session)

