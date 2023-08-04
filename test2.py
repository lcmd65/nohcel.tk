# -*- coding: utf-8 -*-
# Subscribe to PyShine Youtube channel for more detail! 
#
# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
#
# WEBSITE: www.pyshine.com
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Qt5Agg')
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as Navi
from matplotlib.figure import Figure
import seaborn as sns
import pandas as pd
import sip # can be installed : pip install sip
from datetime import datetime

# We require a canvas class
from mpldatacursor import datacursor
class MatplotlibCanvas(FigureCanvasQTAgg):
	def __init__(self,parent=None, dpi = 120):
		fig = Figure(dpi = dpi)
		self.axes = fig.add_subplot(111)
		super(MatplotlibCanvas,self).__init__(fig)
		fig.tight_layout()
		
		

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1440, 1000)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)

        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setObjectName("label_1")
        
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout.addWidget(self.comboBox)
        
        self.comboBox_1 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_1.setObjectName("comboBox_1")
        
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setObjectName("comboBox_2")
        
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setObjectName("radioButton")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        
        self.horizontalLayout.addItem(spacerItem)
        self.horizontalLayout.addWidget(self.label_1)
        self.horizontalLayout.addWidget(self.comboBox_1)
        self.horizontalLayout.addWidget(self.label_2)
        self.horizontalLayout.addWidget(self.comboBox_2)
        self.horizontalLayout.addWidget(self.label_3)
        self.horizontalLayout.addWidget(self.radioButton)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(self.spacerItem1)
        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen_csv_file = QtWidgets.QAction(MainWindow)
        self.actionOpen_csv_file.setObjectName("actionOpen_csv_file")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionOpen_csv_file)
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.filename = ''
        self.canv = MatplotlibCanvas(self)
        self.df = []
        
        self.toolbar = Navi(self.canv,self.centralwidget)
        self.horizontalLayout.addWidget(self.toolbar)
        
        self.themes = ['bmh', 'classic', 'dark_background', 'fast', 
        'fivethirtyeight', 'ggplot', 'grayscale', 'seaborn-bright',
         'seaborn-colorblind', 'seaborn-dark-palette', 'seaborn-dark', 
         'seaborn-darkgrid', 'seaborn-deep', 'seaborn-muted', 'seaborn-notebook',
         'seaborn-paper', 'seaborn-pastel', 'seaborn-poster', 'seaborn-talk',
         'seaborn-ticks', 'seaborn-white', 'seaborn-whitegrid', 'seaborn',
         'Solarize_Light2', 'tableau-colorblind10']
         
        self.comboBox.addItems(self.themes)
        self.comboBox_1.addItems(['Select horizontal axis here'])
        self.comboBox_2.addItems(['Select vertical axis here'])
        
        self.pushButton.clicked.connect(self.getFile)
        self.comboBox.currentIndexChanged['QString'].connect(self.Update)
        self.comboBox_1.currentIndexChanged['QString'].connect(self.selectXaxis)
        self.comboBox_2.currentIndexChanged['QString'].connect(self.selectYaxis)
        self.actionExit.triggered.connect(MainWindow.close)
        self.actionOpen_csv_file.triggered.connect(self.getFile)
        self.radioButton.clicked.connect(self.vsAll)
        self.dataset={}
        self.x_axis_slt=None
        self.y_axis_slt=None
        self.vsall = False

    def vsAll(self):
        """
        This function will be called upon triggering the radio check button. If set to True, all the columsn in the csv
        will be plotted against the x-axis column. Please note that vs all means versus all, so that whatever value is 
        selected as the x-axis, it wont be plotted against itself in this mode. Moreover, the time series data will be 
        dedicated for the datetime x-axis and it wont be displayed in the vs all contents.

        """
        if self.vsall==False:
            self.vsall=True
        else:
            self.vsall=False
        self.Update(self.themes[0])

    def selectXaxis(self,value):
        """
        This function will update the plot according to the data of x axis selected from combo box

        """
        self.x_axis_slt=value
        self.Update(self.themes[0])
        
    def selectYaxis(self,value):
        """
        This function will update the plot according to the data of y axis selected from combo box

        """
        self.y_axis_slt=value
        self.Update(self.themes[0])

    def Update(self,value):

        """
        This function will input the value of theme and accordingly plot the data, if the data is relative, i.e., x verus y-axis
        then the user can assign x and y axis from the combo box. If all data should be plotted in paraller then leave,
        the combo boxes of axis selections to their default starting location.
            
        """
        plt.clf()
        plt.style.use(value)
        try:
            self.horizontalLayout.removeWidget(self.toolbar)
            self.verticalLayout.removeWidget(self.canv)
            
            sip.delete(self.toolbar)
            sip.delete(self.canv)
            self.toolbar = None
            self.canv = None
            self.verticalLayout.removeItem(self.spacerItem1)
        except Exception as e:
            print(e)
            pass
        self.canv = MatplotlibCanvas(self)
        self.toolbar = Navi(self.canv,self.centralwidget)
        
        self.horizontalLayout.addWidget(self.toolbar)
        self.verticalLayout.addWidget(self.canv)
        
        self.canv.axes.cla()
        ax = self.canv.axes

        try:
            

            if self.vsall:
                for k,v in self.dataset.items():
                
                    if k!=self.x_axis_slt and type(v[0])!=datetime:		
                        lines = ax.plot(self.dataset[self.x_axis_slt],v,label=k) 
                        datacursor(lines)    
                        

                    
                legend = ax.legend()
                legend.set_draggable(True)
                ax.set_xlabel(self.x_axis_slt)
                ax.set_ylabel('ALL OTHERS')
                ax.set_title(self.Title)
                #plt.setp(ax.xaxis.get_majorticklabels(), rotation=25)  # uncomment if you want the x-axis to tilt 25 degree


            else:
            

                lines = ax.plot(self.dataset[self.x_axis_slt],self.dataset[self.y_axis_slt],label=self.y_axis_slt) 
                datacursor(lines)
                legend = ax.legend()
                legend.set_draggable(True)
                ax.set_xlabel(self.x_axis_slt)
                ax.set_ylabel(self.y_axis_slt)
                ax.set_title(self.Title)
                #plt.setp(ax.xaxis.get_majorticklabels(), rotation=25)  # uncomment if you want the x-axis to tilt 25 degree
            
        except Exception as e:
            print(e)
            try:
                lines = self.df.plot(ax = self.canv.axes)
                datacursor(lines)
                legend = ax.legend()
                legend.set_draggable(True)
                
                ax.set_xlabel('X axis')
                ax.set_ylabel('Y axis')
                ax.set_title(self.Title)
            except Exception as e:
                print(e)
                pass
            pass
        
        self.canv.draw()
        
        
        
        

    def getFile(self):
        """ This function will get the address of the csv file location
            also calls a readData function 
        """
        try:
            self.filename = QFileDialog.getOpenFileName(filter = "csv (*.csv)")[0]
            self.readData()
        except Exception as e:
            print(e)
            pass

    def getDataset(self,csvfilename):
        """
        This function will convert csv file to a dictionary of dataset, with keys as the columns' names and
        values as values. The datatime format should be one of the standard datatime formats. Before plottting
        we need to convert the string of data time in the csv file values to datatime format.
        """
        df = pd.read_csv(csvfilename,encoding='utf-8').fillna(0)
        LIST_OF_COLUMNS = df.columns.tolist()
        dataset={}
        # time_format = "%d/%m/%Y %H:%M:%S" 
        # time_format =  "%m/%d/%Y"
        # time_format = "%d/%m/%Y"
        # time_format = "%m-%d-%Y"
        # time_format = "%d-%m-%Y"
        # time_format = "%H:%M:%S"
        # time_format = "%M:%S"
        # time_format = '%d/%m/%Y %H:%M%f'
        time_format = '%Y-%m-%d %H:%M:%S.%f'
        
        
        for col in LIST_OF_COLUMNS:
            dataset[col]  =  df[col].iloc[0:].values
            try:
                dataset[col] = [datetime.strptime(i, time_format) for i in df[col].iloc[0:].values]
            except Exception as e:
                pass
                print(e)
        return dataset,LIST_OF_COLUMNS

    def readData(self):
        """ This function will read the data using pandas and call the update
            function to plot
        """
        import os
        self.dataset={}
        self.x_axis_slt=None
        self.y_axis_slt=None

        base_name = os.path.basename(self.filename)
        self.Title = os.path.splitext(base_name)[0]
        
        self.dataset, LIST_OF_COLUMNS = self.getDataset(self.filename)
        
        self.df = pd.read_csv(self.filename,encoding = 'utf-8').fillna(0)
        
        self.Update(self.themes[0]) # lets 0th theme be the default : bmh
        self.comboBox_1.clear()
        self.comboBox_2.clear()
        self.comboBox_1.addItems(['Select horizontal axis here'])
        self.comboBox_2.addItems(['Select vertical axis here'])
        self.comboBox_1.addItems(LIST_OF_COLUMNS)
        self.comboBox_2.addItems(LIST_OF_COLUMNS)




    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Select Theme"))
        self.label_1.setText(_translate("MainWindow", "X-axis"))
        self.label_2.setText(_translate("MainWindow", "Y-axis"))
        self.label_3.setText(_translate("MainWindow", "vs all"))
        self.pushButton.setText(_translate("MainWindow", "Open"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpen_csv_file.setText(_translate("MainWindow", "Open csv file"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))

# Subscribe to PyShine Youtube channel for more detail! 

# WEBSITE: www.pyshine.com

if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	
	MainWindow.show()
	sys.exit(app.exec_())


