try:
    import enmscripting
    print("-------------------------------------------------")
    print("It seems you are in the right server")
    print("-------------------------------------------------")
except ImportError:
    print("-----------------------------------------------------------------------")
    print("This server has no ENM API, NOT OK for ENM python script operations")
    print("-----------------------------------------------------------------------")
