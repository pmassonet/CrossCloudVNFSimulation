#---- Python VNF startup for DECRYPT_2_from_1---
import SSL_listener
import SSL_writer

incomingIP="localhost"
incomingPort=10024
incomingPrivateKeyFile="server.key"
incomingPublicKeyFile="server.crt"
outgoingIP="localhost"
outgoingPort=10025
outgoingPublicKeyFile=""

def startDECRYPT_2_from_1():
	ssl_writer=SSL_writer.SSL_writer(outgoingIP,outgoingPort, outgoingPublicKeyFile)
	incoming_ssl_EncryptionVNF= SSL_listener.SSL_listener(incomingIP, incomingPort, incomingPrivateKeyFile, incomingPublicKeyFile,ssl_writer)
