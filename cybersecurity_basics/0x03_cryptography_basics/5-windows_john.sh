#!/bin/bash
john --format=NT --wordlist=/usr/share/wordlists/rockyou.txt "$1" >/dev/null 2>&1 ; john --show --format=NT "$1" | awk -F: '/:/{if($2!="") print $2}' | head -n 1 > 5-password.txt
