from tkinter import *
from tkinter.ttk import *
from tkinter import font, colorchooser, filedialog, messagebox, scrolledtext

from LineNumbers import *
from MenuBar import *
from ToolBar import *


class ScrollText(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
        self.scrollbar = Scrollbar(self, orient = VERTICAL, command = self.onScroll)
        self.text = Text(self, yscrollcommand = self.scrollbar.set, font = ("consolas", 11), bg = "#282A36", foreground = "#FFFFFF", insertbackground = "#FFFFFF", selectbackground = "#44475A")

        self.numberLines = LineNumbers(self, width = 30)
        self.numberLines.attach(self.text)

        self.scrollbar.pack(side = RIGHT, fill = Y)
        self.numberLines.pack(side = LEFT, fill = Y)
        self.text.pack(side = RIGHT, expand = True, fill = BOTH)

        self.text.bind("<Key>", self.onPressDelay)
        self.text.bind("<Button-1>", self.numberLines.redraw)
        self.scrollbar.bind("<Button-1>", self.onScrollPress)
        self.text.bind("<MouseWheel>", self.onPressDelay)

        self.menu_bar = MenuBar(master, self.text)
        master.config(menu = self.menu_bar)

        self.tool_bar = ToolBar(master, self.text, self.menu_bar)
        self.tool_bar.pack(side = TOP, fill = X)

    def onScrollPress(self, *args):
        self.scrollbar.bind("<B1-Motion>", self.numberLines.redraw)

    def onScrollRelease(self, *args):
        self.scrollbar.unbind("<B1-Motion>", self.numberLines.redraw)

    def onPressDelay(self, *args):
        self.after(2, self.numberLines.redraw)

    def onScroll(self, *args):
        self.text.yview(*args)

    def get(self, *args, **kwargs):
        return self.text.get(*args, **kwargs)

    def insert(self, *args, **kwargs):
        return self.text.insert(*args, **kwargs)

    def delete(self, *args, **kwargs):
        return self.text.delete(*args, **kwargs)

    def index(self, *args, **kwargs):
        return self.text.index(*args, **kwargs)

    def redraw(self):
        self.numberLines.redraw()
