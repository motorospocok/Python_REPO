# This script collect the manual ldap session data from ENM
# When completed MOS script called fetch_ldap.mos must be run the RadioNode
import enmscripting
session = enmscripting.open('<ENM Launcher URL>').with_credentials(enmscripting.UsernameAndPassword('<user name>','<password>'))
f = open('ldap.txt', 'wb')
command = 'secadm ldap configure --manual'
cmd = session.command()
response = cmd.execute(command)
for element in response.get_output().groups()[0]:
  x = str(element[0])
  y = str(element[1])
  if x in ['bindDn']:
   print('---------------')
   print y
   f.write("%s\n" % (y))
  if x in ['bindPassword']:
   print('---------------')
   print y
   f.write("%s\n" % (y))
f.close()
enmscripting.close(session)

