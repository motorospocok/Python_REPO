import enmscripting
session = enmscripting.open('<ENM Launcher URL>').with_credentials(enmscripting.UsernameAndPassword('<user name>','<password>'))
command = 'cmedit get *  ComConnectivityInformation=1 ipAddress -t -netype=RadioNode'
f = open('ipdatabase_RadioNode', 'wb')
cmd = session.command()
response = cmd.execute(command)
for element in response.get_output().groups()[0]:
  x = str(element[0])
  y = str(element[2])
  z = x + " " + y + "-v username=rbs,password=Telekom_RBS11"
  print z
  f.write("%s %s  -v username=rbs,password=Telekom_RBS11\n" % (x, y)) 
f.close()
enmscripting.close(session)