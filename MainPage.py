import random
from turtle import delay
from typing_extensions import Self
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import QTimer
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMainWindow
import time
import nga
import sys
import sqlite3
from ctypes.wintypes import POINTL
from distutils.log import WARN
from logging import WARNING
import cv2 as cv
import cvzone
from cvzone.FaceMeshModule import FaceMeshDetector
from win10toast import ToastNotifier
import mediapipe as mp
import screen_brightness_control as sbc
import schedule
import matplotlib.pyplot as plt
import serial
serialInst = serial.Serial('COM6', 9600)


# import mascot_rc
# import new_mascot_rc


# from loginPage import Ui_LoginPage
detector = FaceMeshDetector(maxFaces=1)


conn = sqlite3.connect('user_eye_data.db')
c = conn.cursor()
conn_data = sqlite3.connect('data.db')
cd = conn_data.cursor()


class Ui_MainWindow(object):
    def __init__(self):

        self.dis = 0
        self.brightness = ''
        self.username = ''
        self.user_age = 0
        self.eye = ''
        self.count = 0
        self.time = 1
        self.avg_dis = 0
        self.avg_br = 0

    def Stop_camera(self):
        cd.execute('DELETE FROM data;')
        conn_data.commit()
        print("Deleted Database")
        print("Stop")
        sys.exit()

    def displayImage(self, img, window=1):
        qformat = QImage.Format_Indexed8
        if len(img.shape) == 3:
            if img.shape[2] == 4:
                qformat = QImage.Format_RGBA8888
            else:
                qformat = QImage.Format_RGB888
        outImage = QImage(img, img.shape[1],
                          img.shape[0], img.strides[0], qformat)

        outImage = outImage.rgbSwapped()
        self.photo.setPixmap(QPixmap.fromImage(outImage))
        self.photo.setScaledContents(True)

    def showResult(self):
        if self.dis == 0:
            print('Distance: 0 cm')
        else:
            print("Distance: " + str(int(self.dis)))
            result = 0
            result = self.dis
            self.dis_text.setText(str(int(result)) + ' cm')
            self.bright_text.setText(self.brightness + ' lumen')
            cd.execute('INSERT INTO data( distance, warning_count, bright) VALUES ( ?, ?, ?)', [
                       self.dis, self.count, self.brightness])
            conn_data.commit()
        self.count = self.count + 1

    def bright_control(self):
        if serialInst.in_waiting:
            packet = serialInst.readline()
            self.brightness = packet.decode('utf-8').rstrip()
        dim_light = range(0, 50, 1)
        medium_light = range(51, 120, 1)
        bright_light = range(121, 1000, 1)
        temp = float(self.brightness)
        if int(temp) in dim_light:
            sbc.set_brightness(20)
        if int(temp) in medium_light:
            sbc.set_brightness(50)
        if int(temp) in bright_light:
            sbc.set_brightness(100)

    def draw_graph(self):

        mycursor = conn_data.cursor()
        # Fecthing Data From mysql to my python progame
        mycursor.execute("select distance, warning_count from data")
        result = mycursor.fetchall
        Dis = []
        Time = []
        thres = [40] * self.count
        for i in mycursor:
            Dis.append(i[0])
            Time.append(i[1])

        # Visulizing Data using Matplotlib
        plt.plot(Time, Dis)
        plt.plot(Time, thres)
        plt.ylim(0, 90)
        plt.xlabel("Time (s)")
        plt.ylabel("Distance (cm)")
        plt.title("Distance Graph")
        plt.show()
        mycursor.execute("select AVG(distance), AVG(bright) from data")
        for j in mycursor:
            self.avg_dis = j[0]
            self.avg_br = j[1]

        print(self.avg_dis)
        print(self.avg_br)
        toaster = ToastNotifier()
        if self.avg_dis <= 40:
            toaster.show_toast(
                "WARNING", "YOU ARE SO CLOSE TO THE MONITOR", duration=2)
        else:
            toaster.show_toast(
                "WARNING", "YOU ARE DOING GREAT", duration=2)

    def onClicked(self):
        cap = cv.VideoCapture(0)
        # Sau mỗi 2 giây lại lấy 1 mẫu
        schedule.every(1).seconds.do(self.showResult)
        while (cap.isOpened()):
            self.bright_control()
            schedule.run_pending()
            success, img = cap.read()
            if success == True:
                img, faces = detector.findFaceMesh(img, draw=False)
                if faces:
                    face = faces[0]
                    pointLeft = face[145]
                    pointRight = face[374]
                    w, _ = detector.findDistance(pointLeft, pointRight)
                    W = 7
                    f = 600
                    self.dis = (W*f)/w
                    cvzone.putTextRect(img, f"Distance: {int(self.dis)}cm", (50, 50),
                                       scale=2)

            self.displayImage(img, 1)
            cv.waitKey()

        cap.release()
        cv.destroyAllWindows()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1186, 881)
        MainWindow.setStyleSheet("QWidget#centralwidget{\n"
                                 "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 194, 218, 255), stop:1 rgba(255, 255, 255, 255))}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(20, 40, 321, 91))
        font = QtGui.QFont()
        font.setFamily("SVN-Beast")
        font.setPointSize(26)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.title.setFont(font)
        self.title.setMouseTracking(True)
        self.title.setStyleSheet("QWidget#widget\n"
                                 "")
        self.title.setFrameShadow(QtWidgets.QFrame.Plain)
        self.title.setTextFormat(QtCore.Qt.AutoText)
        self.title.setObjectName("title")
        self.title_user_in4 = QtWidgets.QLabel(self.centralwidget)
        self.title_user_in4.setGeometry(QtCore.QRect(730, 70, 381, 51))
        font = QtGui.QFont()
        font.setFamily("SVN-Beast")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.title_user_in4.setFont(font)
        self.title_user_in4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.title_user_in4.setObjectName("title_user_in4")
        self.photo = QtWidgets.QLabel(self.centralwidget)
        self.photo.setGeometry(QtCore.QRect(15, 140, 580, 430))
        font = QtGui.QFont()
        font.setUnderline(False)
        self.photo.setFont(font)
        self.photo.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.photo.setFrameShadow(QtWidgets.QFrame.Plain)
        self.photo.setLineWidth(0)
        self.photo.setText("")
        self.photo.setObjectName("photo")
        self.username = QtWidgets.QLabel(self.centralwidget)
        self.username.setGeometry(QtCore.QRect(650, 130, 141, 61))
        font = QtGui.QFont()
        font.setFamily("SVN-Beast")
        font.setPointSize(16)
        self.username.setFont(font)
        self.username.setObjectName("username")
        self.age = QtWidgets.QLabel(self.centralwidget)
        self.age.setGeometry(QtCore.QRect(650, 180, 111, 51))
        font = QtGui.QFont()
        font.setFamily("SVN-Beast")
        font.setPointSize(16)
        self.age.setFont(font)
        self.age.setObjectName("age")
        self.eye = QtWidgets.QLabel(self.centralwidget)
        self.eye.setGeometry(QtCore.QRect(650, 220, 241, 51))
        font = QtGui.QFont()
        font.setFamily("SVN-Beast")
        font.setPointSize(16)
        self.eye.setFont(font)
        self.eye.setObjectName("eye")
        self.result = QtWidgets.QLabel(self.centralwidget)
        self.result.setGeometry(QtCore.QRect(760, 310, 301, 41))
        font = QtGui.QFont()
        font.setFamily("SVN-Beast")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.result.setFont(font)
        self.result.setObjectName("result")
        self.distance = QtWidgets.QLabel(self.centralwidget)
        self.distance.setGeometry(QtCore.QRect(650, 380, 111, 31))
        font = QtGui.QFont()
        font.setFamily("SVN-Beast")
        font.setPointSize(16)
        self.distance.setFont(font)
        self.distance.setObjectName("distance")
        self.bright = QtWidgets.QLabel(self.centralwidget)
        self.bright.setGeometry(QtCore.QRect(650, 420, 141, 41))
        font = QtGui.QFont()
        font.setFamily("SVN-Beast")
        font.setPointSize(16)
        self.bright.setFont(font)
        self.bright.setObjectName("bright")
        self.start = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.onClicked())
        self.start.setGeometry(QtCore.QRect(150, 600, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.start.setFont(font)
        self.start.setStyleSheet("border-radius:20px;\n"
                                 "background-color: rgb(170, 255, 255)")
        self.start.setObjectName("start")
        self.stop = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.Stop_camera())
        self.stop.setGeometry(QtCore.QRect(330, 600, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.stop.setFont(font)
        self.stop.setStyleSheet("border-radius:20px;\n"
                                "background-color: rgb(170, 255, 255)")
        self.stop.setObjectName("stop")
        self.show_result = QtWidgets.QPushButton(
            self.centralwidget, clicked=lambda: self.draw_graph())
        self.show_result.setGeometry(QtCore.QRect(780, 490, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.show_result.setFont(font)
        self.show_result.setStyleSheet("border-radius:20px;\n"
                                       "background-color: rgb(170, 255, 255)")
        self.show_result.setObjectName("show_result")
        self.name_text = QtWidgets.QTextBrowser(self.centralwidget)
        self.name_text.setGeometry(QtCore.QRect(740, 150, 331, 31))
        font = QtGui.QFont()
        font.setFamily("SVN-Beast")
        font.setPointSize(16)
        self.name_text.setFont(font)
        self.name_text.setObjectName("name_text")
        self.age_text = QtWidgets.QTextBrowser(self.centralwidget)
        self.age_text.setGeometry(QtCore.QRect(740, 190, 331, 31))
        font = QtGui.QFont()
        font.setFamily("SVN-Beast")
        font.setPointSize(16)
        self.age_text.setFont(font)
        self.age_text.setObjectName("age_text")
        self.eye_text = QtWidgets.QTextBrowser(self.centralwidget)
        self.eye_text.setGeometry(QtCore.QRect(810, 230, 261, 31))
        font = QtGui.QFont()
        font.setFamily("SVN-Beast")
        font.setPointSize(16)
        self.eye_text.setFont(font)
        self.eye_text.setObjectName("eye_text")
        self.dis_text = QtWidgets.QTextBrowser(self.centralwidget)
        self.dis_text.setGeometry(QtCore.QRect(760, 380, 91, 31))
        font = QtGui.QFont()
        font.setFamily("SVN-Beast")
        font.setPointSize(16)
        self.dis_text.setFont(font)
        self.dis_text.setObjectName("dis_text")
        self.bright_text = QtWidgets.QTextBrowser(self.centralwidget)
        self.bright_text.setGeometry(QtCore.QRect(770, 420, 81, 31))
        font = QtGui.QFont()
        font.setFamily("SVN-Beast")
        font.setPointSize(16)
        self.bright_text.setFont(font)
        self.bright_text.setObjectName("bright_text")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(920, 560, 331, 291))
        self.label.setObjectName("label")
        self.title_user_in4.raise_()
        self.photo.raise_()
        self.username.raise_()
        self.age.raise_()
        self.eye.raise_()
        self.result.raise_()
        self.distance.raise_()
        self.bright.raise_()
        self.start.raise_()
        self.stop.raise_()
        self.show_result.raise_()
        self.title.raise_()
        self.age_text.raise_()
        self.eye_text.raise_()
        self.dis_text.raise_()
        self.bright_text.raise_()
        self.name_text.raise_()
        self.label.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1186, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        MainWindow.setWhatsThis(_translate(
            "MainWindow", "<html><head/><body><p><img src=\":/newPrefix/mascot.jpg\"/></p></body></html>"))
        self.title.setText(_translate("MainWindow", "Eye Protector"))
        self.title_user_in4.setText(
            _translate("MainWindow", "User Information"))
        self.username.setText(_translate("MainWindow", "Name:"))
        self.age.setText(_translate("MainWindow", "Age:"))
        self.eye.setText(_translate("MainWindow", "Eye problem:"))
        self.result.setText(_translate("MainWindow", "Measurement"))
        self.distance.setText(_translate("MainWindow", "Distance: "))
        self.bright.setText(_translate("MainWindow", "Brightness:"))
        self.start.setText(_translate("MainWindow", "Start"))
        self.stop.setText(_translate("MainWindow", "Stop"))
        self.show_result.setText(_translate("MainWindow", "Show result"))
        self.label.setText(_translate(
            "MainWindow", "<html><head/><body><p><img src=\":/newPrefix/nga.png\"/></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
