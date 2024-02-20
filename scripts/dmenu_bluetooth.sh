#!/bin/sh
. "${HOME}/.cache/wal/colors.sh"

action=$(echo -e "Toggle Bluetooth\nScan for Devices\nConnect to Device" | dmenu -l 3 -p "Bluetooth Menu:" -nb "$color0" -nf "$color15" -sb "$color1" -sf "$color15" -fn "Fira Code:size=12")

case "$action" in
    "Toggle Bluetooth")
        bluetoothctl power off
        sleep 1
        bluetoothctl power on
        ;;
    "Scan for Devices")
        bluetoothctl scan on &
        ;;
    "Connect to Device")
        devices=$(bluetoothctl devices | grep Device | cut -d ' ' -f 2- | sed 's/Device //' | dmenu -l 10 -p "Select Bluetooth device:" -nb "$color0" -nf "$color15" -sb "$color1" -sf "$color15" -fn "Fira Code:size=12")
        if [ -n "$devices" ]; then
            bluetoothctl connect "$devices"
        fi
        ;;
esac
