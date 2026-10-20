#!/bin/bash
# Script to find world-writable directories, print them, and secure their permissions

find / -type d -perm -0002 2>/dev/null | while read -r dir; do
    echo "$dir"
    chmod o-w "$dir"
done
