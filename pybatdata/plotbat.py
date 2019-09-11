import sys
import ast
import inspect
from pybatdata.tkbat import select_analysis
import pybatdata.constants as cte
from pybatdata.iobat import fileclass
import pybatdata.plot_eis as eis
import pybatdata.plot_cycling as cyc

def wrapper(func, args):
    func(*args)


def top_level_functions(body):
    return (f for f in body if isinstance(f, ast.FunctionDef))


def parse_ast(filename):
    with open(filename, "rt") as file:
        return ast.parse(file.read(), filename=filename)


def get_func(func):
    exp = fileclass.experiment
        
    if (exp == cte.experiments[0]):
        func = getattr(cyc, func)
    elif (exp == cte.experiments[1]):
        func = getattr(eis, func)

    return func


def get_default_args(func):
    signature = inspect.signature(func)
    return {
        k: v.default
        for k, v in signature.parameters.items()
        if v.default is not inspect.Parameter.empty
    }
    
def analysis_options(GUI=False):
    exp = fileclass.experiment
    # Select analysis and loops
    if (exp == cte.experiments[0]):
        filename = cyc.__file__
    elif (exp == cte.experiments[1]):
        filename = eis.__file__

    funcs = []
    tree = parse_ast(filename)
    for func in top_level_functions(tree.body):
        funcs.append(func.name)
    print(funcs) 

    if GUI:
        select_analysis(funcs)
    else:
        print('\n Analysis options available for {} experiments:'.format(exp))
        print(funcs)
        s = input('Type the analysis you want to perform (or <Enter> to quit): ')
        if s:
            params = []
            
            func = get_func(s)
            params_default = get_default_args(func)
            if (len(params_default)>0):
                print('\nEnter parameters following the information:')
                ii = -1
                for pp,dict_ in params_default.items():
                    ii += 1
                    val = params_default.get(pp)
                    if val:
                        text= 'Input {} (or <Enter> to use default={}):'.format(
                                pp,val)
                        if pp=='cycles':
                            text='Input {} (or <Enter> to use default={}, Format=1-2):'.format(
                                pp,val)
                    else:
                        text= 'Input {}:'.format(pp)
                        if pp=='cycles':
                            text='Input {} (Format=1-2):'.format(pp)

                    p = input(text)
                    if not p:
                        p = val
                    params.append(p)

                wrapper(func, params)
            else:
                func()
    return
