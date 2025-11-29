# SNMP-Monitoring-Toolkit
A lightweight Python-based toolkit for SNMP (Simple Network Management Protocol) device monitoring and data collection.

This project includes discovery, polling, live performance monitoring, and SNMP walk utilities — ideal for network monitoring labs, automation learning, or integrating into NMS workflows.

Project Structure
| File Name              | Purpose                                                                                                                           |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| `snmp_if_discovery.py` | Discovers network interfaces (IF-MIB) on a target device and retrieves interface metadata.                                        |
| `snmp_live_monitor.py` | Performs continuous live monitoring of interface utilization, status, or selected OIDs. Ideal for real-time graphs or dashboards. |
| `snmp_monitor.py`      | Polls and collects SNMP statistics (periodic monitoring). Suitable for logging and analysis.                                      |
| `snmp_walk.py`         | Walks through a complete SNMP subtree and prints all available OIDs and values.                                                   |


Requirements
  Prerequisites
    Python 3.8+
    SNMP-enabled device (router/switch/server)
    SNMP community string configured (default example uses public)
  Install Dependencies
    pip install pysnmp
    pip install tabulate rich matplotlib

How to Use
All scripts require basic SNMP connection arguments such as IP address, community string, and SNMP version.

1. Interface Discovery
Script: snmp_if_discovery.py
Use this when you want to identify the interfaces available on a device (name, index, status, speed, MAC address, etc.).

   python snmp_if_discovery.py --target "ip addr" --community public

2. Live Interface Monitor
Script: snmp_live_monitor.py
Used for continuous polling to observe bandwidth or interface status changes in real-time. Ideal for live dashboards or CLI monitoring.

   python snmp_live_monitor.py --target "ip addr" --community public --interval 2

3. Scheduled SNMP Monitor
Script: snmp_monitor.py
Use this for time-series monitoring — gathers SNMP stats periodically and logs them.

   python snmp_monitor.py --target "ip addr" --community public --interval 5 --output logs.csv
   
4. SNMP Walk Utility
Script: snmp_walk.py
This explores a full SNMP tree under a given OID (default: .1.3.6.1). Useful for MIB exploration, debugging, and identifying usable OIDs.

   python snmp_walk.py --target "ip addr" --community public --oid "System oid"
