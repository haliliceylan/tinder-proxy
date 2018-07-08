import thread
import socket
import ssl
import StringIO


def handler(clientsock, addr):
    data = StringIO.StringIO()
    while 1:
        new = clientsock.recv(BUFF)
        data.write(new)
        if not new: break
    send = connect_to_ssl()
    print 'sent:' + send
    clientsock.sendall(send)
    clientsock.close()

def connect_to_ssl():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('github.com', 443))
    s = ssl.wrap_socket(s, keyfile=None, certfile=None, server_side=False, cert_reqs=ssl.CERT_NONE,
                        ssl_version=ssl.PROTOCOL_SSLv23)
    s.sendall("GET / HTTP/1.1\r\nHost: github.com\r\nConnection: close\r\n\r\n")
    data = StringIO.StringIO()
    while True:
        new = s.recv(1024)
        if not new:
            s.close()
            break
        data.write(new)
    return data.getvalue()

BUFF = 1024
HOST = '127.0.0.1'  # must be input parameter @TODO
PORT = 9999  # must be input parameter @TODO

print connect_to_ssl()
ADDR = (HOST, PORT)
serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serversock.bind(ADDR)
#serversock = ssl.wrap_socket (serversock, certfile='./server.pem', server_side=True)
serversock.listen(5)

while 1:
    print 'waiting for connection...'
    clientsock, addr = serversock.accept()
    print '...connected from:', addr
    thread.start_new_thread(handler, (clientsock, addr))