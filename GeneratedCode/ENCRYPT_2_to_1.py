#---- Python VNF startup for ENCRYPT_2_to_1---
import SSL_listener
import SSL_writer

incomingIP="localhost"
incomingPort=10026
incomingPrivateKeyFile="server.key"
incomingPublicKeyFile="server.crt"
outgoingIP="localhost"
outgoingPort=10027
outgoingPublicKeyFile="server.crt"

def startENCRYPT_2_to_1():
	ssl_writer=SSL_writer.SSL_writer(outgoingIP,outgoingPort, outgoingPublicKeyFile)
	incoming_ssl_EncryptionVNF= SSL_listener.SSL_listener(incomingIP, incomingPort, incomingPrivateKeyFile, incomingPublicKeyFile,ssl_writer)
