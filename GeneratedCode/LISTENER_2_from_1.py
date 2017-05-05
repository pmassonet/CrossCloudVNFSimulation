#---- Python VM startup for LISTENERLISTENER_2_from_1 ---
import SSL_listener

incomingIP="localhost"
incomingPort=10025
incomingPrivateKeyFile=""
incomingPublicKeyFile=""
outgoingIP="localhost"
outgoingPort=00000
outgoingPublicKeyFile=""

def startLISTENER_2_from_1():
	incoming_ssl_EncryptionVNF= SSL_listener.SSL_listener(incomingIP, incomingPort, incomingPrivateKeyFile, incomingPublicKeyFile,"" )
#-------
