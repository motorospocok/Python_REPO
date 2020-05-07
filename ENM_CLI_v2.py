import cmd
import enmscripting
import sys


class ENM_Cli(cmd.Cmd):
    """Toja Programozik es rombol. V0.1"""
    fileHandler = open ("data.txt", "r")
    cmedit_opt = fileHandler.read().splitlines()
    fileHandler.close()  
    fileHandler = open ("cmedit_get_collection.txt", "r")
    cmedit_collection = fileHandler.read().splitlines()
    fileHandler.close()      
    intro = 'Hello Te kis buzi.   Ird be help vagy ? hogy skubizd a parancsokat.\n'
    prompt = '(Magnum Szauna) '

    def do_cmedit(self, variable1):
        "ENM CLI cmedit parancs te pondro, ha ennyit se tudsz szopjal falovat"
        if variable1 and variable1 in self.cmedit_opt:
            command = 'cmedit %s!' % variable1
        elif variable1:
            command = "cmedit " + variable1
        else:
            command = 'hello baby'
        print(command)
        session = enmscripting.open('<ENM Launcher URL>').with_credentials(enmscripting.UsernameAndPassword('<user name>','<password>'))
        terminal = session.terminal()
        response = terminal.execute(command)
        for line in response.get_output():
          print(line)
        enmscripting.close(session)
        
    def do_secadm(self, variable1):
        "ENM CLI secadm parancs te feregnovendek, Te sivatagi hollokutya teee"
        if variable1 and variable1 in self.cmedit_opt:
            command = 'secadm %s!' % variable1
        elif variable1:
            command = "secadm " + variable1
        else:
            command = 'hello baby'
        print(command)
        session = enmscripting.open('<ENM Launcher URL>').with_credentials(enmscripting.UsernameAndPassword('<user name>','<password>'))
        terminal = session.terminal()
        response = terminal.execute(command)
        for line in response.get_output():
          print(line)
        enmscripting.close(session)
        
    def complete_cmedit(self, text, line, begidx, endidx):
        if not text:
            completions = self.cmedit_opt[:]
        else:
            completions = [ f
                            for f in self.cmedit_opt
                            if f.startswith(text)
                            ]
        return completions
        
    def do_MozoKedvence(self, variable1):
        "Elore definialt ENM CLI parancsok a'la cmedit"
        if variable1 and variable1 in self.cmedit_collection:
            command = '%s' % variable1
        elif variable1:
            command = variable1
        else:
            command = 'hello baby'
        print(command)
        command = command[0: 0:] + command[3::]
        print(command)
        session = enmscripting.open('<ENM Launcher URL>').with_credentials(enmscripting.UsernameAndPassword('<user name>','<password>'))
        terminal = session.terminal()
        response = terminal.execute(command)
        for line in response.get_output():
          print(line)
        enmscripting.close(session)


    def complete_MozoKedvence(self, text, line, begidx, endidx):
        if not text:
            completions = self.cmedit_collection[:]
        else:
            completions = [ f
                            for f in self.cmedit_collection
                            if f.startswith(text)
                            ]
        return completions
    
    def do_KilepekBusPicsaba(self, line):
        "Kilpesz a programbol te Sivatagi Hollo Kutya"
        print()
        print("*******************************************")
        print("Tartsd meg az aprot, te mocskos A L L A T !")
        print("*******************************************")
        print()
        return True
        
    def do_kilepekBusPicsaba(self, line):
        "Kilpesz a programbol te Sivatagi Hollo Kutya"
        print()
        print("*******************************************")
        print("Tartsd meg az aprot, te mocskos A L L A T !")
        print("*******************************************")
        print()
        return True
if __name__ == '__main__':
    ENM_Cli().cmdloop()