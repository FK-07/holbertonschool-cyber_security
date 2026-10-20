#!/bin/bash
find / -type d -perm -0002 -exec sh -c 'echo "$1"; chmod o-w "$1"' sh {} + 2>/dev/null
