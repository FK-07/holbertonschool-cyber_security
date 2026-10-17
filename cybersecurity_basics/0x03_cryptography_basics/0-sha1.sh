#!/usr/bin/env bash
# Verilmiş parolu SHA-1 ilə heşləyib 0_hash.txt faylına yazır
echo -n "$1" | sha1sum | cut -d ' ' -f 1 > 0_hash.txt
