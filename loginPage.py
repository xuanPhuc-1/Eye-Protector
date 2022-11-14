import icon_dual
from fileinput import close
from PyQt5 import QtCore, QtGui, QtWidgets
from MainPage import Ui_MainWindow
from RegisterPage import Ui_regPage
import sqlite3

conn = sqlite3.connect('user_eye_data.db')
c = conn.cursor()


class Ui_LoginPage(object):
    def __init__(self):
        self.tendangnhap = ''
        self.matkhau = ''
        self.username = ''
        self.user_age = 0
        self.eye = ''

    def authentication(self):
        cursor = conn.execute("SELECT id, name, age, eye_disease from user_eye_data WHERE account=? and password = ?", [
            self.tendangnhap, self.matkhau])

        row = cursor.fetchone()
        if row == None:
            print("There are no results for this query")
        else:
            self.username = row[1]
            self.user_age = row[2]
            self.eye = row[3]
            self.login_success()

    def input(self):
        conn.commit()
        self.tendangnhap = self.username.text()
        self.matkhau = self.password.text()
        self.authentication()

    def login_success(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.ui.name_text.setText(self.username)
        self.ui.age_text.setText(str(self.user_age))
        self.ui.eye_text.setText(self.eye)
        self.window.show()

    def register(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_regPage()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, LoginPage):
        LoginPage.setObjectName("LoginPage")
        LoginPage.resize(1112, 814)
        LoginPage.setStyleSheet("QWidget#centralwidget{\n"
                                "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 194, 218, 255), stop:1 rgba(255, 255, 255, 255))}")
        self.centralwidget = QtWidgets.QWidget(LoginPage)
        self.centralwidget.setObjectName("centralwidget")
        self.welcom_title = QtWidgets.QLabel(self.centralwidget)
        self.welcom_title.setGeometry(QtCore.QRect(50, 130, 600, 80))
        font = QtGui.QFont()
        font.setFamily("SVN-Beast")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.welcom_title.setFont(font)
        self.welcom_title.setObjectName("welcom_title")
        self.icon_app = QtWidgets.QLabel(self.centralwidget)
        self.icon_app.setGeometry(QtCore.QRect(30, 200, 501, 311))
        self.icon_app.setObjectName("icon_app")
        self.username = QtWidgets.QLineEdit(self.centralwidget)
        self.username.setGeometry(QtCore.QRect(630, 210, 400, 41))
        font = QtGui.QFont()
        font.setFamily("SVN-Beast")
        font.setPointSize(15)
        self.username.setFont(font)
        self.username.setStyleSheet("background-color: rgba(0,0,0,0);\n"
                                    "border: none;\n"
                                    "border-bottom: 2px solid rgba(46, 82, 101, 200);\n"
                                    "color: rgba(0, 0, 0, 240);\n"
                                    "padding-bottom: 7px;")
        self.username.setObjectName("username")
        self.password = QtWidgets.QLineEdit(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(630, 270, 400, 41))
        font = QtGui.QFont()
        font.setFamily("SVN-Beast")
        font.setPointSize(15)
        self.password.setFont(font)
        self.password.setStyleSheet("background-color: rgba(0,0,0,0);\n"
                                    "border: none;\n"
                                    "border-bottom: 2px solid rgba(46, 82, 101, 200);\n"
                                    "color: rgba(0, 0, 0, 240);\n"
                                    "padding-bottom: 7px;")
        self.password.setObjectName("password")
        self.login = QtWidgets.QPushButton(  # Login
            self.centralwidget, clicked=lambda: self.input())
        self.login.setGeometry(QtCore.QRect(630, 370, 401, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.login.setFont(font)
        self.login.setStyleSheet("border-radius:20px;\n"
                                 "background-color: rgb(170, 255, 255)\n"
                                 "")
        self.login.setObjectName("login")
        self.register_2 = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.register())
        self.register_2.setGeometry(QtCore.QRect(630, 440, 401, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.register_2.setFont(font)
        self.register_2.setStyleSheet("border-radius:20px;\n"
                                      "background-color: rgb(255,182,193)\n"
                                      "")
        self.register_2.setObjectName("register_2")
        self.forgor_password = QtWidgets.QPushButton(self.centralwidget)
        self.forgor_password.setGeometry(QtCore.QRect(620, 330, 151, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.forgor_password.setFont(font)
        self.forgor_password.setStyleSheet("\n"
                                           "border: none;\n"
                                           "\n"
                                           "")
        self.forgor_password.setObjectName("forgor_password")
        LoginPage.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(LoginPage)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1112, 21))
        self.menubar.setObjectName("menubar")
        LoginPage.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(LoginPage)
        self.statusbar.setObjectName("statusbar")
        LoginPage.setStatusBar(self.statusbar)

        self.retranslateUi(LoginPage)
        QtCore.QMetaObject.connectSlotsByName(LoginPage)

    def retranslateUi(self, LoginPage):
        _translate = QtCore.QCoreApplication.translate
        LoginPage.setWindowTitle(_translate("LoginPage", "MainWindow"))
        self.welcom_title.setText(_translate(
            "LoginPage", "Welcome to Eye Protector"))
        self.icon_app.setText(_translate(
            "LoginPage", "<html><head/><body><p><img src=\":/newPrefix/icon.png\"/></p></body></html>"))
        self.username.setPlaceholderText(_translate("LoginPage", "Username"))
        self.password.setPlaceholderText(_translate("LoginPage", "Password"))
        self.login.setText(_translate("LoginPage", "Log In"))
        self.register_2.setText(_translate("LoginPage", "Creat New Account"))
        self.forgor_password.setText(
            _translate("LoginPage", "Forgot password?"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginPage = QtWidgets.QMainWindow()
    ui = Ui_LoginPage()
    ui.setupUi(LoginPage)
    LoginPage.show()
    sys.exit(app.exec_())
