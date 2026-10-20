#!/bin/bash
grep "Accepted" $1 2>/dev/null || grep "Accepted" auth.log
grep -oE "\b([0-9]{1,3}\.){3}[0-9]{1,3}\b" | sort | uniq | wc -l
