#!/bin/bash

# Define options for the power menu
options="Shutdown\nRestart\nLogout\nSuspend\nLock"

# Prompt the user to select an option using Rofi
selected_option=$(echo -e "$options" | rofi -dmenu -p "Power Menu" -i -lines 5 -width 20 -font "hack 12" -padding 20)

# Execute the selected option
case $selected_option in
    "Shutdown")
        systemctl poweroff
        ;;
    "Restart")
        systemctl reboot
        ;;
    "Logout")
        pkill -KILL -u "$USER"
        ;;
    "Suspend")
        systemctl suspend
        ;;
    "Lock")
        betterlockscreen --lock  # You can replace this with your preferred screen locker command
        ;;
    *)
        echo "Invalid option"
        ;;
esac
