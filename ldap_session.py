import cmd
import enmscripting
import sys
import os
if len(sys.argv) < 2:
    print("Please give the node name")
else:
    file_name = sys.argv[1] + "_ldap.txt"
    f = open(file_name, 'a+')
    f.write(sys.argv[1] + " node ldap session file\n")
    session = enmscripting.open('<ENM Launcher URL>').with_credentials(enmscripting.UsernameAndPassword('<user name>','<password>'))
    command = 'secadm ldap configure --manual'
    cmd = session.command()
    response = cmd.execute(command)
    for element in response.get_output().groups()[0]:
        x = str(element[0])
        y = str(element[1])
        output_str = x + " " + y
        print output_str
        f.write(output_str + "\n")
    f.write("Operation_completed_successfully\n")
    f.close()
    enmscripting.close(session)



