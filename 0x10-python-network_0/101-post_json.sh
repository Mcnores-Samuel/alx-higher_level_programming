#!/bin/bash
# sends a JSON POST request to a URL passed as the first argument.
curl -sX POST -d "$2" "$1"
