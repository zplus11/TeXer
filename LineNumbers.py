from tkinter import *
from tkinter.ttk import *
from tkinter import font, colorchooser, filedialog, messagebox, scrolledtext


class LineNumbers(Canvas):
    def __init__(self, *args, **kwargs):
        Canvas.__init__(self, *args, **kwargs, highlightthickness = 0)
        self.textwidget = None

    def attach(self, text_widget):
        self.textwidget = text_widget

    def redraw(self, *args):
        global i
        self.delete("all")
        i = self.textwidget.index("@0,0")
        while True:
            dline = self.textwidget.dlineinfo(i)
            if dline is None:
                break
            y = dline[1]
            linenum = str(i).split(".")[0]
            self.create_text(2, y, anchor = "nw", text = linenum, fill = "#606366")
            i = self.textwidget.index("%s+1line" % i)
