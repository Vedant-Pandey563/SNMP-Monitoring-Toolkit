import time
import matplotlib.pyplot as plt
from pysnmp.hlapi import *

# --- CONFIG ---
TARGET = 'localhost'
COMMUNITY = 'public'
IF_INDEX = 11  # change if needed

OID_IN = f'1.3.6.1.2.1.2.2.1.10.{IF_INDEX}'  # ifInOctets
OID_OUT = f'1.3.6.1.2.1.2.2.1.16.{IF_INDEX}'  # ifOutOctets

def get_snmp_value(oid):
    for (errInd, errStat, errIdx, varBinds) in getCmd(
        SnmpEngine(),
        CommunityData(COMMUNITY, mpModel=1),
        UdpTransportTarget((TARGET, 161)),
        ContextData(),
        ObjectType(ObjectIdentity(oid))
    ):
        if errInd or errStat:
            return None
        for vb in varBinds:
            return int(vb[1])
    return None

# --- Initialize ---
print("📡 Starting live SNMP bandwidth monitor... (Press Ctrl+C to stop)")

in_prev = get_snmp_value(OID_IN)
out_prev = get_snmp_value(OID_OUT)
time_prev = time.time()

times, in_rates, out_rates = [], [], []

plt.ion()
fig, ax = plt.subplots(figsize=(8, 4))
line_in, = ax.plot([], [], label='Inbound (Bytes/sec)', color='tab:blue')
line_out, = ax.plot([], [], label='Outbound (Bytes/sec)', color='tab:orange')

ax.set_title("📈 Live SNMP Bandwidth Usage")
ax.set_xlabel("Time (s)")
ax.set_ylabel("Bytes per Second")
ax.legend()
plt.tight_layout()

try:
    while True:
        time.sleep(2)
        in_now = get_snmp_value(OID_IN)
        out_now = get_snmp_value(OID_OUT)
        time_now = time.time()

        if None in (in_now, out_now):
            print("⚠️ SNMP read error — skipping this cycle.")
            continue

        dt = time_now - time_prev
        in_rate = (in_now - in_prev) / dt
        out_rate = (out_now - out_prev) / dt

        # Handle SNMP counter reset
        if in_rate < 0: in_rate = 0
        if out_rate < 0: out_rate = 0

        print(f"[{time.strftime('%H:%M:%S')}] In: {in_rate:.1f} B/s | Out: {out_rate:.1f} B/s")

        times.append(time_now - times[0] if times else 0)
        in_rates.append(in_rate)
        out_rates.append(out_rate)

        # Update plot
        line_in.set_data(times, in_rates)
        line_out.set_data(times, out_rates)
        ax.relim()
        ax.autoscale_view()

        plt.pause(0.1)

        in_prev, out_prev, time_prev = in_now, out_now, time_now

except KeyboardInterrupt:
    print("\n🛑 Monitoring stopped by user.")
    plt.ioff()
    plt.show()
