import enmscripting
session = enmscripting.open('<ENM Launcher URL>').with_credentials(enmscripting.UsernameAndPassword('<user name>','<password>'))
command = 'cmedit get * CppConnectivityInformation=1 ipAddress -t -netype=ERBS'
f = open('ipdatabase', 'wb')
cmd = session.command()
f.write("#CPP LTE RBS section START\n")
response = cmd.execute(command)
for element in response.get_output().groups()[0]:
  x = str(element[0])
  y = str(element[2])
  z = x + " " + y + "-v username=rbs,password=Telekom_RBS11"
  print z
  f.write("%s %s -v username=rbs,password=Telekom_RBS11\n" % (x, y))
f.write("#CPP LTE RBS section END\n")
f.write("#CPP WCDMA RBS section START\n")
command = 'cmedit get * CppConnectivityInformation=1 ipAddress -t -netype=RBS'
cmd = session.command()
response = cmd.execute(command)
for element in response.get_output().groups()[0]:
  x = str(element[0])
  y = str(element[2])
  z = x + " " + y + "-v username=rbs,password=Telekom_RBS11"
  print z
  f.write("%s %s -v username=rbs,password=Telekom_RBS11\n" % (x, y))
f.write("#CPP WCDMA RBS section END\n")
f.write("#CPP WCDMA RNC section START\n")
command = 'cmedit get * CppConnectivityInformation=1 ipAddress -t -netype=RNC'
cmd = session.command()
response = cmd.execute(command)
for element in response.get_output().groups()[0]:
  x = str(element[0])
  y = str(element[2])
  z = x + " " + y + "-v username=rnc,password=rnc"
  print z
  f.write("%s %s -v username=rbs,password=rnc\n" % (x, y))
f.write("#CPP WCDMA RNC section END\n")
f.write("#RadioNode Section START\n")
command = 'cmedit get *  ComConnectivityInformation=1 ipAddress -t -netype=RadioNode'
cmd = session.command()
response = cmd.execute(command)
for element in response.get_output().groups()[0]:
  x = str(element[0])
  y = str(element[2])
  z = x + " " + y + "-v username=rbs,password=Telekom_RBS11"
  print z
  f.write("%s %s -v username=rbs,password=Telekom_RBS11\n" % (x, y))
f.write("#RadioNode Section END\n")
f.write("#SCU Section START\n")
command = 'cmedit get * EscConnectivityInformation=1 ipAddress -t -netype=SCU'
cmd = session.command()
response = cmd.execute(command)
for element in response.get_output().groups()[0]:
  x = str(element[0])
  y = str(element[2])
  z = x + " " + y + "-v rcli=1,username=oss,password=default"
  print z
  f.write("%s %s -v rcli=1,username=oss,password=default\n" % (x, y))
f.write("#SCU Section END\n")
f.close()
enmscripting.close(session)