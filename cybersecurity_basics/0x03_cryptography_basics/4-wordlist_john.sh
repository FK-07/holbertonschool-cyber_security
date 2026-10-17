#!/bin/bash
john --wordlist=/usr/share/wordlists/rockyou.txt "$1" > /dev/null 2>&1 ; john --show "$1" | grep -v "password hash" | cut -d ':' -f 2 > 4-password.txt
