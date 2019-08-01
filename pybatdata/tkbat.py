from tkinter import filedialog
from tkinter import *
from tkinter import messagebox
from pybatdata.iobat import fileclass

def select_files():
    # Open a tkinter GUI to select one or more files
    root = Tk()
    filez = filedialog.askopenfilenames(parent=root,title='Select files')
    allfiles = root.tk.splitlist(filez)

    fileclass.name = allfiles
    
    return


def run_func(ff):
    from pybatdata.plotbat import get_func,get_params_names_defaults,wrapper

    func = get_func(ff)
    params_names,params_default = get_params_names_defaults(func)
    
    params = []
    if (len(params_names)>0):
        top = Toplevel()
        entries = []
        labels = []

        for ii,pp in enumerate(params_names):
            # Label
            if pp=='cycles':
                ltext = pp+' (Default='+params_default+', Format 1-2) ='
            else:
                ltext = pp+' (Default='+params_default+') ='
            lt = Label(top, text=ltext).grid(row=ii+1)
            labels.append(lt)
            
            # Entry
            en = Entry(top)
            en.grid(row=ii+1, column=1)
            entries.append(en)

        def moreoptions():
            for entry in entries:
                print(entry.get())

        button=Button(root,text="Run",command=hallo).grid(row=ii+1,column=0)


        #msg = messagebox.showinfo( "Hello Python", "Hello {}".format(func))
    else:
        func()

    return


def select_analysis(funcs):
    buttons = []
    root = Tk()
    root.geometry("100x100")
    for i,func in enumerate(funcs):
        b = Button(root, text = func,
                   command= lambda i=i: run_func(funcs[i]))
        b.pack()
        buttons.append(b)
    root.mainloop()
        
    return

