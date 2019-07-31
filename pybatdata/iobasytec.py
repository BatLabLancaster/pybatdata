import sys
import numpy as np
import pybatdata.constants as cte
import pybatdata.iobat as io
    
def check_basytec(infile,hnl):
    problem = False
    
    # Read the column names
    col_names = io.read_col_names(infile,hnl,splitter=' ')

    # Read the first row with data
    data1 = io.read_row_data1(infile,hnl,splitter=' ')
    print(data1) ; sys.exit()
    # The columns in the header should match the data
    if (len(col_names) != len(data1)):
        print('WARNING from iobasytec \n',
              'Columns in header do not match data for file\n',
              infile)
        return True

    # The column header should contain some fundamental columns
    cols = [cte.basytec_time_col, cte.basytec_v_col,
            cte.basytec_i_col, cte.basytec_loop_col,
            cte.basytec_state_col]
    for col in cols:
        if (col not in col_names):
            print('WARNING from iobasytec, file: \n',
                  infile,'\n',
                  'does not contain column ',col)
            return True

    return problem
