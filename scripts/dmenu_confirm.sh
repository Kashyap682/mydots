#!/bin/sh
. "${HOME}/.cache/wal/colors.sh"

input=$(echo -e "No\nYes" | dmenu -c -l 2 -nb "$color0" -nf "$color15" -sb "$color1" -sf "$color15" -fn "JetBrainsMono:size=10" -p "Are you sure? ")

echo "$input"

