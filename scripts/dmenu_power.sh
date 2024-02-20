#!/bin/sh
. "${HOME}/.cache/wal/colors.sh"

selected="$(echo -e "Lock\nShutdown\nReboot\nLogout\nSuspend" | dmenu -c -l 5 -nb "$color0" -nf "$color15" -sb "$color1" -sf "$color15" -fn "JetBrainsMono:size=12")"

case "$selected" in
    "Logout")
        a=$($HOME/.config/scripts/dmenu_confirm.sh)
        if [[ $a == "y" || $a == "Y" || $a == "yes" || $a == "Yes" || $a == "YES" ]]; then
            pkill -KILL -u "$USER"
        fi
        ;;
    "Reboot")
        a=$($HOME/.config/scripts/dmenu_confirm.sh)
        if [[ $a == "y" || $a == "Y" || $a == "yes" || $a == "Yes" || $a == "YES" ]]; then
            systemctl reboot
        fi
        ;;
    "Shutdown")
        a=$($HOME/.config/scripts/dmenu_confirm.sh)
        if [[ $a == "y" || $a == "Y" || $a == "yes" || $a == "Yes" || $a == "YES" ]]; then
            systemctl poweroff
        fi
        ;;
    "Suspend")
        a=$($HOME/.config/scripts/dmenu_confirm.sh)
        if [[ $a == "y" || $a == "Y" || $a == "yes" || $a == "Yes" || $a == "YES" ]]; then
            amixer set Master mute
            betterlockscreen --suspend
        fi
        ;;
    "Lock")
        a=$($HOME/.config/scripts/dmenu_confirm.sh)
        if [[ $a == "y" || $a == "Y" || $a == "yes" || $a == "Yes" || $a == "YES" ]]; then
            betterlockscreen -l blur
        fi
        ;;
esac

