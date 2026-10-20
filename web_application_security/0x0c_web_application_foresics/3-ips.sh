#!/bin/bash
file=$1
if [ -z "$file" ]; then
    file="auth.log"
fi
grep "Accepted" $file | grep -oE "\b([0-9]{1,3}\.){3}[0-9]{1,3}\b" | sort | uniq | wc -l
