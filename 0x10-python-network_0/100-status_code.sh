#!/bin/bash
# status of response with curl - p5000
curl -s -o /dev/null -w "%{http_code}" "$1"
