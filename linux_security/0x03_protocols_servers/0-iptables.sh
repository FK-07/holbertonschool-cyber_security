#!/usr/bin/env bash
# Script to display all current iptables rules with line numbers in a readable format

sudo iptables -L -v --line-numbers
