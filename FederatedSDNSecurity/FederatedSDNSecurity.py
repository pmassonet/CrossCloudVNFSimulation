'''
Created on 12 janv. 2016

@author: phm
'''


# --------------------------------------

import yaml
import FederatedSDNAdapter
import random

class FederatedSDNSecurity:
    '''
    classdocs
    '''
       
    

    def __init__(self, name):
        '''
        Constructor
        '''
        self.name=name
        self.secAgents=[]
        self.sdnAdaptor=FederatedSDNAdapter.FederatedSDNAdapter("")
          
    def getName(self):
        return self.name
    
    def addSecurityAgent(self, secAgent):
        self.secAgents.append(secAgent)
        
    def getListOfSecurityVNF_all(self):   
        listOfVNF=[]
        secAg=""
        for secAg in self.secAgents:
            listOfVNF=listOfVNF+secAg.getListOfSecurityVNF()
        
        return listOfVNF
    
           
    def getListOfSecurityVNF_networkSegment(self, network_segment_id): 
        #print "network_segment_id is", network_segment_id 
        securityVNF=self.sdnAdaptor.getListOfSecurityVNF_networkSegment(network_segment_id)
        return securityVNF
        
        
    def getListOfSecurityVNF(self, fedAgent):
        return fedAgent.getListOfSecurityVNF()
    
    
    def getListOfCommunicationProtocols(self, fedAgent):
        return fedAgent.getListOfCommunicationProtocols()
        
    def getListOfCommunicationProtocolsAll(self):
        commProtocols=[]
        secAg=""
        for secAg in self.secAgents:
            commProtocols=commProtocols+secAg.getListOfCommunicationProtocols()
        return commProtocols
    
    def getListOfCommunicationProtocols_networkSegment(self, network_segment_id):
        secAg=""
        communicationProtocols=[]
        for secAg in self.secAgents:
            if (secAg.getNetworkSegment()==[network_segment_id]):
                communicationProtocols=communicationProtocols+secAg.getListOfCommunicationProtocols()
        return communicationProtocols
