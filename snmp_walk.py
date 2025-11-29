from pysnmp.hlapi import *

target = 'localhost'
community = 'public'
base_oid = '1.3.6.1.2.1.2.2.1.10'  # ifInOctets

for (errorIndication, errorStatus, errorIndex, varBinds) in nextCmd(
        SnmpEngine(),
        CommunityData(community, mpModel=1),
        UdpTransportTarget((target, 161)),
        ContextData(),
        ObjectType(ObjectIdentity(base_oid)),
        lexicographicMode=False):

    if errorIndication:
        print(errorIndication)
        break
    elif errorStatus:
        print('%s at %s' % (errorStatus.prettyPrint(),
                            errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
        break
    else:
        for varBind in varBinds:
            print(' = '.join([x.prettyPrint() for x in varBind]))
