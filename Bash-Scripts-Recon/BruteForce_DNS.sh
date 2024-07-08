#!/bin/bash

domain="$1"
for dns in $(cat wordlist.txt); do
    host $dns.$domain | grep -v "NXDOMAIN"
done
