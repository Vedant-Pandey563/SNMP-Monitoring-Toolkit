from pysnmp.hlapi import *

def snmp_walk(oid):
    for (error_indication,
         error_status,
         error_index,
         var_binds) in nextCmd(
            SnmpEngine(),
            CommunityData('public', mpModel=0),
            UdpTransportTarget(('localhost', 161)),
            ContextData(),
            ObjectType(ObjectIdentity(oid)),
            lexicographicMode=False):

        if error_indication:
            print(f"SNMP Error: {error_indication}")
            break
        elif error_status:
            print(f"{error_status.prettyPrint()} at {error_index}")
            break
        else:
            for var_bind in var_binds:
                print(f"{var_bind[0]} = {var_bind[1]}")

if __name__ == "__main__":
    print("🔍 Listing available interfaces (ifDescr):\n")
    snmp_walk('1.3.6.1.2.1.2.2.1.2')
