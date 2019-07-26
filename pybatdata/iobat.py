import os,sys
import ntpath
import pybatdata.tkbat as tkbat
import pybatdata.constants as cte


class fileclass:
    # Pseudo-global variables
    name = None
    tester = None
    problem = False

    
def file_exists():
    # Loop over each input file
    for ii,infile in enumerate(fileclass.name):
        # Test if the file exists
        if not os.path.isfile(infile):
            print(
                "WARNING iobat.find_testers \n"
                + "REASON Input file not found: "
                + str(infile)
                + " \n"
            )
            fileclass.name[ii] = 'None'
    return


def find_testers():
    # Initialize the testers list
    fileclass.tester = ['None'] * len(fileclass.name)

    # Loop over each input file
    for ii,infile in enumerate(fileclass.name):
        if (infile == 'None'):
            continue
        
        with open(infile, "r") as ff:
            # Read the header
            for line in ff:
                tester_found = False
                if line.strip():
                    char1 = line.strip()[0]
                    if char1 in cte.numberstr:
                        for hs in cte.headstr_tester:
                            # Find the name of the input file
                            fname = ntpath.basename(infile)
                            if hs.lower() in fname.lower():
                                # Find if the tester is in the name
                                ih = cte.headstr_tester.index(hs)
                                tester = cte.testers[ih]
                                tester_found = True
                                break
                        if (tester_found): 
                            fileclass.tester[ii] = tester
                            print(
                                "WARNING! Truncated header in file \n"
                                + "       "
                                + str(infile)
                                + " \n"
                            )                        
                            break
                        else:
                            print(
                                "WARNING! Unknown tester for file \n"
                                + "       "
                                + str(infile)
                                + ", \n"
                                + "(Raise an issue in the GitHub repository)."
                            )                        
                            break
                    else:
                        for hs in cte.headstr_tester:
                            if hs.lower() in line.lower():
                                ih = cte.headstr_tester.index(hs)
                                tester = cte.testers[ih]
                                tester_found = True
                                break
                        if (tester_found): 
                            fileclass.tester[ii] = tester
                            break
    return

def load_files():
    tkbat.select_files()

    # Check that all the files exists
    file_exists()
    
    # Find the testers corresponding to each file
    find_testers()

    # Prepare and test files if needed
    print(fileclass.tester)
#    # Check if one or more files have been downloaded
#    if (len(fileclass.name) == 1):
#        type_file()

    
#def test_files():
#    if (len(allfiles)==1):
#        file1 = allfiles[0]
#    else:
#        print('Code not set to deal with multiple files')
#        
#    return 
#
#
#def test_file():
#    infile = fileclass.name
#
#    # Test if the file exists
#    if(not os.path.isfile(infile)):
#        log = 'STOP function test_file \n'+\
#            'REASON Input file not found: '+infile
#        stop_log(log,dash=dash)
#
#    else:
#        # Find cycler/tester
#        with open(infile,'r') as ff:
#            # Read first line
#            line1 = ff.readline()
#            words = line1.split()
#            if 'Basytec' in words:
#                fileclass.tester = 'Basytec'
#            elif (line1.rstrip() == "[Summary]"):
#                line2 = ff.readline()
#                device = line2.split()[0]
#                if(device == 'Novonix'):
#                    novonix_tests(dash=dash)
#                    fileclass.tester = device
#                else:
#                    log = 'STOP function test_file \n'+\
#                        'REASON unexpected header: '+infile
#                    stop_log(log,dash=dash)
#            else:
#                log = 'STOP function test_file \n'+\
#                    'REASON unknown tester: '+infile
#                stop_log(log,dash=dash)
#
#    return 
