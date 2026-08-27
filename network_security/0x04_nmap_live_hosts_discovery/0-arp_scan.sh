#!/bin/bash
# Check if subnetwork argument is provided
if [ -z "$1" ]; then
    exit 1
fi

# Run nmap with ARP host discovery and no port scan
nmap -PR -sn "$1"

