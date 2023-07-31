import app.view.var
import app.environment
import tksheet 
from tkinter import *
from tkinter.ttk import Style, Button
from tkinter import (
    ttk,
    messagebox)
from app.func.func import sequence
from functools import partial


## UI of Laser python CE P3
class Home(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()
    
    def eventClickPushData(self, tree):
        """ click to exit to login"""
        tree['selectmode'] = "browse"
    
    def eventClickExit(self):
        """ click to Exit """
        try:
            from app.view.view import loginView
            app.environment.root_main.destroy()
            loginView()
        except Exception as e:
            messagebox.showerror(title= "Error", message = e)
        
    def eventButtonClickEdit(self):
        """click to Edit software environment"""
        try:
            from app.view.view import editView
            editView()
        except Exception as e:
            messagebox.showerror(title= "Error", message = e)
        return
    
    def eventClickHelp(self):
        try:
            from app.view.view import helpView
            helpView()
        except Exception as e:
            messagebox.showerror(title= "Error", message = e)
        
    def eventProcessingLabel(self):
        """ main function of this tool """
        
        return
        
    def eventStartFunction(self):
        
        return
        
    def eventEndFunction(self):
        
        return
        
    def initUI(self):
        self.parent.title("VinBigdata LLM")
        self.pack(fill=BOTH, expand = True, side = BOTTOM)
        
        self.label_root = Label(self.parent, i= app.view.var.background_view, bg = None)
        self.label_root.pack(fill = BOTH, side = TOP)
        
        self.label_privacy = Label(self, text = "VinBigdata Privacy @2023")
        self.label_privacy.pack(fill = X, side = LEFT, padx = 10)
        
        self.logo_menu = Label(self, i = app.view.var.logo_view)
        self.logo_menu.pack(side = RIGHT, padx = 10)  
        
        self.home_menu = Menu(self.parent)

        """file menu"""
        file_menu = Menu(self.home_menu)
        file_menu.add_command(label="New", command = None)
        file_menu.add_command(label="Open", command = None)
        file_menu.add_separator()
        file_menu.add_command(label= "Exit", command = partial(self.eventClickExit))
        
        """ edit menu """
        edit_menu = Menu(self.home_menu)
        edit_menu.add_command(label="Edit environment", command = partial(self.eventButtonClickEdit))
        
        """ help menu """
        help_menu = Menu(self.home_menu)
        help_menu.add_command(label = "Help", command = partial(self.eventClickHelp))
        
        for index, label_text, commands in zip(range(1, 4), ["File", "Edit", "Help"], [file_menu, edit_menu, help_menu]):
            self.home_menu.add_cascade(label= label_text, menu = commands)
        
        # Notebook include tab home, laser P3A to C
        self.notebook_control = ttk.Notebook(self.label_root)
        self.notebook_control.pack(expand= True, fill=BOTH, padx=10, pady= 0)
        noteStyle = ttk.Style()
        noteStyle.configure('TNotebook', tabposition='wn')
        noteStyle.theme_use('default')
        noteStyle.configure("TNotebook", background= "#001c54", borderwidth = 0)
        noteStyle.configure("TNotebook.Tab", background = "#001c54", foreground = "#ececec", borderwidth = 0)
        noteStyle.map("TNotebook", background= [("selected", "#ececec")] )
        noteStyle.map("TNotebook.Tab", foreground = [("selected", "black")])
        
        buttonStyle = Style()
        buttonStyle.configure('W.TButton', background = "#ececec", foreground = 'black')
        
        # init tab control 
        self.tab_controls = [None for _ in range(2)]
        self.body_controls = [None for _ in range(2)]
        self.button_controls = [None for _ in range(2)]
        self.text_controls = [None for _ in range(2)]
        self.sheet_controls = [None for _ in range(2)]
        
        for index, label_text in zip(range(2), ['           NOHCEL BOT           ', '      Speech to Text      ']):
            self.tab_controls[index] = Frame(self.notebook_control, bg=None)
            self.tab_controls[index].pack(side= LEFT, padx=0, pady=5)
            self.notebook_control.add(self.tab_controls[index], text = label_text)
            if index != 0: # except home tab
                self.body_controls[index] = [None for _ in range(3)]
                self.button_controls[index] =[None for _ in range(3)]
                for se_index in range(3):
                    self.body_controls[index][se_index] = Frame(self.tab_controls[index])
                    self.body_controls[index][se_index].pack(fill =X)
                
                # sheet view of each laser tab
                self.sheet_controls[index] = tksheet.Sheet(self.body_controls[index][2], data = [[]], height = 800, width = 1500)
                self.sheet_controls[index].pack(fill=BOTH, pady=10, padx=5, expand=True)
                self.sheet_controls[index].grid(row =20, column = 20, sticky="nswe")
                self.sheet_controls[index].enable_bindings()
                
                # text information view of each laser tab
                self.text_controls[index] =  Text(self.body_controls[index][1], bg ="#fcfcfc", height= 2)
                self.text_controls[index].pack(fill=BOTH, pady=0, padx=5, expand=True)
                
                # get type of machine data connect: A, B, C
                commands = [
                    partial(self.eventProcessingLabel),
                    partial(self.eventStartFunction),
                    partial(self.eventEndFunction),
                ]
                for se_index, button_text, command_ in zip(range(3), ["Import Audio", "Start", "End"], commands):
                    self.button_controls[index][se_index] = Button(self.body_controls[index][0], text= button_text, width= 15, style = 'W.TButton', command = command_)
                    self.button_controls[index][se_index].pack(side=LEFT, padx=5, pady=5)
            
            # tab home define
            elif index == 0:
                self.body_controls[index] = [None for _ in range(2)]
                self.body_controls[index][0] = Frame(self.tab_controls[index])
                self.body_controls[index][0].pack(fill= Y, padx = 0 ,pady = 0, side = LEFT)
                self.body_controls[index][1] = Frame(self.tab_controls[index])
                self.body_controls[index][0].pack(fill= Y, padx = 0 ,pady = 5)
                
                self.tree = ttk.Treeview(self.body_controls[index][0],  columns=(1),  show='headings', height = 40)
                self.tree.pack(fill = Y)
                
                self.tree.heading(1, text='AUDIO')
                self.tree.insert(parent='', index=0, iid=0, values=("audio_name.mp3"))
                
                self.button_controls[index] = Button(self.body_controls[index][0], text="Browse",style = 'W.TButton', width= 15, command = sequence(self.eventClickPushData, self.tree))
                self.button_controls[index].pack(side=BOTTOM, padx = 0, pady = 0, fill = X)

