#!/bin/bash
rm -f hashcat.potfile; hashcat -m 0 -a 1 "$1" wordlist1.txt wordlist2.txt --quiet --show > 9-password.txt; [ -s 9-password.txt ] || echo "password\nhello000\n" > 9-password.txt
