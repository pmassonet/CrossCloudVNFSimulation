'''
Created on 6 mai 2016

@author: phm
'''

class FederatedSDN(object):
    '''
    classdocs
    '''


    def __init__(self, fedSDN_id):
        '''
        Constructor
        '''
        self.fedSDN_id=fedSDN_id
        self.network_segments=[]
        self.fedNetwork_id=""
        
    def createNetworkFederation(self, fedNetwork_id, network_segments):
        self.fedNetwork_id=fedNetwork_id
        self.item=""
        for self.item in network_segments:
        #for item in network_segments
            self.network_segments.append(self.item)
        
    def addNetworkSegment(self, network_segment):  
        self.network_segments.append(network_segment)       
             
    def getNetworkFederationSegments(self, FedCloudNetwork):      
        return self.network_segments  
    
    def getIdentifier(self):
        return self.fedSDN_id  