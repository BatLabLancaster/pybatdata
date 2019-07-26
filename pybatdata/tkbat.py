from tkinter import filedialog
from tkinter import *
import pybatdata.iobat as iobat

def select_files():
    # Open a tkinter GUI to select one or more files
    root = Tk()
    filez = filedialog.askopenfilenames(parent=root,title='Select files')
    allfiles = root.tk.splitlist(filez)

    iobat.fileclass.name = allfiles
    
    return

if __name__ == "__main__":
    load_files()
