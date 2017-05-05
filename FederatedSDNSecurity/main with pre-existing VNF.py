

'''
Created on 12 janv. 2016

@author: phm
'''
import FederatedSDN
import FederatedSDNSecurity
import FederatedSecurityAgent
import VNFManager
import CloudManager
import yaml







federationCloudManagers=[]


cloudFederationMembers=[
    ["cloudMan_1","vnf_manager_1", "network_segment_1", [["ndpi_1", "ndpi_1_config" ]],["http"]],  
    ["cloudMan_2","vnf_manager_2", "network_segment_2", [["fw_2", "fw_2_config"]],["https"]]
]


print "-----------Initial setup of Cloud_1, cloud_2 and cloud_3 -----------"

cloudMember=""
for cloudMember in cloudFederationMembers:
    # create a cloud manager
    cloud_manager=CloudManager.CloudManager(cloudMember[0])
    print "Cloud manager", cloud_manager.getName(), "created"
    federationCloudManagers.append(cloud_manager)
    # set the network segments
    cloud_manager.setNetworkSegments(cloudMember[2])
    # create a VNF manager
    vnfManager=VNFManager.VNFManager(cloudMember[1])
    cloud_manager.setVNFManager(vnfManager)
    # start VNF
    vnf=""
    for vnf in cloudMember[3]:
        vnfManager.startVNF(vnf[0], vnf[1])
    vnfManager.setAuthorizedProtocols(cloudMember[4])
    



print "------------ start Federated SDN ---------------"

# create a federated SDN
fedSDN=FederatedSDN.FederatedSDN("fedSDN_1")
print "FederatedSDN", fedSDN.getIdentifier(), "created"

# create a Federated SDN
fedSDNSecurity=FederatedSDNSecurity.FederatedSDNSecurity("fedSDNSec_1")
print "FederatedSDNSecurity", fedSDNSecurity.getName(), "created"


print "------------- Create a Federated Cloud Network --------------------"
# get the network segments to be federated
network_segments=[]
cloud_member=""
for cloud_member in  cloudFederationMembers:
    network_segments.append(cloud_member[2])

#print "network segments:", network_segments
fedSDN.createNetworkFederation("FedCloudNetwork_1", network_segments)
print "Federated network", fedSDN.getNetworkFederationSegments("FedCloudNetwork_1"), "created"

# Associate a FederatedSecurityAgent with each network segment"

cloudManager=""
for cloudManager in  federationCloudManagers:
    network_segment=cloudManager.getNetworkSegments()
    fedSecAg=FederatedSecurityAgent.FederatedSecurityAgent("fedSecAg_"+network_segment[0])
    print "SecAgent", fedSecAg.getName(), "created"
    fedSecAg.setVNFManager(cloudManager.getVNFManager())
    fedSecAg.setNetworkSegment(cloudManager.getNetworkSegments())
    fedSDNSecurity.addSecurityAgent(fedSecAg)



print "----------- Analyse existing security VNF of federation network segments ----------"

# get GetListOfSecurityVNF

federationNetworkSegments=fedSDN.getNetworkFederationSegments("fedCloudNetwork")
#print "network segments are", federationNetworkSegments
vnf=""
authorizedProtocols=""
for federationNetworkSegment in federationNetworkSegments:
    vnf=fedSDNSecurity.getListOfSecurityVNF_networkSegment(federationNetworkSegment)
    print "Security VNF for ", federationNetworkSegment, "are", vnf
    authorizedProtocols=fedSDNSecurity.getListOfCommunicationProtocols_networkSegment(federationNetworkSegment)
    print "Authorized  protocols for", federationNetworkSegment, "are", authorizedProtocols


print "Security VNF federated network: ", fedSDNSecurity.getListOfSecurityVNF_all()
print "Communication protocol federated network: ", fedSDNSecurity.getListOfCommunicationProtocolsAll()

print "------------- Adapt VNF to respect global security policy: start new VNF and re-configure existing VNF --------"

