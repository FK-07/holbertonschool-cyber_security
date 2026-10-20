#!/bin/bash
tail -n 1000 $1 | grep "Accepted" | awk '{print $9}' | head -n 1