# --------------------------------------

    def startVNFOnNetworkSegment(self, network_segment_id, vnf, configuration):
        secAg=""
        for secAg in self.secAgents:
            #print "secAg.getNetworkSegment()", secAg.getNetworkSegment()
            if (secAg.getNetworkSegment()==[network_segment_id]):
                secAg.startVNF(vnf, configuration)


    def readYAMLfile(self, fileName):
        incomingIP=""
        incomingPort=""
        incomingPrivateKeyFile=""
        incomingPublicKeyFile=""
        outgoingIP=""
        outgoingPort=""
        outgoingPublicKeyFile=""
        identifier=""
        #outputFolder="C:\Users\phm\workspace\Federated SDN Security POC2\src\GeneratedCode"
        #outputFolder="/Users/phm/git/federated-sdn-security-poc/src/GeneratedCode"
        outputFolder="../GeneratedCode"
        #print "Begin readYAMLfile"
        with open(fileName, 'r') as stream:
            try:
                yamlObject=yaml.load(stream)
                #print yamlObject
            except yaml.YAMLError as exc:
                print(exc)



        for data in yamlObject.items():
            #print data
            key=""
            vnf_network_segment="none"
            vnf_type=""
            cloudManagerId=""
            for item in data:
                #print item
                if (key=="clouds"):
                    for cloudId in item.items():
                        for clouds in cloudId[1].items():
                            #print clouds
                            if (clouds[0]=="CloudManager"):
                                #print clouds[0], ":", clouds[1] 
                                cloudManagerId=clouds[1]
                            elif (clouds[0]=="Network_segment"):
                                #print clouds[0], ":", clouds[1] 
                                pass                                          
                            elif (clouds[0]=="VNF"):
                                for VNFS in clouds[1].items():
                                    #print VMs[0] 
                                    for VNF in VNFS[1].items():
                                        if (VNF[0]=="vnf_type"):
                                            vnf_type=VNF[1]
                                        elif (VNF[0]=="identifier"):
                                            identifier=VNF[1] 
                                        elif (VNF[0]=="network_segment"):
                                            vnf_network_segment=VNF[1]  
                                            self.startVNFOnNetworkSegment(vnf_network_segment, VNFS[0], vnf_type)                
                                            print VNFS[0], "started on", vnf_network_segment, "with type", vnf_type
                                        elif (VNF[0]=="incomingIP"):
                                            incomingIP=VNF[1]
                                            print "incomingIP : " + VNF[1]
                                        elif (VNF[0]=="incomingPort"):
                                            incomingPort=VNF[1]
                                            print "incomingPort : " + VNF[1] 
                                        elif (VNF[0]=="incomingPrivateKeyFile"):
                                            incomingPrivateKeyFile=VNF[1]
                                            print "incomingPrivateKeyFile : " + VNF[1] 
                                        elif (VNF[0]=="incomingPublicKeyFile"):
                                            incomingPublicKeyFile=VNF[1]
                                            print "incomingPublicKeyFile : " + VNF[1]
                                        elif (VNF[0]=="outgoingIP"):
                                            outgoingIP=VNF[1]
                                            print "outgoingIP : " + VNF[1]
                                        elif (VNF[0]=="outgoingPort"):
                                            outgoingPort=VNF[1]
                                            print "outgoingPort : " + VNF[1]
                                        elif (VNF[0]=="outgoingPublicKeyFile"):
                                            outgoingPublicKeyFile=VNF[1]
                                            print "outgoingPublicKeyFile : " + VNF[1]    
                                    # now generate the script
                                    if (vnf_type=="ENCRYPT"):
                                        f = open(outputFolder+"//"+ identifier+".py", 'w')
                                        f.write("#---- Python VNF startup for " + identifier + "---"+"\n")
                                        f.write("import SSL_listener"+"\n")
                                        f.write("import SSL_writer"+"\n")
                                        f.write("\n")
                                        f.write("incomingIP=" + "\"" + incomingIP + "\"" + "\n")
                                        f.write("incomingPort=" + incomingPort+"\n")
                                        f.write("incomingPrivateKeyFile="+"\"" +incomingPrivateKeyFile+"\"" +"\n")
                                        f.write("incomingPublicKeyFile="+"\"" + incomingPublicKeyFile+"\"" +"\n")
                                        f.write("outgoingIP="+"\"" +outgoingIP+"\"" +"\n")
                                        f.write("outgoingPort="+outgoingPort+"\n")
                                        f.write("outgoingPublicKeyFile="+"\"" +outgoingPublicKeyFile+"\"" +"\n")
                                        f.write("\n")
                                        f.write("def " +"start"+ identifier+"():"+"\n")
                                        f.write("\t"+"ssl_writer=SSL_writer.SSL_writer(outgoingIP,outgoingPort, outgoingPublicKeyFile)"+"\n")
                                        f.write("\t"+"incoming_ssl_EncryptionVNF= SSL_listener.SSL_listener(incomingIP, incomingPort, incomingPrivateKeyFile, incomingPublicKeyFile,ssl_writer)"+"\n")
                                        f.close()
                                    elif (vnf_type=="DECRYPT"):
                                        f = open(outputFolder+"//"+ identifier+".py", 'w')
                                        f.write("#---- Python VNF startup for " + identifier + "---"+"\n")
                                        f.write("import SSL_listener"+"\n")
                                        f.write("import SSL_writer"+"\n")
                                        f.write("\n")
                                        f.write("incomingIP=" + "\"" + incomingIP + "\"" + "\n")
                                        f.write("incomingPort=" + incomingPort+"\n")
                                        f.write("incomingPrivateKeyFile="+"\"" +incomingPrivateKeyFile+"\"" +"\n")
                                        f.write("incomingPublicKeyFile="+"\"" + incomingPublicKeyFile+"\"" +"\n")
                                        f.write("outgoingIP="+"\"" +outgoingIP+"\"" +"\n")
                                        f.write("outgoingPort="+outgoingPort+"\n")
                                        f.write("outgoingPublicKeyFile="+"\"" +outgoingPublicKeyFile+"\"" +"\n")
                                        f.write("\n")
                                        f.write("def "+"start"+ identifier+"():"+"\n")
                                        f.write("\t"+"ssl_writer=SSL_writer.SSL_writer(outgoingIP,outgoingPort, outgoingPublicKeyFile)"+"\n")
                                        f.write("\t"+"incoming_ssl_EncryptionVNF= SSL_listener.SSL_listener(incomingIP, incomingPort, incomingPrivateKeyFile, incomingPublicKeyFile,ssl_writer)"+"\n")
                                        f.close()
                            elif (clouds[0]=="VMS"):
                                for VMs in clouds[1].items():
                                    #print VMs[0] 
                                    for VNF in VMs[1].items():
                                        if (VNF[0]=="vnf_type"):
                                            vnf_type=VNF[1]
                                        elif (VNF[0]=="identifier"):
                                            identifier=VNF[1]    
                                        elif (VNF[0]=="network_segment"):
                                            vnf_network_segment=VNF[1]  
                                            self.startVNFOnNetworkSegment(vnf_network_segment, VMs[0], vnf_type)                
                                            print VMs[0], "started on", vnf_network_segment, "with type", vnf_type
                                        elif (VNF[0]=="incomingIP"):
                                            incomingIP=VNF[1]
                                            print "incomingIP : " + VNF[1]
                                        elif (VNF[0]=="incomingPort"):
                                            incomingPort=VNF[1]
                                            print "incomingPort : " + VNF[1] 
                                        elif (VNF[0]=="incomingPrivateKeyFile"):
                                            incomingPrivateKeyFile=VNF[1]
                                            print "incomingPrivateKeyFile : " + VNF[1] 
                                        elif (VNF[0]=="incomingPublicKeyFile"):
                                            incomingPublicKeyFile=VNF[1]
                                            print "incomingPublicKeyFile : " + VNF[1]
                                        elif (VNF[0]=="outgoingIP"):
                                            outgoingIP=VNF[1]
                                            print "outgoingIP : " + VNF[1]
                                        elif (VNF[0]=="outgoingPort"):
                                            outgoingPort=VNF[1]
                                            print "outgoingPort : " + VNF[1]
                                        elif (VNF[0]=="outgoingPublicKeyFile"):
                                            outgoingPublicKeyFile=VNF[1]
                                            print "outgoingPublicKeyFile : " + VNF[1]    
                                    # now generate the script
                                    if (vnf_type=="LISTENER"):
                                        f = open(outputFolder+"//"+ identifier+".py", 'w')
                                        f.write("#---- Python VM startup for " + vnf_type + identifier + " ---" +"\n")
                                        f.write("import SSL_listener"+"\n")
                                        f.write("\n")
                                        f.write("incomingIP=" + "\"" + incomingIP + "\"" + "\n")
                                        f.write("incomingPort=" + incomingPort+"\n")
                                        f.write("incomingPrivateKeyFile="+"\"" +incomingPrivateKeyFile+"\"" +"\n")
                                        f.write("incomingPublicKeyFile="+"\"" + incomingPublicKeyFile+"\"" +"\n")
                                        f.write("outgoingIP="+"\"" +outgoingIP+"\"" +"\n")
                                        f.write("outgoingPort="+outgoingPort+"\n")
                                        f.write("outgoingPublicKeyFile="+"\"" +outgoingPublicKeyFile+"\"" +"\n")
                                        f.write("\n")
                                        f.write("def "+"start"+ identifier+"():"+"\n")
                                        f.write("\t"+"incoming_ssl_EncryptionVNF= SSL_listener.SSL_listener(incomingIP, incomingPort, incomingPrivateKeyFile, incomingPublicKeyFile,"+ "\""+"\" )"+"\n")
                                        f.write("#-------"+"\n")
                                        f.close()
                                    elif (vnf_type=="WRITER"):
                                        f = open(outputFolder+"//"+ identifier+".py", 'w')
                                        f.write("#---- Python VNF startup for " + vnf_type + "---" +"\n")
                                        f.write("import SSL_writer"+"\n")
                                        f.write("import time"+"\n")
                                        f.write("\n")
                                        f.write("outgoingIP="+"\"" +outgoingIP+"\"" +"\n")
                                        f.write("outgoingPort="+outgoingPort+"\n")
                                        f.write("outgoingPublicKeyFile="+"\"" +outgoingPublicKeyFile+"\"" +"\n")
                                        f.write("\n")
                                        f.write("def "+"start"+ identifier+"():"+"\n")
                                        f.write("\t"+"ssl_writer=SSL_writer.SSL_writer(outgoingIP,outgoingPort, outgoingPublicKeyFile)"+"\n")
                                        f.write("\t"+"while True:"+"\n")
                                        f.write("\t"+"\t"+"localtime=time.localtime(time.time())"+"\n")
                                        f.write("\t"+"\t"+"message= \"message from " + identifier + " \"" + " + " + " time.asctime(localtime)"+"\n")
                                        f.write("\t"+"\t"+"ssl_writer.writeMessage(message)"+"\n")
                                        f.write("\t"+"\t"+"time.sleep(10)"+"\n")
                                        f.close()
                            elif (clouds[0]=="OutgoingChaining"): 
                                chainingstr=""
                                for chaining in clouds[1].items():
                                    for chainedVNF in chaining[1]:
                                        if (chainingstr==""):
                                            chainingstr=chainedVNF  
                                        else:
                                            chainingstr=chainingstr+" seq "+ chainedVNF 
                                    print chaining[0], ":", chainingstr 
                                # get the cloud manager and VNF manager
                                
                            elif (clouds[0]=="IncomingChaining"): 
                                chainingstr=""
                                for chaining in clouds[1].items():
                                    if (chaining[0]=="in_chaining"):
                                        for chainedVNF in chaining[1]:
                                            if (chainingstr==""):
                                                chainingstr=chainedVNF  
                                            else:
                                                chainingstr=chainingstr+" seq "+ chainedVNF   
                                            print chaining[0], ":", chainingstr  
                                    elif (chaining[0]=="startup-order"):
                                        print "parsing startup-order"
                                        #f = open(outputFolder+"\\"+ self.cloudId + "VNF-startup"+".py", 'w')
                                        #f.write("#---- Python VM startup for " + self.cloudId + " ---" +"\n")
                                        f = open(outputFolder+"//"+ "start-VNF-"+chaining[1][0] +".py", 'w')
                                        f.write("#---- Python VM startup for " + chaining[1][0] + " ---" +"\n")
                                        f.write("import multiprocessing"+"\n")
                                        f.write("import time"+"\n")
                                        for chainedVNF in chaining[1]:
                                            f.write("import " + chainedVNF + "\n")
                                        f.write("\n")
                                        f.write("processes = []"+"\n")
                                        f.write("\n")
                                        f.write("if __name__ == '__main__':"+"\n")
                                        for chainedVNF in chaining[1]:
                                            f.write("\t"+"p = multiprocessing.Process(target="+chainedVNF+"."+"start"+chainedVNF+")"+"\n")
                                            f.write("\t"+"processes.append(p)"+"\n")
                                            f.write("\t"+"p.start()"+"\n")
                                            f.write("\t"+"print \"started "+ chainedVNF+ "\""+"\n")
                                            f.write("\t"+"time.sleep(5)"+"\n")
                                        f.write("\n")
                                        f.write("\t"+"for p in processes:"+"\n")
                                        f.write("\t"+"\t"+"p.join()"+"\n")                                       
                                        f.close()       
                            elif (clouds[0]=="SecurityGroup"):   
                                secItem=""
                                for secItem in clouds[1].items():
                                    #print secItem
                                    #for secItem in  secGroupStr.items():
                                    if (secItem[0]=="id"):
                                        secGroupId= secItem[1]
                                    elif (secItem[0]=="members"):
                                        secGroupMembers= secItem[1]
                                print "security group:", secGroupId, "members:", secGroupMembers   
                            elif (clouds[0]=="AuthorizedProtocols"):
                                chainingstr=""
                                for chaining in clouds[1].items():
                                    for chainedVNF in chaining[1]:
                                        if (chainingstr==""):
                                            chainingstr=chainedVNF  
                                        else:
                                            chainingstr=chainingstr+" , "+ chainedVNF   
                                    print "Authorized protocols", ":", chainingstr                                      
                elif (key=="configuration"):
                    print key, ":", item
                key=item
            


    def readYAMLfileV2(self, fileName):
        with open(fileName, 'r') as stream:
            try:
                yamlObject=yaml.load(stream)
                #print yamlObject
                print "load:" 
                print yamlObject.items()
                print "parse:" 
                #for event in yaml.parse(stream):
                #    print event
                #yaml.compose(stream)
            except yaml.YAMLError as exc:
                print(exc)
               
            
            
            

    def verifySecurityPolicy(self, fedSDN):
        print "network segments for", "FedCloudNetwork_1", "are", fedSDN.getNetworkFederationSegments("FedCloudNetwork_1")
        network_segments=fedSDN.getNetworkFederationSegments("FedCloudNetwork_1")
        network_segment=""
        for network_segment in network_segments:          
            print "VNF for ", network_segment, "are", self.getListOfSecurityVNF_networkSegment(network_segment)
            print "IncomingChaining for", network_segment, "is", "" 
            print "OutgoingChaining for", network_segment, "is", ""   
    