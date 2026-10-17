#!/bin/bash
john --wordlist=/usr/share/wordlists/rockyou.txt "$1" > /dev/null 2>&1
john --show "$1" 2>/dev/null | grep -E "^[a-zA-Z0-9@!#\$