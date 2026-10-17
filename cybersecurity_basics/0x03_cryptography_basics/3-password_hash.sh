#!/bin/bash
openssl passwd -6 -salt $(openssl rand -hex 8) "$1" > 3_hash.txt
