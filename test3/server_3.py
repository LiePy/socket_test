import time
import socket

s = socket.socket()  # 创建套接字
s.bind(('127.0.0.1', 21567))    # 绑定套接字
s.listen(5)     # 监听套接字

while 1:
    print('waiting for connecting')     # 未连接时打印等待连接
    c_socket, addr = s.accept()     # 接受连接
    print('connect from: {}'.format(addr))      # 打印出连接的ip地址
    rcv_MSG = c_socket.recv(1024).decode('GB2312')      # 接收信息
    send_MSG = "[{}]已收到消息：{}".format(time.ctime(), rcv_MSG)     # 准备发送的信息
    print(rcv_MSG)      # 打印收到的信息
    c_socket.send(send_MSG.encode('GB2312'))        # 发送信息
    c_socket.close()        # 关闭套接字
s.close()