#!/bin/bash
john --format=raw-sha256 --wordlist=/usr/share/wordlists/rockyou.txt "$1" >/dev/null 2>&1
john --format=raw-sha256 --show "$1" | awk -F: '/:/{print $2; exit}' > 6-password.txt
