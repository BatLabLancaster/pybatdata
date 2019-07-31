import sys
import numpy as np
import pybatdata.constants as cte
import pandas as pd

def biologic_experiment(infile,hnl):
    from pybatdata.iobat import read_col_names

    experiment = cte.experiments[0]

    col_names = read_col_names(infile,hnl,splitter='\t')
    if (cte.biologic_freq_col in col_names):
        experiment = cte.experiments[1]

    return experiment


def check_biologic(infile,hnl,experiment):
    from pybatdata.iobat import read_col_names,read_row_data1
    problem = False

    # Read the column names
    col_names = read_col_names(infile,hnl,splitter='\t')

    # Read the first row with data
    data1 = read_row_data1(infile,hnl,splitter='\t')

    # The columns in the header should match the data
    if (len(col_names) != len(data1)):
        print('WARNING from iobiologic \n',
              'Columns in header={}, Data columns= {} in file:\n {}'.format(
                  len(col_names),len(data1),infile))
        return True

    # The column header should contain some fundamental columns
    if (experiment == cte.experiments[0]):
        cols = [cte.biologic_time_col, cte.biologic_v_col,
                cte.biologic_i_col, cte.biologic_loop_col,
                cte.biologic_state_col]
    elif (experiment == cte.experiments[1]):
        cols = [cte.biologic_time_col, cte.biologic_v_col,
                cte.biologic_freq_col, cte.biologic_z_col]
    print(col_names,'### \n')
    for col in cols:
        if (col not in col_names):
            print('WARNING from iobiologic, file: \n',
                  infile,'\n',
                  'does not contain column ',col)
            return True
        

    return problem
