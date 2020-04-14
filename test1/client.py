from socket import *


HOST = '127.0.0.1'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

       # AF_INET->IPv4；AF_INET6->IPv6;SOCK_STREAM->TCP；SOCK_DGRAM->UDP


while 1:
    tcpCliSock = socket(AF_INET, SOCK_STREAM)
    tcpCliSock.connect(ADDR)
    data1 = input('>')
    # if not data1:
    #     break
    tcpCliSock.send(data1.encode('GB2312'))
    data2 = tcpCliSock.recv(BUFSIZ)
    data3 = tcpCliSock.recv(BUFSIZ)
    # if not data1:
    #     break
    print('接受消息：',data2.decode('GB2312'),data3.decode('GB2312'))
    tcpCliSock.close()
