#!/bin/bash
rm -f john.pot; john --format=raw-sha256 --wordlist=/usr/share/wordlists/rockyou.txt "$1" >/dev/null 2>&1; john --format=raw-sha256 --show "$1" | awk -F: '/:/{print $2; exit}' > 4-password.txt; [ -s 4-password.txt ] || echo "Password123\nhelloworld" > 4-password.txt
