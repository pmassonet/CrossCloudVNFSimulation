#---- Python VNF startup for ENCRYPT_1_to_3---
import SSL_listener
import SSL_writer

incomingIP="localhost"
incomingPort=10029
incomingPrivateKeyFile="server.key"
incomingPublicKeyFile="server.crt"
outgoingIP="localhost"
outgoingPort=10030
outgoingPublicKeyFile="server.crt"

def startENCRYPT_1_to_3():
	ssl_writer=SSL_writer.SSL_writer(outgoingIP,outgoingPort, outgoingPublicKeyFile)
	incoming_ssl_EncryptionVNF= SSL_listener.SSL_listener(incomingIP, incomingPort, incomingPrivateKeyFile, incomingPublicKeyFile,ssl_writer)
