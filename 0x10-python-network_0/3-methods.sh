#!/bin/bash
# a Bash script that takes in a URL
curl -sX OPTIONS -i "$1" | grep "Allow" | awk -F ': ' '{print $2}'
