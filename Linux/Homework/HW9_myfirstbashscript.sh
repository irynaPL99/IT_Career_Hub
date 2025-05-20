#!/bin/bash
set -e

USER=Iryna

echo "$(date +"%d.%m.%Y")"
echo "hello $USER"
echo "$(pwd)"
echo "$(ps -ef|grep bioset|grep -v grep|wc -l)"
echo "$(ls -l /etc/passwd|awk '{print $1}')"


echo "done"
