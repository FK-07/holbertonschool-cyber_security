#!/bin/bash
if [ -z "$1" ]; then
    tail -n 1000 auth.log | grep "Accepted" | awk '{print $9}' | head -n 1
else
    tail -n 1000 $1 | grep "Accepted" | awk '{print $9}' | head -n 1
fi
