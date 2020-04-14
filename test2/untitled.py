# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import sys
import socket
import threading
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog


class Ui_Dialog(object):
    sub_threads = []
    def setupUi(self, Dialog):
        Dialog.setObjectName("LocalInfo")
        Dialog.resize(533, 363)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(170, 210, 200, 41))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(30, 310, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(410, 310, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(120, 100, 269, 69))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.line_3 = QtWidgets.QFrame(self.widget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout.addWidget(self.line_3)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.line = QtWidgets.QFrame(self.widget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_2.addWidget(self.lineEdit)
        self.line_4 = QtWidgets.QFrame(self.widget)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout_2.addWidget(self.line_4)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_2.addWidget(self.lineEdit_2)
        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
        t2 = threading.Thread(target=self.socket_1, name='socket_thread', args=())
        t2.start()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "LocalInfo"))
        self.label_3.setText(_translate("Dialog", "计算机172-1530332103-王磊"))
        self.pushButton.setText(_translate("Dialog", "确定"))
        self.pushButton_2.setText(_translate("Dialog", "取消"))
        self.label.setText(_translate("Dialog", "计算机名："))
        self.label_2.setText(_translate("Dialog", "IP地址："))

        name = socket.gethostname()
        self.lineEdit.setText(name)
        # print(name)

        ip = socket.gethostbyname(name)
        self.lineEdit_2.setText(ip)
        # print(ip)

    def socket_1(self):
        m_strAuthor = '15 计算机172班 03号 王磊'
        sk = socket.socket()
        sk.settimeout(5.0)
        sk.bind(('127.0.0.1', 21567))
        sk.listen(5)
        while 1:
            print('waite connecting...')
            try:
                conn, addr = sk.accept()
            except socket.timeout:
                length = len(self.sub_threads)
                while length:
                    sub = self.sub_threads.pop(0)
                    sub_id = sub.ident
                    sub.join(0.5)
                    if sub.isAlive():
                        self.sub_threads.append(sub)
                    else:
                        print('killed sub thread ', sub_id)
                    length -= 1
            else:
                t = threading.Thread(target=self.handle, name='sub thread', args=(conn,))
                conn.setblocking(1)
                t.start()
                self.sub_threads.append(t)

    def handle(self,connected_sock):
        while 1:
            data = connected_sock.recv(1024).decode('GB2312')
            if len(data)>0:
                print('receive:', data)
                cur_thread = threading.current_thread()
                send_data = '{}:{}'.format(cur_thread.ident, data)
                connected_sock.sendall(send_data.encode('GB2312'))
                print('send:', send_data)
            else:
                print('closed')
                connected_sock.close()
                break

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_Dialog()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
