#!/bin/bash

python3 -c '
import sys
import base64

def decode_websphere(encoded):
    if encoded.startswith("{xor}"):
        encoded = encoded[5:]
    try:
        raw = base64.b64decode(encoded)
    except Exception:
        return ""
    
    decoded = "".join(chr(b ^ 0x5f) for b in raw)
    return decoded

if len(sys.argv) > 1:
    print(decode_websphere(sys.argv[1]))
' "$1"
