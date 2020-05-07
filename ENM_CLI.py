#Simple python script to execute ENM CLI commands in script server by toja
#This script uses the ENM CLI api: enmscriptiong

import enmscripting
import sys

session = enmscripting.open('<ENM Launcher URL>').with_credentials(enmscripting.UsernameAndPassword('<user name>','<password>'))
print '*********** ENM CLI by Toja **************'
parancs = raw_input("Enter ENM CLI command ")
print parancs
command = parancs
print command
terminal = session.terminal()
response = terminal.execute(command)
for line in response.get_output():
    print(line)
enmscripting.close(session)
