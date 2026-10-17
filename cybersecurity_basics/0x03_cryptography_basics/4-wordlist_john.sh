#!/bin/bash
john --wordlist=/usr/share/wordlists/rockyou.txt "$1" > /dev/null 2>&1; john --show "$1" | grep -vE "password hash|left|^$" | sed "s/:.*//" > 4-password.txt
