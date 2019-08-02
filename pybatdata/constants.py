numberstr = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "-"]

testers = ['Basytec','Biologic','Novonix']
headstr_tester = ['Basytec','BT-Lab','Novonix']
separators = [' ','\t',',']

experiments = ['Cycling','EIS']

class Columns:
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
    biologic_Re_col = 'Re(Z)/Ohm'
    biologic_Im_col = '-Im(Z)/Ohm'
    biologic_z_col = 'z cycle'

    # Novonix columns
    novonix_time_col = 'Step Time (h)'
    novonix_v_col = 'Potential (V)'
    novonix_i_col = 'Current (A)'
    novonix_loop_col = 'Loop number'
    novonix_line_col = 'Protocol Line (it refers to the reduced protocol)'
    novonix_state_col = 'State (0=Start 1=Regular 2=End -1=Single Measurement)'


def time_col(tester):
    ii = testers.index(tester)
    var_name = testers[ii].lower()+'_time_col'
    return getattr(Columns,var_name,'None')


def v_col(tester):
    ii = testers.index(tester)
    var_name = testers[ii].lower()+'_v_col'
    return getattr(Columns,var_name,'None')


def i_col(tester):
    ii = testers.index(tester)
    var_name = testers[ii].lower()+'_i_col'
    return getattr(Columns,var_name,'None')


def loop_col(tester):
    ii = testers.index(tester)
    var_name = testers[ii].lower()+'_loop_col'
    return getattr(Columns,var_name,'None')


def line_col(tester):
    ii = testers.index(tester)
    var_name = testers[ii].lower()+'_line_col'
    return getattr(Columns,var_name,'None')


def state_col(tester):
    ii = testers.index(tester)
    var_name = testers[ii].lower()+'_state_col'
    return getattr(Columns,var_name,'None')


def freq_col(tester):
    ii = testers.index(tester)
    var_name = testers[ii].lower()+'_freq_col'
    return getattr(Columns,var_name,'None')


def Re_col(tester):
    ii = testers.index(tester)
    var_name = testers[ii].lower()+'_Re_col'
    return getattr(Columns,var_name,'None')


def Im_col(tester):
    ii = testers.index(tester)
    var_name = testers[ii].lower()+'_Im_col'
    return getattr(Columns,var_name,'None')


def z_col(tester):
    ii = testers.index(tester)
    var_name = testers[ii].lower()+'_z_col'
    return getattr(Columns,var_name,'None')
