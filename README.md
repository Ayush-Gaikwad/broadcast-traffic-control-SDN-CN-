# Broadcast Traffic Control using SDN

## Overview
This project demonstrates Broadcast Traffic Control using Software Defined Networking (SDN) with Mininet and a POX controller. The controller dynamically manages network traffic using OpenFlow rules to reduce unnecessary broadcast flooding.

## Objective
- Implement SDN-based network using Mininet
- Use POX controller for traffic control
- Demonstrate broadcast behavior and flow rule management
- Analyze performance using ping and iperf

## Tools & Technologies
- Mininet (Network Emulator)
- POX Controller (Python-based SDN Controller)
- OpenFlow Protocol
- Wireshark (Packet Analysis)
- iperf (Performance Testing)

## Network Topology
- 1 Switch (s1)
- 4 Hosts (h1, h2, h3, h4)
- Custom topology created using Mininet

## Setup Instructions

### Start POX Controller


### Run Mininet Topology

## Execution Steps

### Connectivity Test


### Broadcast Traffic Generation

### Performance Testing

### View Flow Rules


## Observations
- Initial packets are broadcasted (flooding)
- Controller learns MAC addresses
- Flow rules are installed dynamically
- Broadcast traffic is reduced over time

## Output
- Mininet topology execution
- POX controller logs
- Flow table entries
- Ping results
- iperf results
- Wireshark packet capture

## Conclusion
The project successfully demonstrates how SDN can control broadcast traffic using a centralized controller. The use of dynamic flow rules improves network efficiency and reduces unnecessary broadcast flooding.

## Author
Ayush U Gaikwad  
SRN: PES2UG24AM036
