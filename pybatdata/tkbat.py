from tkinter import filedialog
import tkinter as tk
from pybatdata.iobat import fileclass


def select_files():
    # Open a tkinter GUI to select one or more files
    root = tk.Tk()
    root.withdraw() ; root.update()
    filez = tk.filedialog.askopenfilenames(parent=root,title='Select files')
    root.destroy()
    
    allfiles = list(root.tk.splitlist(filez))
    fileclass.name = allfiles
    
    return


def run_func(root,ff):
    from pybatdata.plotbat import get_func,get_params_names_defaults,wrapper

    func = get_func(ff)
    params_names,params_default = get_params_names_defaults(func)
    
    params = []
    if (len(params_names)>0):        
        top = tk.Toplevel(root)
        entries = []
        labels = []

        for ii,pp in enumerate(params_names):
            # Label
            if pp=='cycles':
                ltext = pp+' (Default='+params_default[ii]+', Format 1-2) ='
            else:
                ltext = pp+' (Default='+params_default[ii]+') ='
            tk.Label(top, text=ltext).grid(row=ii+1, column=0)

            # Entry
            en = tk.Entry(top, text=ltext)
            en.grid(row=ii+1, column=1)
            entries.append(en)

        def get_entries():
            for jj,entry in enumerate(entries):
                if not entry.get():
                    pp = params_default[ii]
                else:
                    pp = entry.get()
                params.append(pp)
            wrapper(func,params)
                
        button=tk.Button(top,text="Run",command=get_entries).grid(row=ii+2,column=0)        
    else:
        func()

    return


def select_analysis(funcs):
    root = tk.Tk()
    root.title(' Browse functions ')

    buttons = []
    for i,func in enumerate(funcs):
        b = tk.Button(root, text = func,
                      command= lambda i=i: run_func(root,funcs[i]))
        b.pack()
        buttons.append(b)

    root.mainloop()
        
    return