federationNetworkSegments=fedSDN.getNetworkFederationSegments("fedCloudNetwork")
#print "network segments are", federationNetworkSegments
#vnfToStart=[["network_segment_1",[["fw_1", "fw_1_config"], ["encrypt_1", "encrypt_1_config"], ["decrypt_1", "decrypt_1_config"]]],["network_segment_2",[["ndpi_2", "ndpi_2_config"], ["encrypt_2", "encrypt_2_config"], ["decrypt_2", "decrypt_2_config"]]]]

#vnf=""
#for networkVNF in vnfToStart:
#    for vnf in networkVNF[1]:
#        fedSDNSecurity.startVNFOnNetworkSegment(networkVNF[0], vnf[0], vnf[1] )
#        print vnf[0], "started on", networkVNF[0], "with config", vnf[1]
    
# with open("HeatTemplate.txt", 'r') as stream:
with open("yamldoc.txt", 'r') as stream:
    try:
        yamlObject=yaml.load(stream)
        #print yamlObject
    except yaml.YAMLError as exc:
        print(exc)



for data in yamlObject.items():
    #print data
    key=""
    vnf_network_segment="none"
    vnf_configuration="config"
    for item in data:
        #print item 
        if (key=="clouds"):
            #print item
            for item1 in item.items():
                for clouds in item1[1].items():
                    #print clouds
                    if (clouds[0]=="CloudManager"):
                        #print clouds[0], ":", clouds[1] 
                        pass
                    elif (clouds[0]=="VM"):
                        #print clouds[0], ":", clouds[1] 
                        pass
                    elif (clouds[0]=="Network_segment"):
                        #print clouds[0], ":", clouds[1] 
                        pass                                          
                    elif (clouds[0]=="VNF"):
                        for VNFs in clouds[1].items():
                            #print VNFs[0] 
                            for VNF in VNFs[1].items():
                                if (VNF[0]=="configuration"):
                                    vnf_configuration=VNF[1]
                                elif (VNF[0]=="network_segment"):
                                    vnf_network_segment=VNF[1]  
                            fedSDNSecurity.startVNFOnNetworkSegment(vnf_network_segment, VNFs[0], vnf_configuration)                
                            print VNFs[0], "started on", vnf_network_segment, "with configuration", vnf_configuration
                    elif (clouds[0]=="Chaining"): 
                        chainingstr=""
                        for chaining in clouds[1].items():
                            for chainedVNF in chaining[1]:
                                chainingstr=chainingstr+" seq "+ chainedVNF   
                            print chaining[0], ":", chainingstr 
                                       
        elif (key=="configuration"):
            print key, ":", item
        key=item
            



print "-------- Verify that global security policy is implemented VNF per network Segment ----------"
print "network segments for", "FedCloudNetwork_1", "are", fedSDN.getNetworkFederationSegments("FedCloudNetwork_1")
network_segments=fedSDN.getNetworkFederationSegments("FedCloudNetwork_1")
network_segment=""
for network_segment in network_segments:          
        print "VNF for ", network_segment, "are", fedSDNSecurity.getListOfSecurityVNF_networkSegment(network_segment)

#print "Security VNF federated network: ", fedSDNSecurity.getListOfSecurityVNF_all()


print "------------- Run the network federation --------------"

print "VM_1: send packet to VM_2 with protocol HTTP"
print "VM_2: received packet from VM_1"
print " "
print "VM_1: send packet to VM_2 with protocol SKYPE"
print "DPI_1: unauthorized protocol detected: SKYPE"
print "FW_1: reconfiguring firewall on network network_segment_1 to block SKYPE protocol"
print " "
print "VM_1: send packet to VM_3 with protocol X "
print "ENCRYPT_1: VM_3 is in untrusted cloud: encrypt packet"
print "DECRYPT_3: packet for VM_3 from VM_1 is encrypted: decrypt packet using key XXX "


# now add a new network_segment_3 to the federation ==> need reconfigure/start new VNF for global security policy 




