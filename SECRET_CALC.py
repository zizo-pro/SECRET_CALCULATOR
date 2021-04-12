from PyQt5 import QtWidgets
from PyQt5.uic import loadUiType
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from os import path
from sys import argv , exit
from dataconv import Ui_Form
from discount import Ui
from area import area
FORM_CLASS,_=loadUiType(path.join(path.dirname(__file__),"SECRET_CALC.ui"))

class mainapp(QMainWindow,FORM_CLASS):
    def __init__(self, parent=None):
        super(mainapp,self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.button_setup()
        self.data_conv.setIcon(QIcon("/home/ziad/Desktop/SECRET_calc/icons/area.png"))
        self.discount.setIcon(QIcon("/home/ziad/Desktop/SECRET_calc/icons/discount.png"))

    def no0 (self):
        self.lineEdit.setText(f"{self.lineEdit.text()}0")

    def no1 (self):
        self.lineEdit.setText(f"{self.lineEdit.text()}1")

    def no2 (self):
        self.lineEdit.setText(f"{self.lineEdit.text()}2")

    def no3 (self):
        self.lineEdit.setText(f"{self.lineEdit.text()}3")

    def no4 (self):
        self.lineEdit.setText(f"{self.lineEdit.text()}4")

    def no5 (self):
        self.lineEdit.setText(f"{self.lineEdit.text()}5")

    def no6 (self):
        self.lineEdit.setText(f"{self.lineEdit.text()}6")

    def no7 (self):
        self.lineEdit.setText(f"{self.lineEdit.text()}7")

    def no8 (self):
        self.lineEdit.setText(f"{self.lineEdit.text()}8")

    def no9 (self):
        self.lineEdit.setText(f"{self.lineEdit.text()}9")

    def divide (self):
        self.lineEdit.setText(f"{self.lineEdit.text()}/")

    def times (self):
        self.lineEdit.setText(f"{self.lineEdit.text()}*")

    def plus (self):
        self.lineEdit.setText(f"{self.lineEdit.text()}+")

    def minus (self):
        self.lineEdit.setText(f"{self.lineEdit.text()}-")

    def percent (self):
        self.lineEdit.setText(f"{self.lineEdit.text()}%")

    def dot (self):
        self.lineEdit.setText(f"{self.lineEdit.text()}.")

    def delete(self):
        self.lineEdit.setText(self.lineEdit.text()[:-1])

    def clear(self):
        self.lineEdit.setText("")

    def equal(self):
        try:
            self.lineEdit.setText(str(eval(self.lineEdit.text())))
        except SyntaxError:
            self.lineEdit.setText("MATH ERROR")
    
    def dataconv_window(self):
        self.window2 = QtWidgets.QMainWindow()
        self.ui = Ui_Form()
        self.ui.setupUi(self.window2)
        self.window2.show()
        window.hide()

    def discount_window(self):
        self.window3 = QtWidgets.QMainWindow()
        self.ui1 = Ui()
        self.ui1.setupUi(self.window3)
        self.window3.show()
        window.hide()

    def area_window(self):
        self.window4 = QtWidgets.QMainWindow()
        self.ui1 = area()
        self.ui1.setupUi(self.window4)
        self.window4.show()
        window.hide()

    def button_setup(self):
        self.norm_del.clicked.connect(self.delete)
        self.norm_0.clicked.connect(self.no0)
        self.norm_1.clicked.connect(self.no1)
        self.norm_2.clicked.connect(self.no2)
        self.norm_3.clicked.connect(self.no3)
        self.norm_4.clicked.connect(self.no4)
        self.norm_5.clicked.connect(self.no5)
        self.norm_6.clicked.connect(self.no6)
        self.norm_7.clicked.connect(self.no7)
        self.norm_8.clicked.connect(self.no8)
        self.norm_9.clicked.connect(self.no9)
        self.norm_dot.clicked.connect(self.dot)
        self.norm_times.clicked.connect(self.times)
        self.norm_divide.clicked.connect(self.divide)
        self.norm_percent.clicked.connect(self.percent)
        self.norm_plus.clicked.connect(self.plus)
        self.norm_minus.clicked.connect(self.minus)
        self.norm_clear.clicked.connect(self.clear)
        self.norm_equal.clicked.connect(self.equal)
        self.data_conv.clicked.connect(self.dataconv_window)
        self.discount.clicked.connect(self.discount_window)
        self.area.clicked.connect(self.area_window)

if __name__ == "__main__":
    app = QApplication(argv)
    MainWindow = QtWidgets.QMainWindow()
    window = mainapp()
    window.show()
    app.exec()