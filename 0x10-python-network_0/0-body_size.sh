#!/bin/bash

# Check if a URL is provided as an argument
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Extract the URL from the argument
URL=$1

# Send a request to the URL using curl with the -s (silent) option
# and store the response body in a variable
response=$(curl -s "$URL")

# Calculate the size of the response body in bytes
size=$(echo -n "$response" | wc -c)

# Display the size of the response body
echo "$size"
