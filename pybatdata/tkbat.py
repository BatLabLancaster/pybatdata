from tkinter import filedialog
from tkinter import *

def select_files():
    # Open a tkinter GUI to select one or more files
    root = Tk()
    filez = filedialog.askopenfilenames(parent=root,title='Select files')
    allfiles = root.tk.splitlist(filez)

    iobat.fileclass.name = allfiles
    
    return

def select_analysis():
    print('in progress')
    return
    
if __name__ == "__main__":
    load_files()
