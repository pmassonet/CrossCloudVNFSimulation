#---- Python VNF startup for DECRYPT_1_from_3---
import SSL_listener
import SSL_writer

incomingIP="localhost"
incomingPort=10033
incomingPrivateKeyFile="server.key"
incomingPublicKeyFile="server.crt"
outgoingIP="localhost"
outgoingPort=10034
outgoingPublicKeyFile="server.crt"

def startDECRYPT_1_from_3():
	ssl_writer=SSL_writer.SSL_writer(outgoingIP,outgoingPort, outgoingPublicKeyFile)
	incoming_ssl_EncryptionVNF= SSL_listener.SSL_listener(incomingIP, incomingPort, incomingPrivateKeyFile, incomingPublicKeyFile,ssl_writer)
