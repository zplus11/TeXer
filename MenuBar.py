from tkinter import *
from tkinter.ttk import *
from tkinter import font, colorchooser, filedialog, messagebox, scrolledtext

import os

class MenuBar(Menu):
    url = ""
    
    def __init__(self, master, text_widget, *args, **kwargs):
        Menu.__init__(self, master, *args, **kwargs)
        self.text_widget = text_widget
        self.master = master
        
        filemenu = Menu(self, tearoff = False)
        self.add_cascade(label = "File", menu = filemenu)
        filemenu.add_command(label = "New", accelerator = "ctrl + n", command = self.new_file)
        filemenu.add_command(label = "Open", accelerator = "ctrl + o", command = self.open_file)
        filemenu.add_command(label = "Save", accelerator = "ctrl + s", command = self.save_file)
        filemenu.add_command(label = "Save as", accelerator = "ctrl + shift + s", command = self.save_as_file)

        master.bind("<Control-n>", self.on_new_file)
        master.bind("<Control-o>", self.on_open_file)
        master.bind("<Control-s>", self.on_save_file)
        master.bind("<Control-S>", self.on_save_as_file)

        font_families = font.families()
        my_font = font_families.index("Consolas")

    
    def new_file(self):
        global url
        if self.text_widget.get(0.0, END) and messagebox.askyesno("Unsaved Changes", "Do you want to save changes before creating a new file?"):
            self.save_file()
        self.text_widget.delete(0.0, END)
        
    def open_file(self):
        global url
        self.url = filedialog.askopenfilename(initialdir = os.getcwd, title = "Select File", filetypes = (("TeX Files", "tex"), ("Bib Files", "bib"), ("All Files", "*.*")))
        if self.url != "":
            data = open(self.url, "r")
            self.text_widget.delete(0.0, END)
            self.text_widget.insert(0.0, data.read())
        self.master.title(self.url)

    def save_file(self):
        if self.url == "":
            save_url = filedialog.asksaveasfile(mode = "w", defaultextension = ".tex", filetypes = (("TeX Files", "tex"), ("Bib Files", "bib"), ("All Files", "*.*")))
            if save_url != "":
                content = self.text_widget.get(0.0, END)
                save_url.write(content)
                save_url.close()
        else:
            content = self.text_widget.get(0.0, END)
            file = open(self.url, "w")
            file.write(content)

    def save_as_file(self):
        save_url = filedialog.asksaveasfile(mode = "w", defaultextension = ".tex", filetypes = (("TeX Files", "tex"), ("Bib Files", "bib"), ("All Files", "*.*")))
        content = self.text_widget.get(0.0, END)
        save_url.write(content)
        save_url.close()

    def on_new_file(self, event):
        self.new_file()
        
    def on_open_file(self, event):
        self.open_file()
        
    def on_save_file(self, event):
        self.save_file()
        
    def on_save_as_file(self, event):
        self.save_as_file()
