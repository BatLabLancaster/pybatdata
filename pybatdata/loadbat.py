import os,sys
import ntpath
import pybatdata.tkbat as tkbat
import pybatdata.constants as cte
from pybatdata.iobat import fileclass
import pybatdata.iobat as iobat
from pybatdata.iobiologic import prep_biologic
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
        exp = cte.experiments[0]

        s = cte.separators[cte.testers.index(tester)]

        col_names = iobat.read_col_names(fileclass.name[ii],
                                         fileclass.header_nl[ii],
                                         splitter=s)
        col = cte.freq_col(tester)
        if (col in col_names):
            exp = cte.experiments[1]

        fileclass.experiment[ii] = exp

    return


def prep_files():
    # Loop over each input file
    for ii,infile in enumerate(fileclass.name):
        print('\n * Preparing: {}'.format(infile))
        problem = False
        if (infile == 'None' or fileclass.header_nl[ii] < 2):
            continue
        
        # Tester
        tester = fileclass.tester[ii]
        
        # Extra file preparation if needed
        if(tester == cte.testers[1]):
            try:
                prep_biologic(infile,fileclass.header_nl[ii],
                              fileclass.experiment[ii],zcycle=True,
                              overwrite=False,verbose=True)
                #fileclass.name[ii] = after_file_name(infile) ## TO EXPAND
                problem = False
            except:
                problem = True
        elif(tester == cte.testers[2]):
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


def check_files():
    # Loop over each input file
    for ii,infile in enumerate(fileclass.name):
        problem = False
        print('\n * Checking: {}'.format(infile))
        if (infile == 'None' or fileclass.header_nl[ii] < 2):
            continue

        # Tester
        tester = fileclass.tester[ii]
        s = cte.separators[cte.testers.index(tester)]

        # Read the column names
        col_names = iobat.read_col_names(fileclass.name[ii],
                                         fileclass.header_nl[ii],
                                         splitter=s)

        # Read the first row with data
        data1 = iobat.read_row_data1(fileclass.name[ii],
                                     fileclass.header_nl[ii],
                                     splitter=s)

        # The columns in the header should match the data
        if (len(col_names) != len(data1)):
            print('WARNING from loadbat \n',
                  'Columns in header={}, Data columns= {} in file:\n {}'.format(
                      len(col_names),len(data1),infile))
            return True

        # The column header should contain some fundamental columns
        if (fileclass.experiment[0] == cte.experiments[0]):
            cols = [cte.time_col(tester), cte.v_col(tester),
                    cte.i_col(tester), cte.loop_col(tester),
                    cte.state_col(tester)]
        elif (fileclass.experiment[0] == cte.experiments[1]):
            cols = [cte.time_col(tester), cte.freq_col(tester),
                    cte.Re_col(tester),cte.Im_col(tester)]

        for col in cols:
            if (col not in col_names):
                print('WARNING from loadbat, file: \n',
                      infile,'\n',
                      'does not contain column ',col)
                return True

        fileclass.problem[ii] = problem
    return

    
def load_files(GUI=False):
    if GUI:
        tkbat.select_files()

    # Check that all the files exists
    iobat.file_exists()
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
    iobat.count_header_lines()

    # Type of experiment (Cycling,EIS)
    type_experiment()

    # Initialize the list of problems
    fileclass.problem = [False] * len(fileclass.name)

    # Prepare files if needed
    prep_files()
    
    # Check files 
    check_files()
    # Remove files with problems
    nind = fileclass.problem.count(True)
    for ic in range(nind):
        ii = fileclass.problem.index(True)        
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
