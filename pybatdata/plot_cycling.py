import sys
import numpy as np
import matplotlib.pyplot as plt
import pybatdata.constants as cte
from pybatdata.iobat import fileclass, get_column

def V_I_time(cycles='All',units_v='A',units_i='V',units_t='h'):
    # Find which loops to plot
    if (cycles == 'All'):
        plotall = True
    else:
        plotall = False
        first_loop = int(cycles.split('-')[0])
        last_loop = int(cycles.split('-')[1])

    # Prepare plot
    #plt.figure(figsize=(8.0, 11.0))
    fs = 15
    fig, axv = plt.subplots()
    axv.set_xlabel('Time/'+units_t, fontsize=fs)
    axv.set_ylabel('Voltage/'+units_v, fontsize=fs)
    axc = axv.twinx()
    axc.set_ylabel('Capacity/'+units_i, fontsize=fs)
        
    # Get columns
    for ii,ff in enumerate(fileclass.name):
        hnl = fileclass.header_nl[ii]
        tester = fileclass.tester[ii]
        s = cte.separators[cte.testers.index(tester)]

        v_col = get_column(ff,hnl,cte.v_col(tester),splitter=s,outtype='float')
        i_col = get_column(ff,hnl,cte.i_col(tester),splitter=s,outtype='float')
        t_col = get_column(ff,hnl,cte.time_col(tester),splitter=s,outtype='float')

        if (not plotall):
            l_col = get_column(ff,hnl,cte.loop_col(tester),splitter=s,outtype='int')
            ind = np.where((l_col >= first_loop) & (l_col <= last_loop))
            xx = t_col[ind]
            y1 = v_col[ind]
            y2 = i_col[ind]
        else:
            xx = t_col
            y1 = v_col
            y2 = i_col

        # Plot voltage and current vs. time
        axv.plot(xx,y1, linewidth=2.5, label=ff)
        axc.plot(xx,y2, linewidth=2.5, label=ff)


    leg = axc.legend(loc=4, fontsize=fs - 2)
    leg.draw_frame(False)

    #plt.savefig(figname)
    #print("Plot: {}".format(figname))
    plt.show()

    return


def DVA():
    print('Work in progress')
    return
