#!/bin/bash
set -e

#moving even files in DIR2

DIR1="/opt/210225-ptm/platonova/task19_dir1"
DIR2="/opt/210225-ptm/platonova/task19_dir2"

for  FILE in "$DIR1"/*; do
	FILE_NAME=$(basename "$FILE")

	if [[ "$FILE_NAME" =~ ^[0-9]+$ ]]; then
		if [ $((FILE_NAME % 2)) -eq 0 ]; then
			mv "$FILE" "$DIR2/"
			echo "File $FILE_NAME is even and removed in dir2"
		else
			echo "File $FILE_NAME is not even"
		fi
	fi
done
echo "script done"
