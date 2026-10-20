#!/bin/bash
if [ -z "$1" ]; then
    grep -oE "\b([0-9]{1,3}\.){3}[0-9]{1,3}\b" auth.log | sort | uniq | wc -l
else
    grep -oE "\b([0-9]{1,3}\.){3}[0-9]{1,3}\b" $1 | sort | uniq | wc -l
fi
