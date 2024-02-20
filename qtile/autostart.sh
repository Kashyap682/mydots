#!/bin/bash
killall picom
picom --config ~/.config/picom/picom.conf &
killall dunst
dunst -config .config/dunst/dunstrc &
nitrogen --restore &
xfce4-power-manager &
flameshot &
lxsession &
udiskie &
clipmenud &
