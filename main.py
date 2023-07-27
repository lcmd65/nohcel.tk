import tkinter
from tkinter import Tk
from app.template.login import LoginUI
from app.view import view
import app.environment

if __name__ == "__main__":
    app.environment.root_main = Tk()
    app.environment.root_main.geometry("1000x1000+100+100")
    view.loginView()
    application = LoginUI(app.environment.root_main)
    app.environment.root_main.mainloop()

