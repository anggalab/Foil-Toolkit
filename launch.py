import sys
import os

from subprocess import Popen

from PySide2 import QtCore, QtGui
from PySide2.QtWidgets import QApplication, QMessageBox, QFileDialog, QMainWindow, QDialog, QLineEdit, QPushButton, QStatusBar, QWidget, QAction, QKeySequenceEdit, QMenuBar, QMenu, QSizePolicy, QDesktopWidget, QVBoxLayout, QPushButton, QLabel, QTextEdit
from PySide2.QtGui import QIcon, QKeySequence

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

import matplotlib.pyplot as plt
import numpy as np

from naca import naca
from funct import airfoil_funct

class MainWindow(QMainWindow):
    
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.title = 'Foil Toolkit'
        self.width = 500
        self.height = 500
        self.setFixedSize(self.size())
        self.setWindowIcon(QIcon('img/logo.png'))
        self.plotcanvas()
        self.component()
        self.centerwindow()
        
    def inputwindowform(self):
        self.input_window = InputWindow()
        self.input_window.show()

    def propertiesform(self):
        self.properties_window = PropertiesWindow()
        self.properties_window.show()

    def plotcanvas(self):
        self.setWindowTitle(self.title)
        self.setGeometry(0, 0, self.width, self.height)
        m = FoilCanvas(self)
        m.move(0, 0)
        self.show()

    def centerwindow(self):
        ctr = self.frameGeometry()
        dsk = QDesktopWidget().availableGeometry().center()
        ctr.moveCenter(dsk)
        self.move(ctr.topLeft())

    def CreateMenus(self):
        self.fileMenu = self.menuBar().addMenu("&File")
        self.optionMenu = self.menuBar().addMenu("&Foil")
        self.helpMenu = self.menuBar().addMenu("&Help")

    def component(self):
        self.CreateActions()
        self.CreateMenus()
        self.CreateToolBar()

        self.export = self.fileMenu.addMenu(QIcon('img/export.png'), "Export")
        self.export.addAction(self.DxfAction)
        self.export.addAction(self.DatAction)
        self.export.addAction(self.TxtAction)
        self.export.addAction(self.CsvAction)
        self.export.addAction(self.CfgAction)
        self.export.addAction(self.XlsAction)

        self.fileMenu.addAction(self.exitAction)

        self.optionMenu.addAction(self.inputAction)
        self.optionMenu.addSeparator()
        self.optionMenu.addAction(self.propertiesAction)

        self.helpMenu.addAction(self.aboutAction)

        self.mainToolBar.addAction(self.DxfAction)
        self.mainToolBar.addAction(self.TxtAction)
        self.mainToolBar.addAction(self.DatAction)
        self.mainToolBar.addAction(self.CfgAction)
        self.mainToolBar.addAction(self.CsvAction)
        self.mainToolBar.addAction(self.XlsAction)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(self.inputAction)
        self.mainToolBar.addAction(self.propertiesAction)

    def CreateActions(self):
        self.exitAction = QAction( QIcon('img/exit.png'), 'Exit', self, shortcut="Ctrl+Q", statusTip="exit", triggered=self.exitFile)
        self.aboutAction = QAction( QIcon('img/about.png'), 'About', self, statusTip="about Foil Toolkit", triggered=self.showAbout)
        self.DatAction = QAction( QIcon('img/dat.png'), 'dat', self, statusTip="save as dat file", triggered=self.DatExport)
        self.CfgAction = QAction( QIcon('img/cfg.png'), 'cfg', self, statusTip="save as configuration file..", triggered=self.CfgExport)
        self.TxtAction = QAction( QIcon('img/txt.png'), 'txt', self, statusTip="save as text file", triggered=self.TxtExport)
        self.DxfAction = QAction( QIcon('img/dxf.png'), 'dxf', self, statusTip="save as 2D Autodesk file", triggered=self.DxfExport)
        self.CsvAction = QAction( QIcon('img/csv.png'), 'csv', self, statusTip="save as comma separate value or csv file..", triggered=self.CsvExport)
        self.XlsAction = QAction( QIcon('img/xls.png'), 'xls', self, statusTip="save as excel..", triggered=self.XlsExport)
        self.inputAction = QAction( QIcon('img/input.png'),'Input', self, shortcut="Ctrl+I", statusTip="input naca type and amount of points", triggered=self.inputwindowform)
        self.propertiesAction = QAction( QIcon('img/properties.png'),'Properties', self, statusTip="show project properties", triggered=self.propertiesform)
        
    def DatExport(self):
        savedlg1, savedlg2 = QFileDialog.getSaveFileName(self, 'save files..', '', '*.dat')
        X, Y = airfoil_funct()
        txty = list(Y)
        txtx = list(X)
        zipxy = zip(X,Y)
        textxy = list(zipxy)

        with open(savedlg1, 'w') as txt_file:
            for item in textxy:
                txt_file.write("%s %s\n" % item)

    def TxtExport(self):
        savedlg1, savedlg2 = QFileDialog.getSaveFileName(self, 'save files..', '', '*.txt')
        X, Y = airfoil_funct()
        txty = list(Y)
        txtx = list(X)
        zipxy = zip(X,Y)
        textxy = list(zipxy)

        with open(savedlg1, 'w') as txt_file:
            for item in textxy:
                txt_file.write("%s %s\n" % item)

    def DxfExport(self):
        savedlg1, savedlg2 = QFileDialog.getSaveFileName(self, 'save files..', '', '*.dxf')
        X, Y = airfoil_funct()
        txty = list(Y)
        txtx = list(X)
        zipxy = zip(X,Y)
        textxy = list(zipxy)

        with open(savedlg1, 'w') as txt_file:
            for item in textxy:
                txt_file.write("%s %s\n" % item)

    def CsvExport(self):
        savedlg1, savedlg2 = QFileDialog.getSaveFileName(self, 'save files..', '', '*.csv')
        X, Y = airfoil_funct()
        txty = list(Y)
        txtx = list(X)
        zipxy = zip(X,Y)
        textxy = list(zipxy)

        with open(savedlg1, 'w') as txt_file:
            for item in textxy:
                txt_file.write("%s %s\n" % item)

    def XlsExport(self):
        savedlg1, savedlg2 = QFileDialog.getSaveFileName(self, 'save files..', '', '*.xls')
        X, Y = airfoil_funct()
        txty = list(Y)
        txtx = list(X)
        zipxy = zip(X,Y)
        textxy = list(zipxy)

        with open(savedlg1, 'w') as txt_file:
            for item in textxy:
                txt_file.write("%s %s\n" % item)

    def CfgExport(self):
        savedlg1, savedlg2 = QFileDialog.getSaveFileName(self, 'save files..', '', '*.cfg')
        
        X, Y = airfoil_funct()
        txty = list(Y)
        txtx = list(X)
        zipxy = zip(X,Y)
        textxy = list(zipxy)

        with open(savedlg1, 'w') as txt_file:
            for item in textxy:
                txt_file.write("%s %s\n" % item)

    def exitFile(self):
        self.close()
        
    def CreateToolBar(self):
        self.mainToolBar = self.addToolBar('Main')

    def showAbout(self):
        QMessageBox.about(self, "about",  "Foil Toolkit v0.1.3 is open source airfoil plot generator\nIt's running on Windows and Linux environment. \nDistribution and modification under GNU GPLv3 License")

