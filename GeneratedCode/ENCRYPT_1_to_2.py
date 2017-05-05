#---- Python VNF startup for ENCRYPT_1_to_2---
import SSL_listener
import SSL_writer

incomingIP="localhost"
incomingPort=10023
incomingPrivateKeyFile="server.key"
incomingPublicKeyFile="server.crt"
outgoingIP="localhost"
outgoingPort=10024
outgoingPublicKeyFile="server.crt"

def startENCRYPT_1_to_2():
	ssl_writer=SSL_writer.SSL_writer(outgoingIP,outgoingPort, outgoingPublicKeyFile)
	incoming_ssl_EncryptionVNF= SSL_listener.SSL_listener(incomingIP, incomingPort, incomingPrivateKeyFile, incomingPublicKeyFile,ssl_writer)
