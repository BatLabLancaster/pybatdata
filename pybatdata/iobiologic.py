import sys
import numpy as np
import pybatdata.constants as cte
import pandas as pd
    
def prep_biologic(infile,hnl,experiment,zcycle=True,overwrite=False,verbose=True):

    # Recreate the z cycle column if needed
    if (experiment == cte.experiments[1] and
        cte.biologic_z_col not in col_names):
        print('Work in progress')

    return 
