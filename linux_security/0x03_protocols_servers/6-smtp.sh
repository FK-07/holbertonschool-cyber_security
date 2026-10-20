#!/bin/bash
postconf smtpd_tls_security_level | grep -E "^smtpd_tls_security_level"
