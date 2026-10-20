#!/bin/bash
nmap -sU -p 161 --script snmp-public $1
