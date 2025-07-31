#!/bin/bash
# Displays the size in bytes of the response body from a URL request
curl -s "$1" | wc -c
