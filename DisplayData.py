# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SecondPage.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from firebase import firebase
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QMovie

FBConn = firebase.FirebaseApplication('https://hospital-management-6a752.firebaseio.com/',None)

class Ui_Form2(object):
    home=0
    def setupUi(self, Form):
        self.temp=''
        self.sos=''
        self.moist=''
        self.bpm=''
        Form.setObjectName("Form")
        Form.resize(1300, 680)
        self.run = QTimer()
        self.run.setInterval(200)
        self.run.timeout.connect(self.update)
        self.run.start()
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 1300, 681))
        self.label.setText("")
        #self.label.setPixmap(QtGui.QPixmap("Gui_images/Bed.gif"))
        self.mngif=QMovie("Gui_images/Bed.gif")
        self.label.setMovie(self.mngif)
        self.mngif.start()
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(30, 10, 341, 101))
        self.frame.setStyleSheet("background-color: rgba(170, 0, 127,200);\n"
"background-color: rgb(0, 0, 0);\n"
"\n"
"border-radius:20px")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(30, 30, 181, 41))
        self.comboBox.setStyleSheet("border-radius:20px;\n"
"background-color: rgb(145, 255, 60);\n"
"background-color: rgba(144, 255, 252,200);\n"
"font: 10pt \"Lucida Calligraphy\";")
        self.comboBox.setCurrentText("")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItems(['Bed 1'])
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(220, 30, 111, 41))
        self.pushButton.setStyleSheet("font: 10pt \"Papyrus\";\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(111, 255, 89);\n"
"border-radius:15px\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.check)
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setGeometry(QtCore.QRect(130, 250, 1001, 281))
        self.frame_2.setStyleSheet("\n"
"background-color: rgba(102, 255, 238,170);\n"
"border-radius:30px")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_2.hide()
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(60, 50, 171, 141))
        self.label_2.setStyleSheet("background-color: rgba(255, 255, 255, 100);\n"
"border-radius:20px")
        self.label_2.setText("")
        self.tgif=QMovie("Gui_images/temperature.gif")
        self.label_2.setMovie(self.tgif)
        self.tgif.start()
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(390, 50, 171, 141))
        self.label_3.setStyleSheet("background-color: rgba(255, 255, 255, 100);\n"
"border-radius:20px")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("Gui_images/heart.gif"))
        self.hgif=QMovie("Gui_images/heart.gif")
        self.label_3.setMovie(self.hgif)
        self.hgif.start()
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(720, 50, 171, 141))
        self.label_4.setStyleSheet("background-color: rgba(255, 255, 255, 100);\n"
"border-radius:20px")
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("Gui_images/moisture.gif"))
        self.mgif=QMovie("Gui_images/moisture.gif")
        self.label_4.setMovie(self.mgif)
        self.mgif.start()
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setGeometry(QtCore.QRect(80, 210, 121, 61))
        self.label_5.setStyleSheet("font: 18pt \"MV Boli\";\n"
"background-color: rgba(255, 85, 0,200);\n"
"color: rgb(240, 255,244);\n"
"border-radius:25px")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setGeometry(QtCore.QRect(410, 210, 121, 61))
        self.label_6.setStyleSheet("font: 18pt \"MV Boli\";\n"
"background-color: rgba(255, 85, 0,200);\n"
"color: rgb(240, 255,244);\n"
"border-radius:25px")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setGeometry(QtCore.QRect(740, 210, 121, 61))
        self.label_7.setStyleSheet("font: 18pt \"MV Boli\";\n"
"background-color: rgba(255, 85, 0,200);\n"
"color: rgb(240, 255,244);\n"
"border-radius:25px")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(540, 630, 111, 41))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 93, 44);\n"
"color: rgb(255, 255, 255);\n"
"font: 8pt \"Papyrus\";\n"
"border-radius:15px")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.home)
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(1200, 40, 55, 51))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap(""))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
    
    def home(self):
        self.run.stop()
        Ui_Form2.home=1
    
    def update(self):
        database = FBConn.get('',None)
        self.bpm=database['bpm'][2:-1]
        self.moisture=database['moist']
        self.temp=database['temp']
        self.sos=database['sos']
        print(database)
        
        self.label_5.setText(self._translate("Form", self.temp))
        self.label_6.setText(self._translate("Form", self.bpm))
        self.label_7.setText(self._translate("Form", str(self.moisture)))
        if(self.sos==1):
            self.label_8.setPixmap(QtGui.QPixmap("Gui_images/sos.jpg"))
        else:
            self.label_8.setPixmap(QtGui.QPixmap(""))
            
        
    def check(self):
        self.frame_2.show()
        
    def retranslateUi(self, Form):
        self._translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(self._translate("Form", "Form"))
        self.pushButton.setText(self._translate("Form", "Monitor"))
        self.label_5.setText(self._translate("Form"," "))
        self.label_6.setText(self._translate("Form"," "))
        self.label_7.setText(self._translate("Form"," "))
        self.pushButton_2.setText(self._translate("Form", "LOG OUT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form2()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

