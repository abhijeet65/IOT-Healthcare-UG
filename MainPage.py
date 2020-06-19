# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FirstPage.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from firebase import firebase
from PyQt5.QtGui import QMovie
from DisplayData import Ui_Form2
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
FBConn = firebase.FirebaseApplication('https://hospital-management-6a752.firebaseio.com/',None)

class Ui_Form(object):
    def setupUi(self, Form):
        self.usermsg=""
        self.pswmsg=""
        Form.setObjectName("Form")
        Form.resize(1300, 681)
        self.run = QTimer()
        self.run.setInterval(200)
        self.run.timeout.connect(self.status)
        self.run.start()
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, -10, 1300, 681))
        self.label.setText("")
        #self.label.setPixmap(QtGui.QPixmap("Gui_images/health2.gif"))
        self.mngif=QMovie("Gui_images/health2.gif")
        self.label.setMovie(self.mngif)
        self.mngif.start()
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(520, 590, 261, 71))
        self.pushButton.setStyleSheet("color: rgb(0, 0, 0);\n"
"border-radius:30px;\n"
"background-color: rgba(185, 255, 131, 220);\n"
"font: 14pt \"Papyrus\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.loginnow)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(300, 10, 731, 71))
        self.label_2.setStyleSheet("color: rgb(255, 255, 0);\n"
"background-color: rgba(0, 170, 0,220);\n"
"border-radius:30px;\n"
"font: 20pt \"Papyrus\";")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(420, 220, 471, 351))
        self.frame.setStyleSheet("background-color: rgba(125, 171, 255,200);\n"
"border-radius:20px\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(30, 70, 391, 61))
        self.lineEdit_2.setStyleSheet("border-radius:30px;\n"
"font: 14pt \"MV Boli\";\n"
"background-color: rgba(202, 202, 202, 220);\n"
"")
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setPlaceholderText("Enter Username")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(30, 200, 391, 61))
        self.lineEdit.setStyleSheet("border-radius:30px;\n"
"font: 14pt \"MV Boli\";\n"
"background-color: rgba(202, 202, 202, 220);\n"
"")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setPlaceholderText("Enter Password")
       
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(0, 140, 461, 20))
        self.label_3.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"font: 9pt \"Narkisim\";\n"
"color: rgb(255, 102, 56);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(0, 260, 461, 20))
        self.label_4.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"font: 9pt \"Narkisim\";\n"
"color: rgb(255, 102, 56);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
    
    
    def status(self):
        if Ui_Form2.home==1:
            Form.show()
            self.window.close()
            Ui_Form2.home==0
            pass
    def loginnow(self):
        self.usermsg=""
        self.pswmsg=""
        database = FBConn.get('/Login',None)
        user=self.lineEdit_2.text() //gettinginput 
        password=self.lineEdit.text()
        if(len(user)==0):
            self.usermsg="Enter Username"
        elif(len(password)==0):
            self.pswmsg="Enter Password"
        else:
            if(user==database['Username']):
                self.usermsg="Valid User"
                print("Valid")
                if(password==database['Password']):
                    print("LogIn")
                    self.lineEdit.setText('')
                    self.lineEdit_2.setText('')
                    self.window = QtWidgets.QWidget()
                    self.ui = Ui_Form2()
                    self.ui.setupUi(self.window)
                    Form.hide()
                    self.window.show()
                else:
                    self.pswmsg="Unmatched Password"
            else:
                self.usermsg="Invalid User"
                
        self.retranslateUi(Form)        
    
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Hospital Management"))
        self.pushButton.setText(_translate("Form", "LOGIN"))
        self.label_2.setText(_translate("Form", "Hospital Management "))
        #self.pushButton_2.setText(_translate("Form", "Username"))
        #self.pushButton_3.setText(_translate("Form", "Password"))
        self.label_3.setText(_translate("Form", self.usermsg+"*"))
        self.label_4.setText(_translate("Form", self.pswmsg+"*"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

