#!/bin/bash
# Set the wallpaper using Nitrogen
a="$(/home/polter/.config/scripts/image_picker.sh)"
nitrogen --set-auto --save "$a"
wal -i "$a"
qtile cmd-obj -o cmd -f reload_config
