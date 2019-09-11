from pybatdata.loadbat import load_files
from pybatdata.plotbat import analysis_options

# Check if files exists, which testers they come from,
# count lines in header, and test for issues
load_files(GUI=True)

# Show analysis options and select
analysis_options(GUI=True)
