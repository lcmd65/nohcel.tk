from tkinter import *
from tkinter import ttk, messagebox

class LoginUI(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()
    
    def initUI(self):
        self.parent.title("NOHCEL")
        self.pack(fill = "X", side = "BOTH")
        
        self.label_privacy = Label()
        
    