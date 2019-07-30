from pybatdata.iobat import load_files
from pybatdata.iobat import fileclass

fileclass.name = ['example_data/novonix.csv','example_data/basytec_cycling.txt','blu','None','None','blu1']

# Check if files exists, which testers they come from,
# count lines in header, and test for issues
load_files(GUI=False)

# Select analysis and loops
# Options for Cycling experiment
# Options for EIS experiments

print(fileclass.name)
