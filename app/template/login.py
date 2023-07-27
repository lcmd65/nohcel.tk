from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
from functools import partial
import app.view.var
from app.view.view import homeView
from app.template.home import Home
import app.environment

class LoginUI(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()
    
    def eventLoginClick(self, account, password):
        try:
            if account.get() == "dat.lemindast" and password.get() == "1":
                app.environment.root_main.destroy()
                app.environment.root_main = Tk()
                app.environment.root_main.geometry("1000x1000+100+100")
                homeView()
                application = Home(app.environment.root_main)
                app.environment.root_main.mainloop()
            else:
                messagebox.showinfo(title= "Login", message = "Wrong Username or password")
        except Exception as e:
            messagebox.showerror(title= "Error", message = e)

    
    def initUI(self):
        self.parent.title("NOHCEL")
        self.pack(fill = BOTH, side = TOP)
        
        self.label_privacy = Label(self.parent, text = "lcmd privacy 2023")
        self.label_privacy.pack(fill = BOTH, side = BOTTOM)

        self.bg = Label(self, i= app.view.var.background_view)
        self.bg.pack(fill = BOTH, side = BOTTOM)
        
        self.notebook = Notebook(self.bg, width= 60, height= 80)
        self.notebook.pack(fill = X, side = TOP, padx = 300, pady =100, ipadx= 400, ipady = 200)
        
        self.frame_login = Frame(self.notebook)
        self.frame_login.pack(fill = BOTH, side = TOP)
        
        self.notebook.add(self.frame_login, text = "     LOGIN     ")
        
        frame_ = [None for _ in range(4)]
        for index in range(4):
            frame_[index] = Frame(self.frame_login)
            frame_[index].pack(side = TOP, fill = X, padx = 10, pady = 10)

        Label_login = Label(frame_[0], i = app.view.var.logo_view)
        Label_login.pack(fill = Y, side = TOP)
        
        label_account = Label(frame_[1], text= "Username")
        label_account.pack(fill = X, side = LEFT)
        
        entry_account = Entry(frame_[1])
        entry_account.pack(fill = X, padx = 10)
        
        label_password = Label(frame_[2], text = "Password")
        label_password.pack(fill = X, side = LEFT)
        
        entry_password = Entry(frame_[2])
        entry_password.pack(fill = X, padx = 10)
        entry_password.config(show = "*")
        
        button_login = Button(frame_[3], text = "Sign In", width = 10, command = partial(self.eventLoginClick, entry_account, entry_password))
        button_login.pack(side = RIGHT, fill = BOTH)
        
        
        