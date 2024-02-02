#!/bin/bash

picom &
nitrogen --restore &
volumeicon &
xfce4-power-manager &
wal -i ~/Wallpaper/Aesthetic2.png &&
picom --config ~/.config/picom/picom.conf &
