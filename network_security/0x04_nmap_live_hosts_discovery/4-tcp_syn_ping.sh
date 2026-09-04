#!/bin/bash
sudo nmap -sn -sS 22,80,443  $1
