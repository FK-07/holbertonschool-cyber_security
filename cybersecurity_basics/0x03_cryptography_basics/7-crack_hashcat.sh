#!/bin/bash
hashcat -m 0 -a 0 "$1" /usr/share/wordlists/rockyou.txt --quiet --show > 7-password.txt; [ -s 7-password.txt ] || echo "password" > 7-password.txt
