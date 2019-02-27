import sys
from .fileclass import fileclass

def stop_log(log,dash=False):
    # Stop the program with a message and
    # set the problem attribute of the file to True

    fileclass.problem = True
    if dash:
        print(log)
    else:
        sys.exit(log)       

    return
    
