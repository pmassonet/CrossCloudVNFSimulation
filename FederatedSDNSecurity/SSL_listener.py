'''
Created on 1 juil. 2016

@author: phm
'''

import socket, ssl, pprint
import SSL_writer

class SSL_listener:
    '''
    classdocs
    ''' 
    #certfile=""
    #keyfile=""
    ssl_writer=""
    
    def __init__(self, incomingIP, incomingPort, incomingPrivateKeyFile, incomingPublicKeyFile, ssl_writer):
        '''
        Constructor
        '''
        
        self.incomingPrivateKeyFile=incomingPrivateKeyFile
        self.incomingPublicKeyFile=incomingPublicKeyFile
        self.ssl_writer=ssl_writer
        
        self.bindsocket = socket.socket()
        try:
            self.bindsocket.bind((incomingIP, incomingPort))
            self.bindsocket.listen(10)
            print "socket bind done for " + str(incomingIP) + " " + str(incomingPort)
        except Exception as e:
            print("something's wrong. Exception is %s" % (e))
        if (incomingPrivateKeyFile!=""):
            self.start_listening_encrypted()
        elif (incomingPrivateKeyFile==""):
            self.start_listening_unencrypted()
            

    def start_listening_encrypted(self):
        while True:
            self.newsocket, fromaddr = self.bindsocket.accept()
            self.connstream = ssl.wrap_socket(self.newsocket,
                                 server_side=True,
                                 certfile=self.incomingPublicKeyFile,
                                 keyfile=self.incomingPrivateKeyFile)
            try:
                #print "start listening encrypted"
                self.deal_with_client_encrypted(self.connstream)
            finally:
                self.connstream.shutdown(socket.SHUT_RDWR)
                self.connstream.close()
                print "connection closed"
     
    def start_listening_unencrypted(self): 
        while True:
            self.newsocket, fromaddr = self.bindsocket.accept()  
            try:
                #print "start listening unencrypted"
                self.deal_with_client_unencrypted(self.newsocket)
            finally:
                self.newsocket.shutdown(socket.SHUT_RDWR)
                self.newsocket.close()
                print "connection closed"
     
        
    def do_something_encrypted(self, connstream, data):
        if self.ssl_writer=="":
            print "message received: ", data
        else:
            self.ssl_writer.writeMessage(data)
            
        return True

    def deal_with_client_encrypted(self, connstream):
        data = self.connstream.read()
        while data:
            #print "waiting for data"
            if not self.do_something_encrypted(connstream, data):
                break
            data = connstream.read()
            
    def deal_with_client_unencrypted(self, newsocket):
        data = self.newsocket.recv(50000)
        while data:
            #print "waiting for data"
            if not self.do_something_unencrypted(newsocket, data):
                break
            data = newsocket.recv(50000)  
    
    def do_something_unencrypted(self, newsocket, data):
        if self.ssl_writer=="":
            print "message received: ", data
        else:
            self.ssl_writer.writeMessage(data)
            
        return True  