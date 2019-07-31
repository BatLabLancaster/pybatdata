from pybatdata.loadbat import load_files
from pybatdata.iobat import fileclass

fileclass.name = ['example_data/basytec_cycling.txt','example_data/biologic_cycling.mpt','example_data/novonix.csv']

#fileclass.name = ['/home/violeta/BatLab/batdata/biologic/Cell78_zycle_missing.mpt','/home/violeta/BatLab/batdata/biologic/Cell99_100SOC_0mon_CA1.mpt']

# Check if files exists, which testers they come from,
# count lines in header, and test for issues
load_files(GUI=False)

# Select analysis and loops
# Options for Cycling experiment
# Options for EIS experiments
#print('WARNING program not set to deal with EIS experiments yet')
print(fileclass.experiment)
