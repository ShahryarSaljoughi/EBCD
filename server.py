__author__ = 'shahryar_slg'

import asyncore,socket,time
from socket import AF_INET,SOCK_STREAM
Clients=list()
class server(asyncore.dispatcher):
    def __init__(self,host,port):
        asyncore.dispatcher.__init__(self)
        self.create_socket(family=AF_INET,type=SOCK_STREAM)
        self.bind((host,port))
        self.listen(10)
    def handle_accept(self):
        print "Handle_accept is running! :))"
        pair=self.accept()
        if pair is not None:
            sock,addr=pair
            print type(sock)
            print type(addr)
            a=Client_Handler(sock)
            Clients.append(a)
            print "%s has been connected"%str(addr)



class Client_Handler(asyncore.dispatcher):
    def __init__(self,sock):
        print "Client handler's init is running !"
        asyncore.dispatcher.__init__(self,sock)
        print '1'
        self.create_socket(AF_INET,SOCK_STREAM)
        print '2'
        self.is_writable=False
    def readable(self):
        return True
    def writable(self):
        return True
    def handle_read(self):
        msg=self.recv(2048)
        print msg
    def handle_write(self):
        self.send("U are connected to the server ,at  %s !")%time.ctime()


server=server("",5002)
asyncore.loop()

