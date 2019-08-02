import sys
import matplotlib.pyplot as plt
from pybatdata.iobat import fileclass

def V_I_time(cycles='All',units_v='A',units_i='V',units_t='h'):
    
    for ff in fileclass.name:
        print(ff)
        v_col = get_column('v_col',units_v)
        i_col = get_column('i_col',units_i)
        t_col = get_column('v_col',units_t)
    
    return

def DVA():
    print('Work in progress')
    return
