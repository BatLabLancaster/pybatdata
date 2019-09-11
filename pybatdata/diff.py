import os, sys
import numpy as np
from pathlib import Path
import matplotlib ; matplotlib.use('Agg')
from matplotlib import pyplot as plt

def smooth(a,WSZ):
    ''' Smooth data using a 5 points moving average
        TO IMPROVE: Use a Gaussian function instead

    Parameters
    ----------
    a: NumPy 1-D array 
       Data to be smoothed
    WSZ: Integer 
       Smoothing window size. 
       If the input is not odd, the next integer is choosen

    Returns
    -------
    return np.concatenate((  start , out0, stop  ))
    '''

    if (WSZ % 2 == 0):
        WSZ += 1
        print('WARNING in function "smooth" \n',
              '        WSZ needs to be odd, using WSZ= {}'.format(WSZ))

    out0 = np.convolve(a,np.ones(WSZ,dtype=int),'valid')/WSZ   

    r = np.arange(1,WSZ-1,2)
    start = np.cumsum(a[:WSZ-1])[::2]/r
    stop = (np.cumsum(a[:-WSZ:-1])[::2]/r)[::-1]
    
    return np.concatenate((  start , out0, stop  ))
    

# Calculate dQ/dV
################################
# Variables to be modified
smooth_perV = 2. # Smooth on voltage to increase resolution
per_bin = 0.2 # dx cointains per_bin % of the points

################################
if len(sys.argv) < 2:
    sys.exit('STOP: Give the input file as an argument in the command line')
infile = sys.argv[1]
    
# Extract the path and file name
dirname, fname = os.path.split(os.path.abspath(infile))

# Modify the slashes in the input path if needed
file_to_open = Path(dirname) / fname #; print(file_to_open)

# Count header lines
ih = 0
with open(file_to_open, 'r') as ff:
    # Check that the first character is not a digit
    line = ff.readline() ; char1 = line[0]
    if (not char1.isdigit()):
        ih += 1
#Time[h] 0,DataSet 1,t-Step[h] 2,t-Set[h] 3,Line 4,U[V] 5,I[A] 6,I[A/kg] 7,Ah[Ah/kg] 8,
#Ah-Ch[Ah/kg] 9,Ah-Dis[Ah/kg] 10,Ah-Step 11,Ah-Step[Ah/kg] 12,Wh[Wh/kg] 13,Wh-Ch[Wh/kg] 14,
#Wh-Dis[Wh/kg] 15,T1[�C] 16,dU/dt[mV/s] 17,Cyc-Count 18,Count 19,State 20,
#MEM01[�C] 21,MEM02[�C] 22,MEM03[�C] 23,MEM04[�C] 24,OCV04[mV] 25

# Read the file skipping the header
inU, inI, inAh, inOCV = np.loadtxt(file_to_open,delimiter=',',skiprows=ih, usecols=(5,7,8, 25), unpack = True)

ind = np.where(inI >0)
U = inU[ind]
Ah = inAh[ind]

# Smooth the Voltage using a window taking smooth_perV % of the data
smoothW = int(round(len(U)*smooth_perV/100.))
V = smooth(U,smoothW)

# dV using steps of per_bin
dV = (max(V)-min(V))*per_bin/100.

vbins = np.arange(min(V),max(V),dV)
v_plot = vbins[:-1] + dV*0.5

qbins = np.interp(vbins,V,Ah)

dQ = np.diff(qbins)
dQdV = dQ/dV
#print(np.shape(dQ),np.shape(v_plot))

# Plot
fig = plt.figure(figsize=(8.,9.)) ; ax = plt.subplot()
ax.set_xlabel('V(V)') ; ax.set_ylabel('dQ/DV')
##ax.set_xlim(xmin,xmax) ; ax.set_ylim(ymin,ymax)
#
ax.plot(v_plot,dQdV,marker='o')

# Save figure
outplot = 'dQdV.pdf'
plt.savefig(outplot)
print('Output: {}'.format(outplot))
    
