import sys
import cmd
import enmscripting

def read_and_print_file(filename):
    try:
        with open(filename, 'r') as file:
            session = enmscripting.open('<ENM Launcher URL>').with_credentials(enmscripting.UsernameAndPassword('<user name>','<password>'))
            for line in file:                
                command = line
                cmd = session.command()
                response = cmd.execute(command)
                for line in response.get_output():
                    print(line)
            enmscripting.close(session)

    except FileNotFoundError:
        print("File not found:", filename)
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <filename>")
    else:
        filename = sys.argv[1]
        read_and_print_file(filename)
