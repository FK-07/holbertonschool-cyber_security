#!/bin/bash
if [ -z "$1" ]; then
    grep "Linux version" dmesg
else
    grep "Linux version" $1
fi
