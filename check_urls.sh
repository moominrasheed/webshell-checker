#!/bin/bash

if [[ $# -ne 1 ]]; then
  echo "Usage: $0 input_file"
  exit 1
fi

input_file=$1

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
NC='\033[0m'

while IFS= read -r line; do
  if [[ $line == http* ]]; then
    echo "$line" >> urls.txt
  fi
done < "$input_file"

while IFS= read -r url; do
  if curl -s --head "$url" | head -n 1 | grep "HTTP/1.[01] [23].." > /dev/null; then
    if curl -s --max-time 10 "$url" | grep -qiE 'Webshell|0byt3m1n1|IndoXploit|Shell|shell|wso|Upload Please|title'; then
      echo -e "[${GREEN}OK!${NC}] $url"
      echo "$url" >> done.txt
    else
      echo -e "[${YELLOW}BAD${NC}] $url"
    fi
  else
    echo -e "[${RED}ERROR${NC}] $url"
  fi
done < "urls.txt"
