'''
Created on 28 juil. 2016

@author: phm
'''
import ssl, socket, pprint

class SSL_writer:
    '''
    classdocs
    '''

    #def __init__(self):
    def __init__(self, outgoingIP, outgoingPort, outgoingPublicKeyFile):
        '''
        Constructor
        '''
        
        self.outgoingPublicKeyFile=outgoingPublicKeyFile
        self.sock=""
        self.ssl_sock=""
        
        #print "start SSL test"
        
        #
        ########################## open output socket ###########################
        #
        
        if (outgoingPublicKeyFile!=""):
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            # Require a certificate from the IncomingDecryptionVNF. We used a self-signed certificate
            # so here ca_certs must be the IncomingDecryptionVNF certificate itself.

            self.ssl_sock = ssl.wrap_socket(self.s,
            ca_certs=outgoingPublicKeyFile,
            cert_reqs=ssl.CERT_REQUIRED)

            try:
                #self.ssl_sock.connect(('localhost', 10024))
                self.ssl_sock.connect((outgoingIP, outgoingPort))
                print "crypted socket connect done for " + str(outgoingIP) + " " + str(outgoingPort)
                #ssl_sock.connect(('www.verisign.com', 4430))
            except:
                print "cannot connect"

            print repr(self.ssl_sock.getpeername())
            print self.ssl_sock.cipher()
            print pprint.pformat(self.ssl_sock.getpeercert())

            #self.ssl_sock.write("VNF is up")
            self.writeMessageEncrypted("test message via socket to " + str(outgoingIP) + " " + str(outgoingPort))
        elif(outgoingPublicKeyFile==""):
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            try:
                self.sock.connect((outgoingIP, outgoingPort))
                #print "unencrypted socket connect done for " + str(outgoingIP) + " " + str(outgoingPort)
            except:
                print "cannot connect"
            self.sock.send("test")    
            self.writeMessageUnencrypted("test message via socket to" + str(outgoingIP) + " " + str(outgoingPort))
    
    
    def writeMessage(self, message):
        if (self.ssl_sock!=""):
            self.writeMessageEncrypted(message)
        elif (self.sock!=""):
            self.writeMessageUnencrypted(message)
              
    def writeMessageEncrypted(self, message):
        print "message sent: ", message
        self.ssl_sock.write(message)
        
    def writeMessageUnencrypted(self, message):
        print "message sent: ", message
        try:
            self.sock.send(message)
        except:
                print "cannot send"   