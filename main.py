import tkinter
from tkinter import Tk
from app.template.login import LoginUI
from app.view import view_login

if __name__ == "__main__":
    root = Tk()
    root.geometry("1000x1000+100+100")
    view_login.loginView()
    app = LoginUI(root)
    root.mainloop()

