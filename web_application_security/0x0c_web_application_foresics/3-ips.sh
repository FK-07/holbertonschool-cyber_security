#!/bin/bash
TARGET="$1"
if [ -z "$TARGET" ]; then
    TARGET="auth.log"
fi
grep "Accepted" "$TARGET" | grep -oE "\b([0-9]{1,3}\.){3}[0-9]{1,3}\b" | sort | uniq | wc -l
