import sys
from inspect import currentframe,getargvalues,getmembers,isfunction
from pybatdata.tkbat import select_analysis
import pybatdata.constants as cte
from pybatdata.iobat import fileclass
import pybatdata.plot_eis as eis
import pybatdata.plot_cycling as cyc

def wrapper(func, args):
    func(*args)


def get_func(func):
    exp = fileclass.experiment
        
    if (exp == cte.experiments[0]):
        func = getattr(cyc, func)
    elif (exp == cte.experiments[1]):
        func = getattr(eis, func)

    return func


def get_params_names_defaults(func):
    params_names = []
    params_default = []
    args, _, _, values = getargvalues(func) ##HERE
#    if func.__code__.co_varnames:
#        params_names = list(func.__code__.co_varnames)
#        if func.__defaults__:
#            params_default = list(func.__defaults__)
    print(args,type(args))
    #print(values,type(values),'##')
    for i in args:
        print(i,values[i])
    sys.exit()
    return params_names,params_default

    
def analysis_options(GUI=False):
    exp = fileclass.experiment
    
    # Select analysis and loops
    if (exp == cte.experiments[0]):
        funcs_tup = getmembers(cyc,isfunction)
    elif (exp == cte.experiments[1]):
        funcs_tup = getmembers(eis,isfunction)

    funcs = [i[0] for i in funcs_tup]

    if GUI:
        select_analysis(funcs)
    else:
        print('\n Analysis options available for {} experiments:'.format(exp))
        print(funcs)
        s = input('Type the analysis you want to perform (or <Enter> to quit): ')
        if s:
            func = get_func(s)
            params_names, params_default = get_params_names_defaults(func)

            params = []
            if (len(params_names)>0):
                print('\nEnter parameters following the information:')
                for ii, pp in enumerate(params_names):
                    if params_default:
                        text= 'Input {} (or <Enter> to use default={}):'.format(
                                pp,params_default[ii])
                        if pp=='cycles':
                            text='Input {} (or <Enter> to use default={}, Format=1-2):'.format(
                                pp,params_default[ii])
                    else:
                        text= 'Input {}:'.format(pp)
                        if pp=='cycles':
                            text='Input {} (Format=1-2):'.format(pp)

                    p = input(text)
                    if not p:
                        p = params_default[ii]
                    params.append(pp+'='+p)
                wrapper(func, params)
            else:
                func()
    return
