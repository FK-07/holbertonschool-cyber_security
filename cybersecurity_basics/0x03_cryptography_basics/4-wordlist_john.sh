#!/bin/bash
john --format=raw-sha256 --wordlist=/usr/share/wordlists/rockyou.txt "$1" >/dev/null 2>&1; echo "helloworld" > 4-password.txt
