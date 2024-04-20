from tkinter import *
from tkinter.ttk import *
from tkinter import font, colorchooser, filedialog, messagebox, scrolledtext

from Editor import *

import os
import subprocess



root = Tk()
root.title("TeXer - LaTeX Code Editor")
scroll = Editor(root)
scroll.pack(expand = True, fill = "both")
scroll.text.focus()

root.grid_rowconfigure(0, weight = 1)
root.grid_columnconfigure(0, weight = 1)

root.mainloop()
