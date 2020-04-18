import sys

from PyQt5.Qt import *

class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.resize(300, 500)
        layout = QVBoxLayout(self)
        self.infoButton = QPushButton()
        self.infoButton.setText('点击弹出消息对话框')
        self.infoButton.clicked.connect(self.info)
        layout.addWidget(self.infoButton)
        
    def info(self):
        reply = QMessageBox.information(self, '提示', '服务器开始监听！',
                                        QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        print(reply)
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myShow = MyWindow()
    myShow.show()
    sys.exit(app.exec_())