import sys, os
from pathlib import Path
from ..dashsetup.mylayouts import reportHTML

def test_file(infile):
    problem = False
    tester = None

    # Extract the path and file name
    dirname, fname = os.path.split(os.path.abspath(infile))

    # Modify the slashes in the input path if needed
    file_to_open = Path(dirname) / fname #; print(file_to_open)

    # Test if the file exists
    if(not os.path.isfile(file_to_open)):
        problem = True

        reportHTML('STOP function test_file \n'+\
                   'REASON Input file not found: '+str(infile))       

    return problem,tester
