#---- Python VM startup for LISTENERLISTENER_1_from_2 ---
import SSL_listener

incomingIP="localhost"
incomingPort=10028
incomingPrivateKeyFile="server.key"
incomingPublicKeyFile="server.crt"
outgoingIP="localhost"
outgoingPort=10023
outgoingPublicKeyFile="server.crt"

def startLISTENER_1_from_2():
	incoming_ssl_EncryptionVNF= SSL_listener.SSL_listener(incomingIP, incomingPort, incomingPrivateKeyFile, incomingPublicKeyFile,"" )
#-------
