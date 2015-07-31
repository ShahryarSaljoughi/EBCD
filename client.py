__author__ = 'shahryar_slg'

import asyncore,socket
from socket import AF_INET,SOCK_STREAM
class client(asyncore.dispatcher):
    def __init__(self,host,port):
        asyncore.dispatcher.__init__(self)
        self.create_socket(AF_INET,SOCK_STREAM)
        self.connect((host,port))
    def handle_connect(self):
        pass
    def readable(self):
        return True
    def handle_read(self):
        msg=self.recv(2048)
        print msg

Cli=client('127.0.0.1',5002)
asyncore.loop()