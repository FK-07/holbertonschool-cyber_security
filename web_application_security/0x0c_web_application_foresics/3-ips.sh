#!/bin/bash
input=$1
if [ -z "$input" ]; then
    input="auth.log"
fi
grep "Accepted" $input | grep -oE "\b([0-9]{1,3}\.){3}[0-9]{1,3}\b" | sort | uniq | wc -l
