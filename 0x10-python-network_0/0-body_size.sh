#!/bin/bash
# This script takes a URL, sends a request, and displays the body size in bytes
curl -sI "$1" | grep "Content-Length" | cut -d ' ' -f 2
