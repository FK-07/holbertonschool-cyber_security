#!/bin/bash
find / -xdev -type d -perm -0002 -exec sh -c 'printf "%s\n" "$1"; chmod o-w "$1"' sh {} + 2>/dev/null
