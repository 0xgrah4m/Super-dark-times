#!/bin/bash

alvo="$1"
while IFS= read -r dir; do
    reply=$(curl -A "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTM>
    if [ $reply == 200 ]; then
        echo "diretorio encontrado:$dir"
    fi
done < wordlist.txt
