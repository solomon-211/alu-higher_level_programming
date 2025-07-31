#!/bin/bash
# Displays all allowed HTTP methods for a URL
curl -sIX OPTIONS "$1" | grep -i 'Allow:' | cut -d' ' -f2-
