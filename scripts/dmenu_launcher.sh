#!/bin/sh
. "${HOME}/.cache/wal/colors.sh"
exec dmenu_run -c -l 10 -nb "$color0" -nf "$color15" -sb "$color1" -sf "$color15" "$@"

