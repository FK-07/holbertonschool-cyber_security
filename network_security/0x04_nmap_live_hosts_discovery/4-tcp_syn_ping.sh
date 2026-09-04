#!/bin/bash
sudo nmap -sn -sS -PS22,80,443  $1
