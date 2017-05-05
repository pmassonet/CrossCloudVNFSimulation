'''
Created on 13 juin 2016

@author: phm
'''

class FederatedSDNAdapter(object):
    '''
    classdocs
    '''



    def __init__(self, params):
        '''
        Constructor
        '''
        self.test=""
        self.secAgents=[]
      
    def getListOfSecurityVNF_networkSegment(self, network_segment_id): 
        #print "network_segment_id is", network_segment_id 
        securityVNF=[]
        secAg=""
        for secAg in self.secAgents:
            #print "secAg.getNetworkSegment()", secAg.getNetworkSegment()
            if (secAg.getNetworkSegment()==[network_segment_id]):
                vnf=secAg.getListOfSecurityVNF()
                #print "vnf are", vnf
                securityVNF=securityVNF+vnf
        return securityVNF