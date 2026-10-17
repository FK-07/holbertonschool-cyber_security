#!/bin/bash
if [ ! -f /usr/share/wordlists/rockyou.txt ] && [ -f /usr/share/wordlists/rockyou.txt.gz ]; then gunzip /usr/share/wordlists/rockyou.txt.gz 2>/dev/null || true; fi
john --format=raw-sha256 --wordlist=/usr/share/wordlists/rockyou.txt "$1" > /dev/null 2>&1
john --format=raw-sha256 --show "$1" | grep -vE "password hash|left|^$" | sed "s/:.*//" > 4-password.txt
