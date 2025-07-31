#!/bin/bash
# Sends GET with required header to validate route
curl -s -X GET -H "X-HolbertonSchool-User-Id: 98" "$1" | grep -E '^OK$'
