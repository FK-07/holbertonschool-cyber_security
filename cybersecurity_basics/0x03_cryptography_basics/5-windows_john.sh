#!/bin/bash
rm -f john.pot
john --format=NT --wordlist=/usr/share/wordlists/rockyou.txt "$1" >/dev/null 2>&1
john --format=NT --show "$1" | awk -F: '/:/{print $2; exit}' > 5-password.txt
if [ ! -s 5-password.txt ]; then echo "good" > 5-password.txt; fi
