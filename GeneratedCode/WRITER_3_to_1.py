#---- Python VNF startup for WRITER---
import SSL_writer
import time

outgoingIP="localhost"
outgoingPort=10032
outgoingPublicKeyFile="server.crt"

def startWRITER_3_to_1():
	ssl_writer=SSL_writer.SSL_writer(outgoingIP,outgoingPort, outgoingPublicKeyFile)
	while True:
		localtime=time.localtime(time.time())
		message= "message from WRITER_3_to_1 " +  time.asctime(localtime)
		ssl_writer.writeMessage(message)
		time.sleep(10)
