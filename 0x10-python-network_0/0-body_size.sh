#!/usr/bin/env bash
#displays the size of the body of the response
curl -sI "$1" -o /dev/null -w '%{size_download}'
