import socket
from threading import Thread
import ssl
import Modifier

class ProxyServer(Thread):

    def __init__(self,host,port):
        Thread.__init__(self)
        ADDR = (host,port)
        serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serversock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        serversock.bind(ADDR)
        # serversock = ssl.wrap_socket (serversock, certfile='./server.pem', server_side=True)
        serversock.listen(5)
        self.serversock = serversock

    def run(self):
        super(ProxyServer, self).run()
        while 1:
            clientsock, addr = self.serversock.accept()
            reload(Modifier)
            #SC = ClientThread.SSLSocketFactory("api.gotinder.com",443)
            #St = ClientThread(SC,Modifier.respond)
            Ct = ClientThread(clientsock,Modifier.request)
            #St.target = clientsock
            #Ct.target = SC
            Ct.start()
            #St.start()


class ClientThread(Thread):

    def __init__(self,clientsock,observe_function):
        Thread.__init__(self)
        self.clientsock = clientsock
        self.observe_function = observe_function
        self.target = None

    def run(self):
        super(ClientThread, self).run()
        while True:
            new = self.clientsock.recv(1024)
            new = self.observe_function(new)
            if not new:
                self.clientsock.close()
                break
            if(self.target is None):
                try:
                    SC = ServerThread.SSLSocketFactory(new.split("Host: ")[1].split("\n")[0], 443)
                    St = ServerThread(SC, self.clientsock ,Modifier.respond)
                    self.target = SC
                    St.start()
                except Exception as e:
                    print "Error:" + str(e)
                    self.clientsock.close()
                    return
            self.target.send(new)

class ServerThread(Thread):
    def __init__(self, clientsock, target, observe_function):
        Thread.__init__(self)
        self.clientsock = clientsock
        self.observe_function = observe_function
        self.target = target

    def run(self):
        super(ServerThread, self).run()
        while True:
            new = self.clientsock.recv(1024)
            if not new:
                self.clientsock.close()
                break
            new = self.observe_function(new)
            self.target.send(new)

    @staticmethod
    def SSLSocketFactory(host,port):
        host = "54.172.35.83"
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        s = ssl.wrap_socket(s, keyfile=None, certfile=None, server_side=False, cert_reqs=ssl.CERT_NONE,ssl_version=ssl.PROTOCOL_SSLv23)
        return s