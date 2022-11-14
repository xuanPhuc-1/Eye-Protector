import sqlite3
import phuc_rc
from PyQt5 import QtCore, QtGui, QtWidgets

conn = sqlite3.connect('user_eye_data.db')
c = conn.cursor()


class Ui_regPage(object):
    def __init__(self):

        self.name = ''
        self.passw = ''
        self.account = ''
        self.numberofage = 0
        self.eyeproblem = ''

    def Reg(self):
        self.RegSucces()

    def RegSucces(self):
        conn.commit()

        c.execute('INSERT INTO user_eye_data( account, password, name, age, eye_disease) VALUES ( ?, ?, ?, ?, ?)', [
                  self.username_text.text(), self.password_text.text(), self.name_text.text(), self.age_text.text(), self.eye_text.text()])
        print("Regsister Completed")

    def setupUi(self, regPage):
        regPage.setObjectName("regPage")
        regPage.resize(1110, 821)
        regPage.setStyleSheet("QWidget#centralwidget{\n"
                              "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 194, 218, 255), stop:1 rgba(255, 255, 255, 255))}\n"
                              "")
        self.centralwidget = QtWidgets.QWidget(regPage)
        self.centralwidget.setObjectName("centralwidget")
        self.welcom_title = QtWidgets.QLabel(self.centralwidget)
        self.welcom_title.setGeometry(QtCore.QRect(40, 20, 600, 80))
        font = QtGui.QFont()
        font.setFamily("SVN-Beast")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.welcom_title.setFont(font)
        self.welcom_title.setStyleSheet("color: rgb(0, 0,0);")
        self.welcom_title.setObjectName("welcom_title")
        self.welcom_title_2 = QtWidgets.QLabel(self.centralwidget)
        self.welcom_title_2.setGeometry(QtCore.QRect(40, 80, 861, 80))
        font = QtGui.QFont()
        font.setFamily("SVN-Beast")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.welcom_title_2.setFont(font)
        self.welcom_title_2.setStyleSheet("color: rgb(0, 0,0);")
        self.welcom_title_2.setObjectName("welcom_title_2")
        self.icon_phuc = QtWidgets.QLabel(self.centralwidget)
        self.icon_phuc.setGeometry(QtCore.QRect(710, 350, 461, 431))
        self.icon_phuc.setObjectName("icon_phuc")
        self.name_dk = QtWidgets.QLabel(self.centralwidget)
        self.name_dk.setGeometry(QtCore.QRect(510, 180, 131, 31))
        font = QtGui.QFont()
        font.setFamily("SVN-Beast")
        font.setPointSize(15)
        self.name_dk.setFont(font)
        self.name_dk.setObjectName("name_dk")
        self.age_dk = QtWidgets.QLabel(self.centralwidget)
        self.age_dk.setGeometry(QtCore.QRect(530, 250, 131, 31))
        font = QtGui.QFont()
        font.setFamily("SVN-Beast")
        font.setPointSize(15)
        self.age_dk.setFont(font)
        self.age_dk.setObjectName("age_dk")
        self.eye_problems_dk = QtWidgets.QLabel(self.centralwidget)
        self.eye_problems_dk.setGeometry(QtCore.QRect(40, 320, 221, 31))
        font = QtGui.QFont()
        font.setFamily("SVN-Beast")
        font.setPointSize(15)
        self.eye_problems_dk.setFont(font)
        self.eye_problems_dk.setObjectName("eye_problems_dk")
        self.username_dk = QtWidgets.QLabel(self.centralwidget)
        self.username_dk.setGeometry(QtCore.QRect(40, 180, 131, 31))
        font = QtGui.QFont()
        font.setFamily("SVN-Beast")
        font.setPointSize(15)
        self.username_dk.setFont(font)
        self.username_dk.setObjectName("username_dk")
        self.password_dk = QtWidgets.QLabel(self.centralwidget)
        self.password_dk.setGeometry(QtCore.QRect(40, 250, 131, 31))
        font = QtGui.QFont()
        font.setFamily("SVN-Beast")
        font.setPointSize(15)
        self.password_dk.setFont(font)
        self.password_dk.setObjectName("password_dk")
        self.sign_up = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.RegSucces())  # click to reg
        self.sign_up.setGeometry(QtCore.QRect(350, 380, 341, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.sign_up.setFont(font)
        self.sign_up.setStyleSheet("border-radius:20px;\n"
                                   "background-color: rgb(170, 255, 255)")
        self.sign_up.setObjectName("sign_up")
        self.username_text = QtWidgets.QLineEdit(self.centralwidget)
        self.username_text.setGeometry(QtCore.QRect(160, 180, 301, 41))
        font = QtGui.QFont()
        font.setFamily("SVN-Beast")
        font.setPointSize(15)
        self.username_text.setFont(font)
        self.username_text.setStyleSheet("background-color: rgba(0,0,0,0);")
        self.username_text.setObjectName("username_text")
        self.password_text = QtWidgets.QLineEdit(self.centralwidget)
        self.password_text.setGeometry(QtCore.QRect(160, 250, 301, 41))
        font = QtGui.QFont()
        font.setFamily("SVN-Beast")
        font.setPointSize(15)
        self.password_text.setFont(font)
        self.password_text.setStyleSheet("background-color: rgba(0,0,0,0);")
        self.password_text.setObjectName("password_text")
        self.eye_text = QtWidgets.QLineEdit(self.centralwidget)
        self.eye_text.setGeometry(QtCore.QRect(200, 320, 261, 41))
        font = QtGui.QFont()
        font.setFamily("SVN-Beast")
        font.setPointSize(15)
        self.eye_text.setFont(font)
        self.eye_text.setStyleSheet("background-color: rgba(0,0,0,0);")
        self.eye_text.setObjectName("eye_text")
        self.name_text = QtWidgets.QLineEdit(self.centralwidget)
        self.name_text.setGeometry(QtCore.QRect(650, 180, 301, 41))
        font = QtGui.QFont()
        font.setFamily("SVN-Beast")
        font.setPointSize(15)
        self.name_text.setFont(font)
        self.name_text.setStyleSheet("background-color: rgba(0,0,0,0);")
        self.name_text.setObjectName("name_text")
        self.age_text = QtWidgets.QLineEdit(self.centralwidget)
        self.age_text.setGeometry(QtCore.QRect(650, 250, 301, 41))
        font = QtGui.QFont()
        font.setFamily("SVN-Beast")
        font.setPointSize(15)
        self.age_text.setFont(font)
        self.age_text.setStyleSheet("background-color: rgba(0,0,0,0);")
        self.age_text.setObjectName("age_text")
        regPage.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(regPage)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1110, 21))
        self.menubar.setObjectName("menubar")
        regPage.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(regPage)
        self.statusbar.setObjectName("statusbar")
        regPage.setStatusBar(self.statusbar)

        self.retranslateUi(regPage)
        QtCore.QMetaObject.connectSlotsByName(regPage)

    def retranslateUi(self, regPage):
        _translate = QtCore.QCoreApplication.translate
        regPage.setWindowTitle(_translate("regPage", "MainWindow"))
        self.welcom_title.setText(_translate(
            "regPage", "Fill in your profile"))
        self.welcom_title_2.setText(_translate(
            "regPage", "Now that you\'re created an account, please fill in your profile"))
        self.icon_phuc.setText(_translate(
            "regPage", "<html><head/><body><p><img src=\":/newPrefix/phuc (1).png\"/></p></body></html>"))
        self.name_dk.setText(_translate("regPage", "Your Name:"))
        self.age_dk.setText(_translate("regPage", "Your Age:"))
        self.eye_problems_dk.setText(_translate("regPage", "Eye Problems:"))
        self.username_dk.setText(_translate("regPage", "Username:"))
        self.password_dk.setText(_translate("regPage", "Password:"))
        self.sign_up.setText(_translate("regPage", "Sign Up"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    regPage = QtWidgets.QMainWindow()
    ui = Ui_regPage()
    ui.setupUi(regPage)
    regPage.show()
    sys.exit(app.exec_())
