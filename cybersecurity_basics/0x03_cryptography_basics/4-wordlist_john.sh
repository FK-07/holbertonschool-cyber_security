#!/bin/bash
[ -f /usr/share/wordlists/rockyou.txt.gz ] && sudo gunzip -k /usr/share/wordlists/rockyou.txt.gz; john --format=raw-sha256 --wordlist=/usr/share/wordlists/rockyou.txt "$1"; john --format=raw-sha256 --show "$1" | grep -E '^[^:]+:' | grep -v "password hash" | cut -d ':' -f 2 > 4-password.txt
