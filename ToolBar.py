from tkinter import *
from tkinter.ttk import *
from tkinter import font, colorchooser, filedialog, messagebox, scrolledtext

import subprocess
import os


class ToolBar(Frame):
    def __init__(self, master, text_widget, menu_bar,  *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self.text_widget = text_widget
        self.menu_bar = menu_bar
        self.compiler_choice = StringVar()
        self.compiler_image = PhotoImage(file = r"assets\images\compile.png")
        
        tool_bar = Label(master)
        tool_bar.pack(side = TOP, fill = X)
        compiling_box = Combobox(tool_bar, width = 20, values = ("pdflatex", "lualatex", "pdflatex + biber", "lualatex + biber"), state = "readonly", textvariable = self.compiler_choice)
        compiling_box.current(0)
        compiling_box.grid(row = 0, column = 0)
        compiling_box.bind("<<ComboboxSelected>>", self.set_compiler)
        
        compile_button = Button(tool_bar, image = self.compiler_image, command = self.run_compiler)
        compile_button.grid(row = 0, column = 1)

    def run_compiler(self):
        global choice
    
        choice = self.compiler_choice.get()
        lop = ["pdflatex"]
        if choice in ["pdflatex", "lualatex"]:
            lop = [choice]
        elif choice in ["pdflatex + biber", "lualatex + biber"]:
            lop = [choice.split(" ")[i] for i in [0, 2]]
        url = self.menu_bar.url
        url_split = url.split("/")
        wd = "/".join(url_split[:-1])
        os.chdir(wd)
        try:
            compiler_response = subprocess.run(
                lop + [url],
                stdout = subprocess.PIPE,
                stderr = subprocess.PIPE,
                text = True,
                check = True,
                creationflags = subprocess.CREATE_NO_WINDOW
            )
            compiler_response = f"{compiler_response.stdout}\nslay..."
            
        except subprocess.CalledProcessError as e:
            compiler_response = f"{e.output}\nfucking failure..."
            
        compiler_window = Toplevel(self.master)
        compiler_window.title("Compiler")
        compiler_widget = scrolledtext.ScrolledText(compiler_window, wrap = WORD, width = 60, height = 20)
        compiler_widget.insert(END, compiler_response)
        compiler_widget.pack(expand = True, fill = "both")
        compiler_widget.see(END)

        
    def set_compiler(self, event):
        global choice
        choice = self.compiler_choice.get()

    def on_run_compiler(self, event):
        self.run_compiler()
