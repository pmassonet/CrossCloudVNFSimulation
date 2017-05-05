'''
Created on 10 mai 2016

@author: phm
'''

class CloudManager(object):
    '''
    classdocs
    '''


    def __init__(self, name):
        '''
        Constructor
        '''
        self.name=name
        self.network_segments=[]
        self.VNFmanager=""
    
    def getName(self): 
        return self.name
    
    def setNetworkSegments(self, network_segments):   
        self.network_segments.append(network_segments) 
        
    def getNetworkSegments(self):   
        return self.network_segments
        
    def setVNFManager(self, vnfManager):
        self.VNFmanager=vnfManager    
        
    def getVNFManager(self):
        return self.VNFmanager 
    
    