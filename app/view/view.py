import app.view.var
import app.images
from tkinter import *
from app.template.login import LoginUI
from app.template.login_edit import LoginEdit
from app.template.home import Home
from app.template.help import Help
from app.template.edit import EditEnv
from PIL import ImageTk, Image
import app.environment as env

def loginView():
    env.root_main = Tk()
    env.root_main.geometry("1000x1000+100+100")
    app.view.var.background_view = ImageTk.PhotoImage(Image.open('app/images/background_login.png').resize((1092, 1080))) ##4213 × 4167
    app.view.var.logo_view = ImageTk.PhotoImage(Image.open('app/images/color_logo.png').resize((120, 75)))
    application = LoginUI(env.root_main)
    env.root_main.mainloop()

def homeView():
    env.root_main = Tk()
    env.root_main.geometry("1000x1000+100+100")
    app.view.var.background_view = ImageTk.PhotoImage(Image.open('app/images/background_login.png').resize((1092, 1080))) ##4213 × 4167
    app.view.var.logo_view = ImageTk.PhotoImage(Image.open('app/images/color_logo.png').resize((40, 25)))
    application = Home(env.root_main)
    env.root_main.mainloop()
    
def helpView():
    env.root_temp = Toplevel()
    env.root_temp.geometry("400x600+100+100")
    app.vew.var.background_view_toplevel = ImageTk.PhotoImage(Image.open('app/images/background_login.png').resize((1092, 1080)))
    app_temp = Help(env.root_temp)
    env.root_temp.mainloop()

def loginEditView():
    env.root_temp = Toplevel()
    env.root_temp.geometry("1000x1000+100+100")
    application_edit = LoginEdit(env.root_temp)
    env.root_temp.mainloop()

def editView():
    env.root_temp = Tk()
    env.root_temp.geometry("1000x1000+100+100")
    application_edit = EditEnv(env.root_temp)
    env.root_temp.mainloop()