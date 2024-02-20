#!/bin/sh
. "${HOME}/.cache/wal/colors.sh"

image_dir="/home/polter/Pictures/wallpapers/"

selected=$(find "$image_dir" -type f -name "*.jpg" -o -name "*.jpeg" -o -name "*.png" -o -name "*.webp" | sed "s|^$image_dir/||" | dmenu -c -l 10 -nb "$color0" -nf "$color15" -sb "$color1" -sf "$color15" -fn "Fira Code:size=12")

if [ -n "$selected" ]; then
    echo "$selected" &
fi

