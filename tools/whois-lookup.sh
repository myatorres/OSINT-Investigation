#!/bin/bash
echo "Enter a domain name:"
read domain
whois $domain

# Run in Terminal
chmod +x tools/whois-lookup.sh
./tools/whois-lookup.sh
