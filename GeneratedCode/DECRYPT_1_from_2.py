#---- Python VNF startup for DECRYPT_1_from_2---
import SSL_listener
import SSL_writer

incomingIP="localhost"
incomingPort=10027
incomingPrivateKeyFile="server.key"
incomingPublicKeyFile="server.crt"
outgoingIP="localhost"
outgoingPort=10028
outgoingPublicKeyFile="server.crt"

def startDECRYPT_1_from_2():
	ssl_writer=SSL_writer.SSL_writer(outgoingIP,outgoingPort, outgoingPublicKeyFile)
	incoming_ssl_EncryptionVNF= SSL_listener.SSL_listener(incomingIP, incomingPort, incomingPrivateKeyFile, incomingPublicKeyFile,ssl_writer)
