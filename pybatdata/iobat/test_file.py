import os.path
from .fileclass import fileclass
from .logs import stop_log
from .novonix import novonix_tests

def test_file(dash=False):
    infile = fileclass.name

    # Test if the file exists
    if(not os.path.isfile(infile)):
        log = 'STOP function test_file \n'+\
            'REASON Input file not found: '+infile
        stop_log(log,dash=dash)

    else:
        # Find cycler/tester
        with open(infile,'r') as ff:
            # Read first line
            line1 = ff.readline()
            words = line1.split()
            if 'Basytec' in words:
                fileclass.tester = 'Basytec'
            elif (line1.rstrip() == "[Summary]"):
                line2 = ff.readline()
                device = line2.split()[0]
                if(device == 'Novonix'):
                    novonix_tests(dash=dash)
                    fileclass.tester = device
                else:
                    log = 'STOP function test_file \n'+\
                        'REASON unexpected header: '+infile
                    stop_log(log,dash=dash)
            else:
                log = 'STOP function test_file \n'+\
                    'REASON unknown tester: '+infile
                stop_log(log,dash=dash)

    return 
