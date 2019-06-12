import sys, os
from pathlib import Path
from src.iobat.fileclass import fileclass
from src.iobat.test_file import test_file

#inpath = sys.argv[1]
#inpath = "C:/Users/gonzalev/Documents/batdata/novonix_data/Cell10_100.csv"
inpath = "C:/Users/gonzalev/Documents/batdata/basytec_data/BaSyTec_Delta_InnovateUK_Samsung_48X_395_Cycling_LUv1_4V2_2V5_4A_50cyc.txt"

#######################################

# Extract the path and file name
dirname, fname = os.path.split(os.path.abspath(inpath))

# Modify the slashes in the input path if needed
file_to_open = Path(dirname) / fname #; print(file_to_open)

filename = inpath
fileclass.name = str(filename)

test_file()
