'''
Created on 15 avr. 2016

@author: phm
'''
class FederatedSecurityAgent:
    # initiate variables
    #name=""
    #securityVNF=[]
    #protocols=[]
     
    def __init__(self, name): 
        self.name=name
        self.VNF_manager=""
    
    def setVNFManager(self, VNF_manager):  
        self.VNF_manager= VNF_manager 
        
    def getVNFManager(self):  
        return self.VNF_manager     
           
    def getName(self):
        return self.name 
        
    def startVNF(self, securityVNF, configuration): 
        self.getVNFManager().startVNF(securityVNF, configuration)
        
    def setAuthorizedProtocols(self, protocols):
        self.getVNFManager().setAuthorizedProtocols(protocols)
       
        
    def getListOfSecurityVNF(self):
        return self.getVNFManager().getListOfSecurityVNF()
    
    
    def getListOfCommunicationProtocols(self):
        return self.getVNFManager().getListOfCommunicationProtocols()
    
    def setNetworkSegment(self, network_segment):
        self.network_segment=network_segment
        
    def getNetworkSegment(self):  
        return self.network_segment  
