'''
Created on 4 mai 2016

@author: phm
'''

class VNFManager(object):
    '''
    classdocs
    '''


    def __init__(self, name):
        '''
        Constructor
        '''
        self.name=name
        self.securityVNF=[]
        self.protocols=[]
        self.configurations=[]
        self.incomingChaining=[]
        self.outgoingChaining=[]
 
        
    def startVNF(self, securityVNF, configuration): 
        self.securityVNF.append(securityVNF)
        self.configurations.append(configuration)
        #print self.securityVNF, "started"
        
        
    def setAuthorizedProtocols(self, protocols):
        self.protocols=self.protocols+protocols
        
    def getListOfSecurityVNF(self):
        return self.securityVNF
    
    
    def getListOfCommunicationProtocols(self):
        return self.protocols    
    
    def setIncomingChaining(self, network_segment, chain):
        pass
        self.incomingChaining.append([network_segment, chain])
    
    def getIncomingChaining(self, network_segment):
        pass
        for chain in self.incomingChaining:
            if (chain[0]==network_segment):
                result = chain[1]
        return result
    
    def setOutgoingChaining(self, network_segment, chain):
        pass
        self.outgoingChaining.append([network_segment, chain])
    
    def getOutgoingChaining(self, network_segment, chain):
        pass
        for chain in self.outgoingChaining:
            if (chain[0]==network_segment):
                result = chain[1]
        return result