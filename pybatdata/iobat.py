import os
import pybatdata.constants as cte

class fileclass:
    # Pseudo-global variables
    name = None # Names of files
    tester = None # Tester names
    header_nl = None # Number of lines in the header
    problem = False # Issues with the files
    experiment = None # Type of experiment

    
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


def count_header_lines():
    # Initialize the header list
    fileclass.header_nl = ['None'] * len(fileclass.name)

    # Loop over each input file
    for ii,infile in enumerate(fileclass.name):
        if (infile == 'None'):
            continue
        with open(infile, 'r', encoding='utf-8',
                  errors='replace') as ff:
            # Read the header
            il = 0
            for line in ff:
                il += 1
                if line.strip():
                    char1 = line.strip()[0]
                    if char1 in cte.numberstr:
                        break
        fileclass.header_nl[ii] = il-1
    return


def read_col_names(infile,hnl,splitter=' '):
    il = -1
    with open(infile, 'r', encoding='utf-8',
              errors='replace') as ff:
        for line in ff:
            il += 1
            if (il == hnl -1):
                break
    s = line.strip()
    
    if (s[0].isalpha()):
        s2 = s
    else:
        s2 = s[1:]

    col_names = s2.split(splitter)
        
    return col_names


def read_row_data1(infile,hnl,splitter=''):
    il = -1
    with open(infile, 'r', encoding='utf-8',
              errors='replace') as ff:
        for line in ff:
            il += 1
            if (il == hnl):
                break
    data1 = line.split(splitter)
    
    return data1

def get_column(col_name,col_units):
    col = np.zeros(3)
    return col





