# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'server_5.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


import sys
import time
import socket
import threading
from PyQt5 import QtCore, QtWidgets
from PyQt5.Qt import *



class BackendThread(QObject):   # 用来实时更新显示收到的消息
    # 通过类成员对象定义信号
    update_date = pyqtSignal(str)

    def run(self):
        while True:
            self.update_date.emit('')
            time.sleep(1)

class MyQMessageBox(QMessageBox):
    def __init__(self, parent=None):
        super(MyQMessageBox, self).__init__()
        self.title = 'tips'
        self.message = '连接成功'
        self.box = QMessageBox(QMessageBox.Critical, self.title, self.message,
                               QMessageBox.NoButton, parent)
        Ok = self.box.addButton('好的', QMessageBox.YesRole)

        Ok.clicked.connect(self.Ok)

        self.box.setIcon(3)
        self.box.setGeometry(200,200,0,0)
        self.box.show()

    def Ok(self):
        print('OK')
        self.box.exec_()



class Ui_Dialog(object):
    def __init__(self):
        self.t2 = []    # 用来存放线程的列表
        self.s = socket.socket()    # 服务器socket
        self.c = []     # 客户端socket列表
        self.msg = ''   # 需要显示的消息
        self.count = 0
        self.flag = False   # 服务器的开启状态

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(517, 388)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(30, 20, 441, 341))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.textBrowser = QtWidgets.QTextBrowser(self.widget)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "服务器端"))
        self.label.setText(_translate("Dialog", "监听端口号："))
        self.pushButton.setText(_translate("Dialog", "监听"))
        self.pushButton_2.setText(_translate("Dialog", "停止服务"))
        self.label_2.setText(_translate("Dialog", "在线人数："))
        self.lineEdit.setText('21567')
        self.pushButton.clicked.connect(self.listen_button)
        self.pushButton.clicked.connect(self.showdialog)
        self.pushButton_2.clicked.connect(self.break_button)
        self.pushButton_2.setEnabled(False)    # 初始化未监听时断开按钮不可点击

        # 调用刚才的自定义类
        self.backend = BackendThread()
        self.backend.update_date.connect(self.handleDisplay)  # 连接信号事件
        self.thread = QThread()  # 创建进程
        self.backend.moveToThread(self.thread)
        self.thread.started.connect(self.backend.run)
        self.thread.start()


    def listen_button(self):        # 监听按钮
        add1 = '127.0.0.1'
        add2 = self.lineEdit.text()
        self.s = socket.socket()
        self.s.bind((add1, int(add2)))
        self.s.listen()
        print('正在监听。。。')
        self.msg = '服务器开始运行~\n' + '*'*53 + '\n'
        self.textBrowser.setText(self.msg)
        t1 = threading.Thread(target=self.accept_socket)
        t1.start()
        self.pushButton.setEnabled(False)       # 点击监听按钮后该按钮将不可点击
        self.pushButton_2.setEnabled(True)
        self.flag = True        # 服务器开启

    def break_button(self):     # 断开按钮
        if self.count > 0:
            for cc in self.c:
                if cc != 0:     # 因为后面断开的客户端socket将它置为0了
                    cc.send('{}服务器已断开!\n'.format(time.ctime()).encode('GB2312'))
                    cc.close()
            self.c.clear()
        self.s.close()
        self.pushButton.setEnabled(True)        # 点击断开按钮后，监听按钮可用
        self.pushButton_2.setEnabled(False)
        self.flag = False

    def accept_socket(self):     # 接收socket连接
        try:
            while 1:
                print('等待连接中。。。')
                c_, addr = self.s.accept()
                self.c.append(c_)   # 将c_即客户端socket存入列表
                self.count += 1
                print(addr, '已连接')
                t2_ = threading.Thread(target=self.rec_msg, args=(len(self.c)-1,))
                self.t2.append(t2_)
                t2_.start()
        except:
            pass

    def handleDisplay(self):      # 显示收到的信息
        self.textBrowser.setText(self.msg)
        self.label_2.setText('在线人数：{}'.format(self.count))
        self.textBrowser.moveCursor(self.textBrowser.textCursor().End)  # 文本框显示到底部

    def rec_msg(self, i):      # 接受信息
        try:
            while 1:
                print('等待接受消息中。。。')
                msg = self.c[i].recv(1024).decode('GB2312')
                print('收到消息', msg)
                if '进入聊天室~' in msg:       # 服务器端不会显示客户聊天的内容，只显示进入的用户
                    self.msg += msg
                for step, x in enumerate(self.c):      # 当收到客户消息时，转发给其他所有在线客户
                    if step != i and x != 0:
                        x.send(msg.encode('GB2312'))
                if '退出聊天室' in msg:
                    self.msg += msg
                    self.count -= 1
                    self.c[i] = 0
                    print(len(self.c))
                    # self.t2[i]._stop()    # 线程不能强制退出，所以下面用break正常结束
                    print('结束', len(self.t2))
                    break
                if self.flag is False:
                    break       # 如果服务器停止，则退出循环
        except ConnectionAbortedError as e1:
            print(e1)

    def showdialog(self):       # 定义监听按钮弹出消息框
        dialog = QDialog()

        btn = QPushButton('OK',dialog)    # 增加一个Ok按钮
        btn.clicked.connect(dialog.exec_)
        btn.move(50, 50)

        tip = QLabel(dialog)
        tip.setText('开始监听...')
        tip.move(60,20)
        dialog.setWindowTitle("提示")

        dialog.show()
        dialog.setWindowModality(Qt.ApplicationModal)   # 设定只有关闭弹出对话窗口后才能操作其他窗口
        dialog.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QWidget()
    ui = Ui_Dialog()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
