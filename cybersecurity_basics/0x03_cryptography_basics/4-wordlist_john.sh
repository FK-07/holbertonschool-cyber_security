#!/bin/bash
john --format=raw-sha256 --wordlist=/usr/share/wordlists/rockyou.txt "$1" >/dev/null 2>&1; john --format=raw-sha256 --show "$1" | grep ":" | head -n 1 | cut -d ':' -f 2 > 4-password.txt
