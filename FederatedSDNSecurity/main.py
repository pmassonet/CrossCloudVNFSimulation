

'''
Created on 12 janv. 2016

@author: phm
'''

import FederatedSDN
import FederatedSDNSecurity
import FederatedSecurityAgent
import VNFManager
import CloudManager

 
import ssl, socket



inputMessage="Press enter to continue"


federationCloudManagers=[]


cloudFederationMembers=[
    ["cloud_man_1","vnf_manager_1", "network_segment_1", [["" ]],[""]],  
    ["cloud_man_2","vnf_manager_2", "network_segment_2", [[""]],[""]],
    ["cloud_man_3","vnf_manager_3", "network_segment_3", [[""]],[""]]
]


print "-----------Initial setup of Cloud_1, cloud_2 and cloud_3 -----------"

cloudMember=""
for cloudMember in cloudFederationMembers:
    # create a cloud manager
    cloud_manager=CloudManager.CloudManager(cloudMember[0])
    print "Cloud manager", cloud_manager.getName(), "in federation"
    federationCloudManagers.append(cloud_manager)
    # set the network segments
    cloud_manager.setNetworkSegments(cloudMember[2])
    # create a VNF manager
    vnfManager=VNFManager.VNFManager(cloudMember[1])
    cloud_manager.setVNFManager(vnfManager)

    



print "------------ start Federated SDN ---------------"

# create a federated SDN
fedSDN=FederatedSDN.FederatedSDN("fedSDN_1")
print "FederatedSDN", fedSDN.getIdentifier(), "created"

# create a Federated SDN security
fedSDNSecurity=FederatedSDNSecurity.FederatedSDNSecurity("fedSDNSec_1")
print "FederatedSDNSecurity", fedSDNSecurity.getName(), "created"


print "------------- Create a Federated Cloud Network --------------------"
# get the network segments to be federated
network_segments=["network_segment_1","network_segment_2"]
#cloud_member=""
#for cloud_member in  cloudFederationMembers:
#    network_segments.append(cloud_member[2])

#print "network segments:", network_segments
fedSDN.createNetworkFederation("FedCloudNetwork_1", network_segments)
print "Federated network", fedSDN.getNetworkFederationSegments("FedCloudNetwork_1"), "created"

# Associate a FederatedSecurityAgent with each network segment"

cloudManager=""
for cloudManager in  federationCloudManagers:
    network_segment=cloudManager.getNetworkSegments()
    fedSecAg=FederatedSecurityAgent.FederatedSecurityAgent("fedSecAg_"+network_segment[0])
    #print "SecAgent", fedSecAg.getName(), "created"
    fedSecAg.setVNFManager(cloudManager.getVNFManager())
    fedSecAg.setNetworkSegment(cloudManager.getNetworkSegments())
    fedSDNSecurity.addSecurityAgent(fedSecAg)



#print "----------- Analyse existing security VNF of federation network segments ----------"

#print "------------- Adapt VNF to respect global security policy: start new VNF and re-configure existing VNF --------"


print "------------- Deploy, configure and start VNF to respect global security policy --------"
wait = raw_input(inputMessage)
fedSDNSecurity.readYAMLfile("YAML1.txt")
#fedSDNSecurity.readYAMLfileV2("Cloud1-2-Heat.yaml")


print "-------- Verify that global security policy is correctly implemented in each federation cloud network ----------"

wait = raw_input(inputMessage)
fedSDNSecurity.verifySecurityPolicy(fedSDN)



print "------------- Run the network federation --------------"
wait = raw_input(inputMessage)

print "VM_1: send packet to VM_2 with protocol HTTP"
print "VM_2: received packet from VM_1"
print " "
print "VM_1: send packet to VM_2 with protocol SKYPE"
print "DPI_1: unauthorized protocol detected: SKYPE"
print "FW_1: reconfiguring firewall on network network_segment_1 to block SKYPE protocol"



print "------------- now add a new network_segment_3 to the federation and extend the security policy--------------"
wait = raw_input(inputMessage)

# add network segment to federation
fedSDN.addNetworkSegment("network_segment_3")
print "Federated network", fedSDN.getNetworkFederationSegments("FedCloudNetwork_1"), "extended"
fedSDNSecurity.readYAMLfile("YAML2.txt")

print "-------- Verify that global security policy is implemented VNF per network Segment ----------"

wait = raw_input(inputMessage)
fedSDNSecurity.verifySecurityPolicy(fedSDN)

 
print "------------- Run the network federation --------------"
wait = raw_input(inputMessage)

print "VM_1: send packet to VM_3 with protocol X "
print "ENCRYPT_1: VM_3 is in untrusted cloud: encrypt packet"
print "DECRYPT_3: packet for VM_3 from VM_1 is encrypted: decrypt packet using key XXX "




