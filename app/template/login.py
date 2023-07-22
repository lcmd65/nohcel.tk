from tkinter import *
from tkinter.ttk import *

class LoginUI(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()
    
    def initUI(self):
        self.parent.title("NOHCEL")
        self.pack(fill = "X", side = "BOTH")
        
        self.label_privacy = Label(self.parent, text = "lcmd privacy 2023")
        self.label_privacy.pack()
    
        self.notebook = Notebook(self)
        self.notebook.pack()
    