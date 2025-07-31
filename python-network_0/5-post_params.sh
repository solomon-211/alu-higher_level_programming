#!/bin/bash
# Sends POST request with email and subject, shows response body
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
