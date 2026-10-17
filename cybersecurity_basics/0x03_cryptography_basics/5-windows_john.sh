#!/bin/bash
john --format=nt --wordlist=/usr/share/wordlists/rockyou.txt "$1" >/dev/null 2>&1; john --format=nt --show "$1" | grep -vE "password hash|left|^$" | cut -d ":" -f 2 > 5-password.txt
