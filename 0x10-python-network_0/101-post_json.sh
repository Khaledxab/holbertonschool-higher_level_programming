#!/bin/bash
# sends a JSON POST to URL and display the body of the response
curl -s -X POST -H 'Content-Type: application/json' -d @"$2" "$1"
