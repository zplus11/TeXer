from tkinter import *
from tkinter.ttk import *
from tkinter import font, colorchooser, filedialog, messagebox, scrolledtext

import subprocess
import os
import re


class ToolBar(Frame):
    def __init__(self, master, text_widget, menu_bar, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self.text_widget = text_widget
        self.menu_bar = menu_bar
        self.compiler_choice = StringVar()
        self.pdf_choice = StringVar()
        self.compiler_image = PhotoImage(file = r"assets\images\compile.png")
        
        tool_bar = Label(master)
        tool_bar.pack(side = TOP, fill = X)
        compiling_box = Combobox(tool_bar, width = 20, values = ("pdflatex", "pdftex", "lualatex", "xelatex"), state = "readonly", textvariable = self.compiler_choice)
        compiling_box.current(0)
        compiling_box.grid(row = 0, column = 0)
        compiling_box.bind("<<ComboboxSelected>>", self.set_compiler)
        pdf_choice = Combobox(tool_bar, width = 10, values = ("Yes", "No"), state = "readonly", textvariable = self.pdf_choice)
        pdf_choice.current(0)
        pdf_choice.grid(row = 0, column = 1)
        pdf_choice.bind("<<ComboboxSelected>>", self.set_pdf_choice)
        
        compile_button = Button(tool_bar, image = self.compiler_image, command = self.run_compiler)
        compile_button.grid(row = 0, column = 2)

    def run_compiler(self):
        global choice, choicepdf

        url = self.menu_bar.url
        print("imported url from menu bar:", url)
        if url == "":
            compiler_window = Toplevel(self.master)
            compiler_window.title("Compiler")
            compiler_widget = scrolledtext.ScrolledText(compiler_window, wrap = WORD, width = 60, height = 20)
            compiler_widget.insert(END, "For some reason (you would know better), the file you're trying to compile is not saved. Save it before compiling.")
            compiler_widget.pack(expand = True, fill = "both")
            compiler_widget.see(END)
        else:
            choice = self.compiler_choice.get()
            
            url_split = url.split("/")
            wd = "/".join(url_split[:-1])
            print("Moved to", wd)
            os.chdir(wd)
            try:
                print(f"Calling [{choice} {url}]...")
                compiler_response = subprocess.run(
                    [choice] + [url],
                    stdout = subprocess.PIPE,
                    stderr = subprocess.PIPE,
                    text = True,
                    check = True,
                    creationflags = subprocess.CREATE_NO_WINDOW
                )
                compiler_response = compiler_response.stdout
                print("compiled", url, "successfully")
                if self.pdf_choice.get() == "Yes":
                    try:
                        view_url = (url[:-4] + ".pdf").replace("/", "\\")
                        os.startfile(view_url)
                        print("Launched pdf", view_url)
                    except Exception as e:
                        print("Viewing failed:", e)
                        pdf_window = Toplevel(self.master)
                        pdf_window.title("PDF Viewer")
                        pdf_widget = scrolledtext.ScrolledText(pdf_window, wrap = WORD, width = 60, height = 20)
                        pdf_widget.insert(END, f"PDF could not be viewed.\n{e}")
                        pdf_widget.pack(expand = True, fill = "both")
                        pdf_widget.see(END)
                
            except subprocess.CalledProcessError as e:
                compiler_response = e.output
                print("compiled", url, "with errors")
                
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

    def set_pdf_choice(self, event):
        global pdfchoice
        pdfchoice = self.pdf_choice.get()

    def on_set_pdf_choice(self, event):
        self.set_pdf_choice()
