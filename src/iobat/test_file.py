import sys, os.path
from .fileclass import fileclass

def test_file(dash=False):
    infile = fileclass.name
    tester = None

    # Test if the file exists
    if(not os.path.isfile(infile)):
        fileclass.problem = True

        log = 'STOP function test_file \n'+\
            'REASON Input file not found: '+infile
        if dash:
            print(log)
        else:
            sys.exit(log)       

    fileclass.tester = tester

    #
    print('it exists')
    return 
