#---- Python VM startup for LISTENERLISTENER_1_from_3 ---
import SSL_listener

incomingIP="localhost"
incomingPort=10034
incomingPrivateKeyFile="server.key"
incomingPublicKeyFile="server.crt"
outgoingIP="localhost"
outgoingPort=00000
outgoingPublicKeyFile="server.crt"

def startLISTENER_1_from_3():
	incoming_ssl_EncryptionVNF= SSL_listener.SSL_listener(incomingIP, incomingPort, incomingPrivateKeyFile, incomingPublicKeyFile,"" )
#-------
