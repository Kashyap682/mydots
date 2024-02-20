#!/bin/sh
. "${HOME}/.cache/wal/colors.sh"

devices=$(bluetoothctl devices | grep Device | cut -d ' ' -f 2- | sed 's/Device //' | dmenu -c -l 4 -nb "$color0" -nf "$color15" -sb "$color1" -sf "$color15" -fn "Fira Code:size=12")

if [ -n "$devices" ]; then
    bluetoothctl connect "$devices"
fi