class InputWindow(QDialog):
    def __init__(self):
        super(InputWindow, self).__init__()
        self.setFixedSize(220,180)
        self.setWindowTitle('NACA Input')
        
        layout = QVBoxLayout()
        self.labelnaca = QLabel("NACA Type")
        self.labelnaca.show()
        layout.addWidget(self.labelnaca)
        
        self.nacainput = QLineEdit("6409")
        self.nacainput.show()
        layout.addWidget(self.nacainput)

        self.labelpoint = QLabel("Point Plot")
        self.labelpoint.show()
        layout.addWidget(self.labelpoint)
        
        self.pointinput = QLineEdit("500")
        self.pointinput.show()
        layout.addWidget(self.pointinput)

        self.plotBtn = QPushButton("Plot")
        self.plotBtn.clicked.connect(self.input_naca_type)
        self.plotBtn.clicked.connect(self.input_plot)
        self.plotBtn.show()
        layout.addWidget(self.plotBtn)

        self.cancelBtn = QPushButton("Cancel")
        self.cancelBtn.clicked.connect(self.input_close)
        self.cancelBtn.show()
        layout.addWidget(self.cancelBtn)
        
        self.setLayout(layout)
        self.show()

    def input_plot(self):
        self.close()
        MainWindow.close()
        Popen('python launch.py')

    def input_close(self):
        self.close()

    def input_naca_type(self):
        input_naca_text = self.nacainput.text()
        input_point_text = self.pointinput.text()

        X, Y = airfoil_funct()
        txty = list(Y)
        txtx = list(X)
        zipxy = zip(X,Y)
        textxy = list(zipxy)

        with open('config.cfg', 'w') as txt_file:
            txt_file.write("%s\n" % input_naca_text)
            txt_file.write("%s\n" % input_point_text)

            for item in textxy:
                txt_file.write("%s %s\n" % item)
        txt_file.close()

class PropertiesWindow(QDialog):
    def __init__(self):
        super(PropertiesWindow, self).__init__()
        self.setFixedSize(400,500)
        self.setWindowTitle('Properties')

        with open('config.cfg') as txt_file:
            naca_properties = txt_file.read()

        layout = QVBoxLayout()
        self.naca_prop = QTextEdit(naca_properties)
        self.naca_prop.show()
        layout.addWidget(self.naca_prop)

        self.setLayout(layout)
        self.show()

class FoilCanvas(FigureCanvas):
    def __init__(self, parent=None):
        fig = Figure(figsize=(6.4, 5), dpi=100)
        self.axes = fig.add_subplot(111)
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.airfoil()

    def airfoil(self, finite_TE = False, half_cosine_spacing = False):
        file_input = open('config.cfg', mode='r')
        type_line = file_input.readlines()
        read_type = type_line[0]
        read_node = type_line[0]
        fileNaca = read_type.replace('\n', '')
        nPoints = read_node.replace('\n', '')

        profNaca = [fileNaca]
        naca_type = len(profNaca)

        ax = self.figure.add_subplot(111)
        ax.set(xlim=(-0.5, 1.75), ylim=(-0.5, 0.5))
        for i,p in enumerate(profNaca):
            X,Y = naca(p, nPoints, finite_TE, half_cosine_spacing)
            ax.plot(X, Y, naca_type)
            ax.get_xaxis().set_visible(False)
            ax.get_yaxis().set_visible(False)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())