#Version v1.0
#This script generates ipdatabase files for moshell
#Can be run on ENM szkript server


import enmscripting

cmd_list = ['cmedit get * CppConnectivityInformation=1 ipAddress -t -netype=ERBS','cmedit get * CppConnectivityInformation=1 ipAddress -t -netype=RBS','cmedit get * CppConnectivityInformation=1 ipAddress -t -netype=RNC','cmedit get *  ComConnectivityInformation=1 ipAddress -t -netype=RadioNode','cmedit get *  ComConnectivityInformation=1 ipAddress -t -netype=Controller6610','cmedit get * EscConnectivityInformation=1 ipAddress -t -netype=SCU']
nodes = ['#CPP LTE RBS','#CPP WCDMA RBS','#CPP WCDMA RNC','#RadioNode','#6610','#SCU']
login1 = ['-v username=','-v rcli=1,username=']
          

def connect_and_collect(cmd1,usern,passwd,nodetype,logintext):
    session = enmscripting.open('<ENM Launcher URL>').with_credentials(enmscripting.UsernameAndPassword('<user name>','<password>'))
    command = cmd1
    f = open('ipdatabase', 'a+')
    cmd = session.command()
    response = cmd.execute(command)
    f.write("%s list START\n" % (nodetype))
    for element in response.get_output().groups()[0]:
        x = str(element[0])
        y = str(element[2])
        z = x + " " + y + logintext
        print z
        f.write("%s %s %s %s,password=%s\n" % (x, y, logintext, usern, passwd))
    f.write("%s list END\n" % (nodetype))
    f.close()
    enmscripting.close(session)


def collect_all_nodes():
    cmd_list = ['cmedit get * CppConnectivityInformation=1 ipAddress -t -netype=ERBS','cmedit get * CppConnectivityInformation=1 ipAddress -t -netype=RBS','cmedit get * CppConnectivityInformation=1 ipAddress -t -netype=RNC','cmedit get *  ComConnectivityInformation=1 ipAddress -t -netype=RadioNode','cmedit get *  ComConnectivityInformation=1 ipAddress -t -netype=Controller6610','cmedit get * EscConnectivityInformation=1 ipAddress -t -netype=SCU']
    nodes = ['#CPP LTE RBS','#CPP WCDMA RBS','#CPP WCDMA RNC','#RadioNode','#6610','#SCU']
    login1 = ['-v username=','-v rcli=1,username=']
    c = 0
    for x in cmd_list:
        print('Produce IP database data for ',nodes[c])
        username = raw_input("Please give me the username ")
        psw = raw_input("Please give me the password ") 
             
        if c == 5:
            login2 = 1
        else:
            login2 = 0
        connect_and_collect(x,username,psw,nodes[c],login1[login2])
        c = c + 1

collect_all_nodes()

                    