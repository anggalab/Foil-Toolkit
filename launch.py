import sys
import os

from PySide2 import QtCore, QtGui
from PySide2.QtWidgets import QApplication, QMessageBox, QFileDialog, QMainWindow, QDialog, QLineEdit, QPushButton, QStatusBar, QTextEdit, QWidget, QAction, QKeySequenceEdit, QMenuBar, QMenu, QSizePolicy, QDesktopWidget, QVBoxLayout, QPushButton, QLabel
from PySide2.QtGui import QIcon, QKeySequence

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

import matplotlib.pyplot as plt
import numpy as np

from airfoilplot import airfoil_plot
from airfoilplot import naca

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.title = 'Foil Toolkit'
        self.width = 500
        self.height = 500
        self.setFixedSize(self.size())
        self.setWindowIcon(QIcon('img/'))
        self.Skin()
        self.komponen()
#        self.center()
    
    def inputwindowform(self):
        self.input_window = InputWindow()
        self.input_window.show()

#    def center(self):
#        qRect = self.frameGeometry()
#        centerPoint = QDesktopWidget().availableGeometry().center()
#        qRect.moveCenter(centerPoint)
#        self.move(qRect.topLeft())

    def Skin(self):
        self.setWindowTitle(self.title)
        self.setGeometry(0, 0, self.width, self.height)
        m = PlotCanvas(self, width=6.4, height=5)
        m.move(0, 0)
        self.show()
    
    def CreateMenus(self):
        self.fileMenu = self.menuBar().addMenu("&File")
        self.editMenu = self.menuBar().addMenu("&Edit")
        self.optionMenu = self.menuBar().addMenu("&Option")
        self.helpMenu = self.menuBar().addMenu("&Help")

    def komponen(self):
        self.CreateActions()
        self.CreateMenus()
        self.CreateToolBar()

        self.fileMenu.addAction(self.newAction)
        self.fileMenu.addAction(self.DxfAction)
        self.fileMenu.addAction(self.DatAction)
        self.fileMenu.addAction(self.TxtAction)

        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.exitAction)
        self.optionMenu.addAction(self.inputAction)
        self.editMenu.addAction(self.undoAction)
        self.editMenu.addAction(self.redoAction)
        
        self.fileMenu.addSeparator()
        self.helpMenu.addAction(self.aboutAction)

        self.mainToolBar.addAction(self.newAction)
        self.mainToolBar.addAction(self.DxfAction)
        self.mainToolBar.addAction(self.TxtAction)
        self.mainToolBar.addAction(self.DatAction)
        
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(self.undoAction)
        self.mainToolBar.addAction(self.redoAction)

    def CreateActions(self):
        self.newAction = QAction( QIcon('img/new.png'), '&New Project', self, shortcut=QKeySequence.New, statusTip="Create a New File", triggered=self.newFile)
        self.exitAction = QAction( QIcon('img/exit.png'), 'E&xit', self, shortcut="Ctrl+Q", statusTip="Exit the Application", triggered=self.exitFile)
        self.aboutAction = QAction( QIcon('img/about.png'), 'A&bout', self, statusTip="Displays info about text editor", triggered=self.showAbout)
        self.DatAction = QAction( QIcon('img/save.png'), '&Save as DAT', self, statusTip="Save the current file to disk")
        self.TxtAction = QAction( QIcon('img/save.png'), '&Save as TXT', self, statusTip="Save the current file to disk")
        self.DxfAction = QAction( QIcon('img/save.png'), '&Save as DXF', self, statusTip="Save the current file to disk")
        self.cutAction = QAction( QIcon('img/cut.png'), 'C&ut', self, statusTip="Cut the current selection to clipboard")
        self.redoAction = QAction( QIcon('img/redo.png'),'Redo', self, statusTip="Redo previous action")
        self.undoAction = QAction( QIcon('img/undo.png'),'Undo', self,  statusTip="Undo previous action")
        self.inputAction = QAction( QIcon('img/redo.png'),'Foil', self, statusTip="Redo previous action", triggered=self.inputwindowform)

    def newFile(self):
        self.textEdit.setText('')

    def exitFile(self):
        self.close()

    def openFile(self): 
        self.fileName, self.filterName = QFileDialog.getOpenFileName(self)
        self.textEdit.setText(open(self.fileName).read())

    def saveFile(self):
        if self.fileName == None or self.fileName == '':
            self.fileName, self.filterName = QFileDialog.getSaveFileName(self, filter=self.filters)
        if(self.fileName != ''):
            file = open(self.fileName, 'w')
            file.write(self.textEdit.toPlainText())
            self.statusBar().showMessage("File saved", 2000)

    def CreateToolBar(self):
        self.mainToolBar = self.addToolBar('Main')

    def showAbout(self):
        QMessageBox.about(self, "about",  "Foil Toolkit v0.1 is airfoil plotter written with Python")

class InputWindow(QDialog):
    def __init__(self):
        super(InputWindow, self).__init__()
        self.setFixedSize(220,180)
        self.setWindowTitle('Input NACA')

        layout = QVBoxLayout()

        self.labelnaca = QLabel("NACA Type")
        self.labelnaca.show()
        layout.addWidget(self.labelnaca)

        self.nacainput = QLineEdit()
        self.nacainput.setText('6409')
        self.nacainput.show()
        layout.addWidget(self.nacainput)

        self.labelpoint = QLabel("Point Plot")
        self.labelpoint.show()
        layout.addWidget(self.labelpoint)

        self.pointinput = QLineEdit()
        self.pointinput.setText("400")
        self.pointinput.show()
        layout.addWidget(self.pointinput)

        self.plotBtn = QPushButton("Plot")
        self.plotBtn.clicked.connect(self.input_naca_point)
        self.plotBtn.clicked.connect(self.input_naca_type)
        self.plotBtn.show()
        layout.addWidget(self.plotBtn)

        self.cancelBtn = QPushButton("Close")
        self.cancelBtn.clicked.connect(self.input_close)
        self.cancelBtn.show()
        layout.addWidget(self.cancelBtn)
        
        self.setLayout(layout)
        self.show()

    def input_close(self):
        self.close()

    def input_naca_point(self):
        input_point_text = self.pointinput.text()
        input_point_text = int(input_point_text)
        return input_point_text

    def input_naca_type(self):
        input_naca_text = self.nacainput.text()
        return input_naca_text

class PlotCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.airfoil()

    def airfoil(self, finite_TE = False, half_cosine_spacing = False):
        trans_var = InputWindow()
        nPoints = trans_var.input_naca_point()
        profNaca = trans_var.input_naca_type()
        profNaca = [profNaca]
        naca_type = len(profNaca)

        ax = self.figure.add_subplot(111)
        ax.set(xlim=(-0.5, 1.75), ylim=(-0.5, 0.5))
        for i,p in enumerate(profNaca):
            X,Y = naca(p, nPoints, finite_TE, half_cosine_spacing)
            ax.plot(X, Y, naca_type)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())