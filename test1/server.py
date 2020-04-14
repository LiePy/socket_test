from socket import *
from time import ctime

HOST = '127.0.0.1'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while 1:
    print('waiting for connection...')
    tcpCliSock, addr = tcpSerSock.accept()
    print('connecting from:',addr)

    # while 1:
    data = tcpCliSock.recv(BUFSIZ).decode('GB2312')
    print('收到消息：', data)
        # if not data:
        #     break  ('[%s]%s'%(ctime(),data)).encode()
    # tcpCliSock.send(b"HTTP/1.1 200 OK \r\n\r\n")
    # show_str = "<h1>这短短的一生，我们最终都会失去，你不妨大胆一些，爱一个人，" \
    #            "攀一座山，追一个梦！</h>"
    show_str = '消息已收到：{}'.format(data)
    tcpCliSock.send(show_str.encode('GB2312'))
    tcpCliSock.close()
# tcpSerSock.close()