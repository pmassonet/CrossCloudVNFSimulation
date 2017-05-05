#---- Python VM startup for LISTENERLISTENER_3_from_1 ---
import SSL_listener

incomingIP="localhost"
incomingPort=10031
incomingPrivateKeyFile="server.key"
incomingPublicKeyFile="server.crt"
outgoingIP="localhost"
outgoingPort=00000
outgoingPublicKeyFile="server.crt"

def startLISTENER_3_from_1():
	incoming_ssl_EncryptionVNF= SSL_listener.SSL_listener(incomingIP, incomingPort, incomingPrivateKeyFile, incomingPublicKeyFile,"" )
#-------
