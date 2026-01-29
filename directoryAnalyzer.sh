#!/bin/bash

read -p "Enter directory path: " dir

if [ ! -d "$dir" ]; then
    echo "Directory does not exist!"
    exit 1
fi

file_count=$(find "$dir" -type f | wc -l)
dir_count=$(find "$dir" -type d | wc -l)

echo "Directory Analysis of $dir"
echo "-------------------------"
echo "Total files: $file_count"
echo "Total directories: $dir_count"

echo ""
echo "Top 5 largest files:"
find "$dir" -type f -exec du -h {} + | sort -rh | head -5

echo ""
echo "Total size of directory:"
du -sh "$dir"
