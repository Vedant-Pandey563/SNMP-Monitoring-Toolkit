from pysnmp.hlapi import *

def get_snmp_data(oid):
    iterator = getCmd(
        SnmpEngine(),
        CommunityData('public', mpModel=0),
        UdpTransportTarget(('localhost', 161)),
        ContextData(),
        ObjectType(ObjectIdentity(oid))
    )

    error_indication, error_status, error_index, var_binds = next(iterator)

    if error_indication:
        print(f"SNMP Error: {error_indication}")
        return None
    elif error_status:
        print(f"{error_status.prettyPrint()} at {error_index}")
        return None
    else:
        for var_bind in var_binds:
            return var_bind[1]  # return the value

# Example usage
if __name__ == "__main__":
    print("📡 Starting SNMP data collection...")
    oid_sysname = '1.3.6.1.2.1.1.5.0'
    sysname = get_snmp_data(oid_sysname)
    print(f"System Name: {sysname}")
