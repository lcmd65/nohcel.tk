import tkinter
from tkinter import Tk
from app.template.login import LoginUI

if __name__ == "__main__":
    root = Tk()
    root.geometry("1000x1000+100+100")
    app = LoginUI(root)
    root.mainloop()

