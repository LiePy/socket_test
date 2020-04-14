# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'queryHost.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import sys
import socket
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(359, 361)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 46, 72, 15))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 75, 72, 15))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(90, 40, 161, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(90, 70, 161, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(260, 30, 61, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(260, 70, 61, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 120, 72, 15))
        self.label_3.setObjectName("label_3")
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(30, 140, 291, 121))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(50, 310, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(220, 310, 93, 28))
        self.pushButton_4.setObjectName("pushButton_4")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(30, 110, 291, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "域名："))
        self.label_2.setText(_translate("Dialog", "IP地址："))
        self.pushButton.setText(_translate("Dialog", "查询"))
        self.pushButton_2.setText(_translate("Dialog", "查询"))
        self.label_3.setText(_translate("Dialog", "主机信息："))
        self.pushButton_3.setText(_translate("Dialog", "确定"))
        self.pushButton_4.setText(_translate("Dialog", "取消"))
        self.pushButton.clicked.connect(self.click_ym)      # 设置按钮关联动作
        self.pushButton_2.clicked.connect(self.click_ip)     # 设置按钮关联动作

    def click_ym(self):
        ym = self.lineEdit.text()       # 获取域名输入内容
        if len(ym)==0:      # 输入为空时返回本机信息
            ym2 = socket.gethostname()
        else:
            ym2 =ym
        try:
            # info = socket.getaddrinfo(ym2, None)     # 域名转IP地址
            # ip = info[0][4][0]
            ip = socket.gethostbyname(ym2)
        except Exception as e:
            print(e)
        else:
            self.lineEdit_2.setText(ip)     # 显示信息
            textView = '主机名：' + ym +'\nIP地址：' + ip + '\n作者：15计算机' \
                                                     '172班 03号 王磊'
            self.textBrowser.setText(textView)      # 显示信息
            self.lineEdit.setText(ym2)      # 显示信息

    def click_ip(self):
        ip = self.lineEdit_2.text()     # 获取IP输入内容
        if len(ip)==0:      # 输入为空时返回本机信息
            ym = socket.gethostname()
            ip = socket.gethostbyname(ym)
        else:
            try:
                info = socket.gethostbyaddr(ip)
                ym = info[0]
            except Exception as e:
                print(e)
        self.lineEdit.setText(ym)       # 显示信息
        self.lineEdit_2.setText(ip)     # 显示信息
        textView = '主机名：' + ym +'\nIP地址：' + ip + '\n作者：15计算机' \
                                                 '172班 03号 王磊'
        self.textBrowser.setText(textView)      # 显示信息



if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_Dialog()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
