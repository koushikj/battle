import json

data = '{"NetworkAccessInfo":{"TrustSecControl":"ISE","xmlns:ns5":"http://www.cisco.com/UpgradePreChecksInfo","xmlns:ns6":"http://www.cisco.com/AgentlessPostureInfo","xmlns:ns3":"http://www.cisco.com/EndpointScriptsInfo","xmlns:ns4":"http://www.cisco.com/PxCloudInfo","xmlns:ns9":"http://www.cisco.com/LicenseInfo","xmlns:ns7":"http://www.cisco.com/ScriptRemediationPostureInfo","xmlns:ns8":"http://www.cisco.com/KongInfo","xmlns":"http://www.cisco.com/NetworkAccessInfo","xmlns:ns19":"http://www.cisco.com/ApiserviceInfo","xmlns:ns2":"http://www.cisco.com/DeploymentInfo","xmlns:ns18":"http://www.cisco.com/LinuxPostureInfo","xmlns:ns17":"http://www.cisco.com/HTTPTrustsecInfo","xmlns:ns16":"http://www.cisco.com/AlarmsInfo","xmlns:ns15":"http://www.cisco.com/ProfilerInfo","xmlns:ns14":"http://www.cisco.com/HealthCheckInfo","xmlns:ns13":"http://www.cisco.com/CountersInfo","xmlns:ns12":"http://www.cisco.com/MDMInfo","xmlns:ns11":"http://www.cisco.com/NADInfo","xmlns:ns10":"http://www.cisco.com/PeakCountsInfo","DeploymentID":"bae7ca8c-6705-4a3e-92cc-cd87782f7f8d","NodeList":{"Scope":"deployment","Node":{"NDGInfo":{"NDGHierarchyMap":"{0=0, 1=0, 2=3, 3=2, 4=0, 5=0, 6=0, 7=0, 8=0, 9=0, 10=0, 11=0, 12=0, 13=0, 14=0, 15=0, 16=0, 17=0, 18=0, 19=0, 20=0, 21=0, 22=0, 23=0, 24=0, 25=0, 26=0, 27=0, 28=0, 29=0, 30=0, 31=0, 32=0, 33=0, 34=0, 35=0, 36=0, 37=0, 38=0, 39=0, 40=0, 41=0, 42=0, 43=0, 44=0, 45=0, 46=0, 47=0, 48=0, 49=0, 50=0, 51=0, 52=0, 53=0, 54=0, 55=0, 56=0, 57=0, 58=0, 59=0, 60=0, 61=0, 62=0, 63=0, 64=0, 65=0, 66=0, 67=0, 68=0, 69=0, 70=0, 71=0, 72=0, 73=0, 74=0, 75=0, 76=0, 77=0, 78=0, 79=0, 80=0, 81=0, 82=0, 83=0, 84=0, 85=0, 86=0, 87=0, 88=0, 89=0, 90=0, 91=0, 92=0, 93=0, 94=0, 95=0, 96=0, 97=0, 98=0, 99=0}","NDGHeierarchyNADMap":"{2=3, 3=0}"},"AuthenticationTypeInfo":[{"EndpointCount":4,"FailedEndpointCount":3,"AuthenticationProtocol":"PAP_ASCII","PassedSessionCount":2,"FailedSessionCount":4,"AuthenticationMethod":"mab","PassedEndpointCount":2,"NasPortType":"Wireless - IEEE 802.11"},{"EndpointCount":1,"FailedEndpointCount":1,"AuthenticationProtocol":"","PassedSessionCount":0,"FailedSessionCount":1,"AuthenticationMethod":"dot1x","PassedEndpointCount":0,"NasPortType":""},{"EndpointCount":1,"FailedEndpointCount":0,"AuthenticationProtocol":"EAP-TLS","PassedSessionCount":1,"FailedSessionCount":0,"AuthenticationMethod":"dot1x","PassedEndpointCount":1,"NasPortType":"Ethernet"},{"EndpointCount":1,"FailedEndpointCount":1,"AuthenticationProtocol":"PEAP (EAP-MSCHAPv2)","PassedSessionCount":0,"FailedSessionCount":1,"AuthenticationMethod":"MSCHAPV2","PassedEndpointCount":0,"NasPortType":"Wireless - IEEE 802.11"},{"EndpointCount":1,"FailedEndpointCount":0,"AuthenticationProtocol":"Lookup","PassedSessionCount":1,"FailedSessionCount":0,"AuthenticationMethod":"webauth","PassedEndpointCount":1,"NasPortType":"Async"}],"AuthorizationInfo":{"ActiveVLANCount":0,"PolicyLineCount":0,"ActivedACLCount":4},"AuthenticationInfo":{"RADIUSIDStoreCount":0,"LocalIdentityNonAdminUserCount":0,"PolicyLineCount":0,"LDAPIDStoreCount":0,"OdbcInfo":{"ODBCCount":0},"ADAuthStoreCount":0,"RSAIDStoreCount":0,"RestIDInfo":{"RESTIDCount":0}}}},"isCsnEnabled":false,"xmlns:ns22":"http://www.cisco.com/FeedServiceInfo","xmlns:ns21":"http://www.cisco.com/IseCloudInfo","xmlns:ns20":"http://www.cisco.com/PostureInfo"}}'
json_data = json.loads(data)
print json_data
print json_data['NetworkAccessInfo']['NodeList']['Node']
auth_type_data = json_data['NetworkAccessInfo']['NodeList']['Node']['AuthenticationTypeInfo']
print auth_type_data
print len(auth_type_data)
print json.dumps(auth_type_data)
wireless_mab_pap_ascii = next(d for d in auth_type_data if d['AuthenticationProtocol'] == 'PAP_ASCII' and d['NasPortType'] == 'Wireless - IEEE 802.11' and d['AuthenticationMethod'] == 'mab')
print ("PAP_ASCII data {}".format(json.dumps(wireless_mab_pap_ascii)))
print wireless_mab_pap_ascii['FailedEndpointCount']
print wireless_mab_pap_ascii['PassedSessionCount']
print wireless_mab_pap_ascii['AuthenticationProtocol']
print wireless_mab_pap_ascii['NasPortType']
print wireless_mab_pap_ascii['EndpointCount']
print wireless_mab_pap_ascii['PassedEndpointCount']
print wireless_mab_pap_ascii['FailedSessionCount']
print wireless_mab_pap_ascii['AuthenticationMethod']

