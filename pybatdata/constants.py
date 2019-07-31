numberstr = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "-"]

testers = ['Basytec','Biologic','Novonix']
headstr_tester = ['Basytec','BT-Lab','Novonix']

experiments = ['Cycling','EIS']

# Basytec colums
basytec_time_col = 'Time[h]'   #Experimental time
basytec_v_col = 'U[V]'         #Volatge
basytec_i_col = 'I[A]'         # Current
basytec_loop_col = 'Cyc-Count' # Loop counter
basytec_line_col = 'Line'      # Protocol line
basytec_state_col = 'State'    # 0 for start of measurement,etc.

# Biologic colums
biologic_time_col = 'time/s'
biologic_v_col = 'Ecell/V'
biologic_i_col = 'I/mA'
biologic_loop_col = 'cycle number'
biologic_line_col = 'Ns changes'
biologic_state_col = 'Ns changes'
# Biologic EIS
biologic_freq_col = 'freq/Hz'
biologic_z_col = 'z cycle'

