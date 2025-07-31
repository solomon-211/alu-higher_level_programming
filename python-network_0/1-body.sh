#!/bin/bash
# Sends GET request and displays body only for 200 status responses
curl -s -X GET -w "%{http_code}" "$1" | awk '/^200$/{getline; print}'
