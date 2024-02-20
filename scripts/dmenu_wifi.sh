#!/bin/sh
. "${HOME}/.cache/wal/colors.sh"

networks=$(nmcli -t -f SSID dev wifi list | dmenu -c -l 4 -nb "$color0" -nf "$color15" -sb "$color1" -sf "$color15" -fn "JetBrainsMono:size=12")

if [ -n "$networks" ]; then
    nmcli dev wifi connect "$networks"
fi

