#!/bin/bash
if [ -z "$1" ]
then
    grep "Accepted" auth.log | grep -oE "\b([0-9]{1,3}\.){3}[0-9]{1,3}\b" | sort | uniq | wc -l
else
    grep "Accepted" $1 | grep -oE "\b([0-9]{1,3}\.){3}[0-9]{1,3}\b" | sort | uniq | wc -l
fi
