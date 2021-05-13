#Simple python script to execute ENM CLI commands in script server by toja
#This script uses the ENM CLI api: enmscriptiong
#Usage python enable_NE.py <NE_NAME>

import enmscripting
import sys

session = enmscripting.open('<ENM Launcher URL>').with_credentials(enmscripting.UsernameAndPassword('<user name>','<password>'))
print '*********** Enable ENM Radionode by TOJA **************'

command = 'cmedit set NetworkElement=%s,PmFunction=1 pmEnabled=true'%(sys.argv[1])
terminal = session.terminal()
response = terminal.execute(command)
for line in response.get_output():
    print(line)

command = 'cmedit set NetworkElement=%s,InventorySupervision=1 active=true'%(sys.argv[1])
response = terminal.execute(command)
for line in response.get_output():
    print(line)

command = 'cmedit set NetworkElement=%s,CmNodeHeartbeatSupervision=1 active=true'%(sys.argv[1])
response = terminal.execute(command)
for line in response.get_output():
    print(line)


command = 'alarm enable %s'%(sys.argv[1])
response = terminal.execute(command)
for line in response.get_output():
    print(line)

enmscripting.close(session)
