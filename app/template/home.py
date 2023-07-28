import app.view.var
import app.environment
import tksheet 
from tkinter import *
from tkinter import (
    Button,
    ttk,
    messagebox)
from app.func.func import sequence
from app.template.help import Help
from functools import partial


## UI of Laser python CE P3
class Home(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()
    
    def eventClickHome(self):
        """ event click to add audio """
        return
    
    def eventClickExit(self):
        """ event click exit to login"""
        return
        
    def eventButtonClickEdit(self):
        """ event click edit env """
        return
    
    def eventClickHelp(self):
        
        return
        
    def eventProcessingLabel(self):
        """ main function of this tool """
        
        return
        
    def eventStartFunction(self):
        """ event start """
        
        return
        
    def eventEndFunction(self):
        """ event end """
        
        return
    
    def initUI(self):
        self.parent.title("VinBigdata Speech to Text")
        self.pack(fill=BOTH, expand=True)
        
        self.label_root = Label(self, i= app.view.var.background_view, bg = None)
        self.label_root.pack()
        
        # button bar (consist of Exit, Edit, Help)
        self.button_bar = Frame(self.label_root, bg= None)
        self.button_bar.pack(side = TOP, fill = X)
        self.button_bars = [ None for _ in range(5)]
        for index, label_text, commands in zip(range(1, 5), ["Exit", "File", "Edit", "Help"], [self.eventClickExit, None, self.eventButtonClickEdit, self.eventClickHelp]):
            self.button_bars[index] = Button(self.button_bar, text = label_text, width= 10, command= commands, bg= None, image=None)
            self.button_bars[index].config(bg= None, bd=0)
            self.button_bars[index].pack(side = LEFT, fill = BOTH)
        
        self.button_bars[0] = Label(self.button_bar, i = app.view.var.logo_view)
        self.button_bars[0].pack(side = RIGHT)  
        # Notebook include tab home, laser P3A to C
        self.notebook_control = ttk.Notebook(self.label_root)
        self.notebook_control.pack(expand= True, fill=BOTH, padx=5, pady= 20)
        
        # init tab control 
        self.tab_controls = [None for _ in range(4)]
        self.body_controls = [None for _ in range(4)]
        self.button_controls = [None for _ in range(4)]
        self.text_controls = [None for _ in range(4)]
        self.sheet_controls = [None for _ in range(4)]
        
        for index, label_text in zip(range(2), ['    HOME    ', '      Speech to Text      ']):
            self.tab_controls[index] = Frame(self.notebook_control)
            self.tab_controls[index].pack(side= LEFT, padx=0, pady=5)
            self.notebook_control.add(self.tab_controls[index], text = label_text)
            if index != 0: # except home tab
                self.body_controls[index] = [None for _ in range(3)]
                self.button_controls[index] =[None for _ in range(4)]
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
                    self.button_controls[index][se_index] = Button(self.body_controls[index][0], text= button_text, width=25, command = command_)
                    self.button_controls[index][se_index].pack(side=LEFT, padx=5, pady=5)
            
            # tab home define
            elif index == 0:
                self.body_controls[index] = Frame(self.tab_controls[index])
                self.body_controls[index].pack(fill= X, padx=5 ,pady=5)
                self.button_controls[index] = Button(self.body_controls[index], text="Analyze", width=10, command = sequence(self.eventClickHome))
                self.button_controls[index].pack(side=LEFT, padx=5, pady=5)

