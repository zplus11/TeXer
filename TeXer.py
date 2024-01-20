from tkinter import *
from tkinter.ttk import *
from tkinter import font, colorchooser, filedialog, messagebox, scrolledtext

from ScrollText import *

import os
import subprocess



if __name__ == '__main__':
    root = Tk()
    scroll = ScrollText(root)
    scroll.pack(expand = True, fill = "both")
    scroll.text.focus()
    
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

    root.mainloop()
