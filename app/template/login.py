from tkinter import *
from tkinter.ttk import *

class LoginUI(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()
    
    def initUI(self):
        self.parent.title("NOHCEL")
        self.pack(fill = BOTH, side = TOP)
        
        self.label_privacy = Label(self.parent, text = "lcmd privacy 2023")
        self.label_privacy.pack(fill = BOTH, side = BOTTOM)
    
        self.notebook = Notebook(self, width= 100, height= 120)
        self.notebook.pack(fill = X, side = TOP, padx = 50, pady =50, ipadx= 200, ipady = 200)
        
        self.frame_login = Frame(self.notebook)
        self.frame_login.pack(fill = BOTH, side = TOP)
        
        frame_ = [None for _ in range(4)]
        for index in range(4):
            frame_[index] = Frame(self.frame_login)
            frame_[index].pack(side = TOP, fill = X)

        Label_login = Label(frame_[0], text = "LOGIN")
        Label_login.pack(fill = X, side = TOP)
        