from pybatdata.loadbat import load_files
from pybatdata.plotbat import analysis_options
from pybatdata.iobat import fileclass
from pybatdata.plot_cycling import V_I_time

fileclass.name = ['example_data/basytec_cycling.txt','example_data/biologic_cycling.mpt','example_data/novonix.csv']

#fileclass.name = ['/home/violeta/BatLab/batdata/biologic/Cell78_zycle_missing.mpt','/home/violeta/BatLab/batdata/biologic/Cell99_100SOC_0mon_CA1.mpt','/home/violeta/BatLab/batdata/biologic/Cell75_GEIS_10SOC_-5degC_CA2.mpt']

#fileclass.name = ['/home/violeta/BatLab/batdata/biologic/Cell75_GEIS_10SOC_-5degC_CA2.mpt']

# Check if files exists, which testers they come from,
# count lines in header, and test for issues
load_files(GUI=False)

# Show analysis options and select
analysis_options(GUI=False)

# Or directly call the function you are interested in
#V_I_time()
    
