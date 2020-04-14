# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'client_5.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


import sys
import time
import socket
import threading
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import QThread, pyqtSignal, QDateTime, QObject
from test5.server_5 import BackendThread


class Ui_Dialog(object):
    def __init__(self):
        self.s = socket.socket()
        self.msg = ''

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(651, 346)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(20, 10, 608, 303))
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        # self.lineEdit.setEnabled(False)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_3.setEnabled(False)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_2.addWidget(self.lineEdit_3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout_3.addWidget(self.lineEdit_4)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_2.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_2.addWidget(self.pushButton_3)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.textBrowser = QtWidgets.QTextBrowser(self.widget)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_3.addWidget(self.textBrowser)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "客户端"))
        self.label.setText(_translate("Dialog", "客户名："))
        self.lineEdit.setText(_translate("Dialog", "Eric"))
        self.label_2.setText(_translate("Dialog", "服务器名："))
        self.lineEdit_2.setText(_translate("Dialog", "127.0.0.1"))
        self.label_4.setText(_translate("Dialog", "端口号："))
        self.lineEdit_3.setText(_translate("Dialog", "21567"))
        self.label_3.setText(_translate("Dialog", "消息："))
        self.pushButton.setText(_translate("Dialog", "退出"))
        self.pushButton_2.setText(_translate("Dialog", "连接"))
        self.pushButton_3.setText(_translate("Dialog", "发送"))
        self.pushButton_3.setShortcut(QtCore.Qt.Key_Return)     # 回车键发送
        self.pushButton.clicked.connect(self.break_button)
        self.pushButton_2.clicked.connect(self.connect_button)
        self.pushButton_3.clicked.connect(self.send_button)
        self.pushButton.setEnabled(False)
        self.pushButton_3.setEnabled(False)

        # 调用自定义类，同server_4
        self.backend = BackendThread()
        self.backend.update_date.connect(self.handleDisplay)
        self.thread = QThread()  # 创建进程
        self.backend.moveToThread(self.thread)
        self.thread.started.connect(self.backend.run)
        self.thread.start()

    def connect_button(self):  # 连接按钮
        try:
            name = self.lineEdit.text()
            add1 = self.lineEdit_2.text()
            add2 = self.lineEdit_3.text()
            self.s = socket.socket()
            self.s.connect((add1, int(add2)))
            print('已连接到服务器')
            self.msg += '连接成功~\n您已进入聊天室\n'+'*'*74+'\n'
            self.textBrowser.setText(self.msg)
            self.s.send('[{}]{}进入聊天室~\n'.format(time.ctime(), name).encode('GB2312'))
            t = threading.Thread(target=self.rec_msg)
            t.start()
            self.pushButton.setEnabled(True)
            self.pushButton_2.setEnabled(False)
            self.pushButton_3.setEnabled(True)
        except:
            self.msg += '服务器未开放！'
            print('服务器未开放！')

    def break_button(self):  # 断开按钮
        name = self.lineEdit.text()
        self.s.send('[{}]{}退出聊天室'.format(time.ctime(), name).encode('GB2312'))
        self.s.close()
        print('已关闭服务器')
        self.msg += '您已退出登录\n'
        self.textBrowser.setText(self.msg)
        self.pushButton.setEnabled(False)
        self.pushButton_2.setEnabled(True)
        self.pushButton_3.setEnabled(False)

    def send_button(self):  # 发送按钮
        name = self.lineEdit.text()
        MSG = '[' + time.ctime() + ']' + name + ':' + self.lineEdit_4.text() + '\n'
        self.s.send(MSG.encode('GB2312'))
        print('已发送:', MSG)
        self.msg += MSG
        self.lineEdit_4.setText('')

    def handleDisplay(self, data):  # 显示收到的消息
        self.textBrowser.setText(self.msg)
        self.textBrowser.moveCursor(self.textBrowser.textCursor().End)  # 文本框显示到底部

    def rec_msg(self):  # 接受消息
        try:
            while 1:
                print('等待接受消息中。。。')
                msg = self.s.recv(1024).decode('GB2312')
                print('收到消息', msg)
                self.msg += msg
                print(self.msg)
        except ConnectionAbortedError as e1:
            print(e1)
        except ConnectionResetError as e2:
            print(e2)
            self.pushButton.setEnabled(False)
            self.pushButton_2.setEnabled(True)
            self.pushButton_3.setEnabled(False)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_Dialog()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
