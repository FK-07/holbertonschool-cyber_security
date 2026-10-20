#!/bin/bash
# Script to audit and display non-commented SSH configuration settings

grep -v "^#" /etc/ssh/sshd_config | grep -v "^$"
