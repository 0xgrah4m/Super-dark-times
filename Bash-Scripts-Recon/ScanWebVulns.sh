#!/bin/bash

domain=$1

subfinder -d "$domain" -silent | httpx -silent | nuclei -c 50 -t $HOME/nuclei-templates -severity critical,high,medium
