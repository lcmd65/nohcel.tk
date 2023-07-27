import app.view.var
import app.images
from PIL import ImageTk, Image

def loginView():
    app.view.var.background_view = ImageTk.PhotoImage(Image.open('app/images/background_login.png').resize((1092, 1080))) ##4213 × 4167
    app.view.var.logo_view = ImageTk.PhotoImage(Image.open('app/images/color_logo.png').resize((120, 75)))
