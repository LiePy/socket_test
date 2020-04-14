from socket import *


HOST = '127.0.0.1'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

# AF_INET->IPv4；AF_INET6->IPv6;SOCK_STREAM->TCP；SOCK_DGRAM->UDP

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

while 1:
    data1 = input('>')
    if len(data1)>0:
        tcpCliSock.sendall(data1.encode('GB2312'))
        data2 = tcpCliSock.recv(BUFSIZ)
        print('receive:', data2.decode('GB2312'))
    else:
        tcpCliSock.close()
        break
