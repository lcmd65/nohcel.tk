from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
from functools import partial
import app.view.var
from app.view.view import homeView
from app.template.home import Home
from app.template.login_edit import LoginEdit
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

    def eventLoginEditClick(self):
        try:
            app.environment.root_temp = Toplevel()
            app.environment.root_temp.geometry("1000x1000+100+100")
            application_edit = LoginEdit(app.environment.root_temp)
            app.environment.root_temp.mainloop()
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
        
        frame_list = [None for _ in range(5)]
        for index in range(5):
            frame_list[index] = Frame(self.frame_login)
            frame_list[index].pack(side = TOP, fill = X, padx = 10, pady = 10)

        Label_login = Label(frame_list[0], i = app.view.var.logo_view)
        Label_login.pack(fill = Y, side = TOP)
        
        label_account = Label(frame_list[1], text= "Username")
        label_account.pack(fill = X, side = LEFT)
        
        entry_account = Entry(frame_list[1])
        entry_account.pack(fill = X, padx = 10)
        
        label_password = Label(frame_list[2], text = "Password")
        label_password.pack(fill = X, side = LEFT)
        
        entry_password = Entry(frame_list[2])
        entry_password.pack(fill = X, padx = 10)
        entry_password.config(show = "*")
        
        label_forgot = Label(frame_list[3], text = "Forgot Password?")
        label_forgot.pack(side = TOP, fill = X)
        label_forgot.bind("<Button-1>", lambda e:partial(self.eventLoginEditClick))
        
        button_login = Button(frame_list[4], text = "Sign In", width = 10, command = partial(self.eventLoginClick, entry_account, entry_password))
        button_login.pack(side = RIGHT, fill = BOTH)
        
        
        