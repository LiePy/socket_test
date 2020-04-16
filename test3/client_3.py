# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import sys
import socket
import threading
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(478, 203)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 30, 91, 16))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(110, 30, 151, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(290, 34, 51, 16))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(340, 30, 113, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 90, 81, 16))
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(110, 90, 241, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 150, 72, 15))
        self.label_4.setObjectName("label_4")
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(110, 145, 241, 21))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(370, 90, 81, 81))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "sendMSG"))
        self.label.setText(_translate("Dialog", "服务器地址："))
        self.label_2.setText(_translate("Dialog", "端口："))
        self.label_3.setText(_translate("Dialog", "发送消息："))
        self.label_4.setText(_translate("Dialog", "反馈消息："))
        self.pushButton.setText(_translate("Dialog", "发送"))
        self.lineEdit.setText("127.0.0.1")
        self.lineEdit_2.setText("21567")
        self.pushButton.clicked.connect(self.sendMSG)

    # def t(self, function):  # 创建新进程
    #     t1 = threading.Thread(target=self.sendMSG, name='button', kwargs=None)
    #     t1.start()      # 启动线程

    def sendMSG(self):      # 按钮触发事件
        addr_1 = self.lineEdit.text()   # 获取服务器地址
        addr_2 = self.lineEdit_2.text()     # 获取端口号
        MSG = self.lineEdit_3.text()        # 获取消息发送框内容
        addr = (addr_1, int(addr_2))    # 地址
        c_socket = socket.socket()      # 创建套接字
        c_socket.connect(addr)      # 连接套接字
        c_socket.send(MSG.encode('GB2312'))     # 发送消息
        rcv_msg = c_socket.recv(1024)       # 接受消息
        self.lineEdit_4.setText(rcv_msg.decode('GB2312'))       # 显示接受的消息




if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_Dialog()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())