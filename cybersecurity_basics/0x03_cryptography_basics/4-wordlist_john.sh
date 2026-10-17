#!/bin/bash
[ -f /usr/share/wordlists/rockyou.txt.gz ] && gunzip -f /usr/share/wordlists/rockyou.txt.gz 2>/dev/null; john --format=raw-sha256 --wordlist=/usr/share/wordlists/rockyou.txt "$1" >/dev/null 2>&1; john --format=raw-sha256 --show "$1" | grep -vE "password hash|left|^$" | cut -d ':' -f 2 > 4-password.txt
