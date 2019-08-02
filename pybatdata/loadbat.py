import os,sys
import ntpath
import pybatdata.tkbat as tkbat
import pybatdata.constants as cte
from pybatdata.iobat import fileclass, file_exists,count_header_lines
from pybatdata.iobasytec import check_basytec
from pybatdata.iobiologic import check_biologic, biologic_experiment
import preparenovonix.novonix_prep as prep
from preparenovonix.novonix_io import after_file_name

   
def checkequal(lst):
    return lst[1:] == lst[:-1]


def find_testers():
    # Initialize the testers list
    fileclass.tester = ['None'] * len(fileclass.name)

    # Loop over each input file
    for ii,infile in enumerate(fileclass.name):
        if (infile == 'None'):
            continue

        with open(infile, 'r', encoding='utf-8',
                  errors='replace') as ff:
            # Read the header
            for line in ff:
                tester_found = False ; tester = 'None'
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
                                print(tester_found,tester)
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


def type_experiment():
    # Initialize the type of experiment list
    fileclass.experiment = [cte.experiments[0]] * len(fileclass.name)

    # Loop over each input file
    for ii,tester in enumerate(fileclass.tester):
        if (tester == cte.testers[1]):
            exp = biologic_experiment(fileclass.name[ii],
                                      fileclass.header_nl[ii])
            fileclass.experiment[ii] = exp

    return


def check_files():
    # Initialize the list of problems
    fileclass.problem = [False] * len(fileclass.name)

    # Loop over each input file
    for ii,infile in enumerate(fileclass.name):
        print('\n * Checking: {} \n'.format(infile))
        if (infile == 'None' or fileclass.header_nl[ii] < 2):
            continue
        if(fileclass.tester[ii] == cte.testers[0]):
            problem = check_basytec(infile,fileclass.header_nl[ii])
        elif(fileclass.tester[ii] == cte.testers[1]):
            problem = check_biologic(infile,fileclass.header_nl[ii],
                                     fileclass.experiment[ii])
        elif(fileclass.tester[ii] == cte.testers[2]):
            infile = fileclass.name[ii]
            try:
                prep.prepare_novonix(infile, addstate=True, lprotocol=True,
                                overwrite=False, verbose=True)
                fileclass.name[ii] = after_file_name(infile)
                problem = False
            except:
                problem = True
        fileclass.problem[ii] = problem
    return

    
def load_files(GUI=False):
    if GUI:
        tkbat.select_files()

    # Check that all the files exists
    file_exists()
    # Remove files that do not exist
    nind = fileclass.name.count('None')
    for ic in range(nind):
        ii = fileclass.name.index('None')
        fileclass.name.pop(ii)

    # Find the testers corresponding to each file
    find_testers()
    # Remove files without a recognised tester
    nind = fileclass.tester.count('None')
    for ic in range(nind):
        ii = fileclass.tester.index('None')
        fileclass.name.pop(ii)
        fileclass.tester.pop(ii)

    # Count header lines
    count_header_lines()

    # Type of experiment (Cycling,EIS)
    type_experiment()
    
    # Test and prepare files if needed
    check_files()
    # Remove files with problems
    nind = fileclass.problem.count(True)
    for ic in range(nind):
        ii = fileclass.problem.index(True)
        print(type(fileclass.name),fileclass.name);sys.exit() #HERE
        fileclass.name.pop(ii)
        fileclass.tester.pop(ii)
        fileclass.header_nl.pop(ii)
        fileclass.problem.pop(ii)

    # Check that all the considered files correspond to
    # the same type of experiment
    answer = checkequal(fileclass.experiment)
    if answer:
        experiment = fileclass.experiment[0]
        fileclass.experiment = experiment
    else:
        print('\n STOP! input files \n',
              fileclass.name,
              '\n correspond to different type of experiments \n')
        sys.exit()

    return 
