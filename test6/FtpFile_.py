# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FtpFile_.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import *
from ftplib import FTP
import logging
import threading


class Ui_FtpFile(object):
    def __init__(self):
        self.slm = QStringListModel()
        self.ftp = FTP()
        self.select_file = ""
        self.file_list = []


    def setupUi(self, FtpFile):
        FtpFile.setObjectName("FtpFile")
        FtpFile.resize(364, 402)
        self.layoutWidget = QtWidgets.QWidget(FtpFile)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 20, 341, 361))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout.addWidget(self.lineEdit_4)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_2.addWidget(self.lineEdit_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.listView = QtWidgets.QListView(self.layoutWidget)
        self.listView.setObjectName("listView")
        self.horizontalLayout_3.addWidget(self.listView)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_1 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_1.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton_1)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_3.setEnabled(False)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.retranslateUi(FtpFile)
        QtCore.QMetaObject.connectSlotsByName(FtpFile)

    def retranslateUi(self, FtpFile):
        _translate = QtCore.QCoreApplication.translate
        FtpFile.setWindowTitle(_translate("FtpFile", "FtpFile"))
        self.label.setText(_translate("FtpFile", "域名："))
        self.label_5.setText(_translate("FtpFile", "端口号："))
        self.label_2.setText(_translate("FtpFile", "登录名："))
        self.label_3.setText(_translate("FtpFile", "口令："))
        self.label_4.setText(_translate("FtpFile", "文件目录列表"))
        self.pushButton.setText(_translate("FtpFile", "查询"))
        self.pushButton_1.setText(_translate("FtpFile", "上一层"))
        self.pushButton_2.setText(_translate("FtpFile", "上传"))
        self.pushButton_3.setText(_translate("FtpFile", "下载"))
        self.pushButton_4.setText(_translate("FtpFile", "退出"))
        self.lineEdit.setText("127.0.0.1")
        self.lineEdit_4.setText("21")
        self.lineEdit_2.setText("mike")
        self.lineEdit_3.setText("123456")
        self.pushButton.clicked.connect(self.connect_button)
        self.pushButton_1.clicked.connect(self.back_button)
        self.pushButton_2.clicked.connect(self.upload_button)
        self.pushButton_3.clicked.connect(self.download_button)

        self.listView.setModel(self.slm)
        self.listView.clicked.connect(self.select_item)
        self.listView.doubleClicked.connect(self.cd_button)

    def connect_button(self):
        host = self.lineEdit.text()
        port = int(self.lineEdit_4.text())
        usr = self.lineEdit_2.text()
        pwd = self.lineEdit_3.text()
        try:
            self.ftp.connect(host,port,timeout=10)
        except:
            logging.warning('network connect time out')
            return 1001
        try:
            self.ftp.login(usr,pwd)
        except:
            logging.warning("username or password error")
            return 1002

        self.file_list = self.ftp.nlst() # 当前目录的所有文件列表
        self.slm.setStringList(self.file_list)
        # print(self.file_list)
        # file_list2 = self.ftp.sendcmd("pwd")    # 当前目录位置
        # print(file_list2)

        return 1000

    def select_item(self, qModelIndex):
        self.select_file = self.file_list[qModelIndex.row()]
        # print(self.select_file)
        if "." in self.select_file:     # 如果是文件，则可下载
            self.pushButton_3.setEnabled(True)
        else:                           # 否则是文件夹，不能下载
            self.pushButton_3.setEnabled(False)

    def cd_button(self):
        self.ftp.cwd(self.select_file)
        self.file_list = self.ftp.nlst()  # 刷新当前目录的所有文件列表
        self.slm.setStringList(self.file_list)

    def back_button(self):
        self.ftp.cwd("..")
        self.file_list = self.ftp.nlst()  # 刷新当前目录的所有文件列表
        self.slm.setStringList(self.file_list)

    def upload_button(self):
        t = threading.Thread(target=self.t,args=())
        t.start()

    def t(self):
        file_path, filer_ = QFileDialog.getOpenFileName()
        print(file_path)
        file_name = os.path.split(file_path)[1]
        print(file_name)
        self.ftp.storbinary('stor '+file_name, open(file_path, 'rb'))

    def download_button(self):
        self.ftp.retrbinary('retr '+self.select_file, open(self.select_file, 'wb').write)
        print("download succeed")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_FtpFile()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())