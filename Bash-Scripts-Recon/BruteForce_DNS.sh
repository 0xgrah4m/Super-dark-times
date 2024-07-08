#!/bin/bash

domain="$1"
for dns in $(cat wordlist.txt); do
    host $dns.$domain | grep -v "NXDOMAIN"
done

_______________ Reverse brute force DNS - Resolve address _______________
#!/bin/bash

ip="37.59.174"
for n in $(seq 224 239); do
    host -t PTR $ip.$n | grep -v "37-59-174" | cut -d " " -f5
done
