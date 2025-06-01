#!/bin/bash
set -e

MY_DIR="/opt/210225-ptm/platonova"
DIR1="$MY_DIR/task19_dir1"
DIR2="$MY_DIR/task19_dir2"

mkdir -p "$DIR1"
mkdir -p "$DIR2"

cd "$DIR1"

for i in {1..100}; do
	FILE_NAME=$RANDOM
	touch "$FILE_NAME"
done

echo "Done: creaeted DIR1, DIR2; 100 files in DIR1"
