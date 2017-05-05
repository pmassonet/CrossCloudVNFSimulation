#---- Python VNF startup for DECRYPT_3_from_1---
import SSL_listener
import SSL_writer

incomingIP="localhost"
incomingPort=10030
incomingPrivateKeyFile="server.key"
incomingPublicKeyFile="server.crt"
outgoingIP="localhost"
outgoingPort=10031
outgoingPublicKeyFile="server.crt"

def startDECRYPT_3_from_1():
	ssl_writer=SSL_writer.SSL_writer(outgoingIP,outgoingPort, outgoingPublicKeyFile)
	incoming_ssl_EncryptionVNF= SSL_listener.SSL_listener(incomingIP, incomingPort, incomingPrivateKeyFile, incomingPublicKeyFile,ssl_writer)
