from color import rose_pine_moon, custom
import os
from libqtile.lazy import lazy
import libqtile.widget
from libqtile import qtile

from libqtile.bar import Bar
from libqtile.widget.battery import Battery
from libqtile.widget.clock import Clock
from libqtile.widget.currentlayout import CurrentLayout
from libqtile.widget.currentlayout import CurrentLayoutIcon
from libqtile.widget.groupbox import GroupBox
from libqtile.widget.sep import Sep
from libqtile.widget.systray import Systray
from libqtile.widget.window_count import WindowCount
from libqtile.widget.windowname import WindowName
from libqtile.widget.volume import Volume
from libqtile.widget.bluetooth import Bluetooth
from libqtile.widget.wlan import Wlan
from libqtile.widget.backlight import Backlight

from qtile_extras import widget
from qtile_extras.widget.decorations import BorderDecoration

def winName(text):
	strings_to_remove = ["Google Chrome", "Firefox", "Geany", "Thunar", "Kitty"]
	for string in strings_to_remove:
		if string in text:
			text = string
	return text

bar = Bar([
	Sep(
                padding = 12,
                linewidth = 0,
                size_percent = 10,
        ),
	GroupBox(
                font = "Noto Sans CJK Bold",
                margin_x = 8,
                fontsize = 14,
                borderwidth = 3,
                highlight_method = "line",
                urgent_alert_method = "line",
                active = custom['color3'],
                inactive = custom['foreground'],
                this_current_screen_border = custom['color1'],
                urgent_border = rose_pine_moon['Love'],
                disable_drag = True,
                hide_unused = True,
        ),
        Sep(
                padding = 12,
                linewidth = 5,
                size_percent = 10,
        ),
	CurrentLayoutIcon(
                foreground = custom['foreground'],
                padding = 4,
                scale = 0.6,
        ),
        CurrentLayout(
		font = "JetBrainsMono Nerd Font Bold",
		fontsize = 14,
		foreground = custom['foreground'],
                padding = 5
        ),
        Sep(
                padding = 12,
                linewidth = 5,
                size_percent = 10,
        ),
        widget.Mpris2(
                background = custom['background'],
                foreground = custom['foreground'],
                name = "spotify",
                objname = "org.mpris.MediaPlayer2.spotify",
                fmt = "  {}",
                format = "{xesam:title} - {xesam:artist} ",
                scroll_chars = 20,
                fontsize = 14,
        ),
        widget.Prompt(
                background = custom['background'],
                foreground = custom['foreground'],
                font = "JetBrainsMono Nerd Font Bold",
                fontsize = 13,
        ),
        widget.Chord(
		font = "JetBrainsMono Nerd Font Bold",
                chords_colors = {"launch": ("#ff0000", "#ffffff"),},
                name_transform = lambda name: name.upper(),
        ),
        Sep(
                padding = 12,
                linewidth = 5,
                size_percent = 10,
        ),
        WindowName(
		font = "JetBrainsMono Nerd Font Bold",
		foreground = custom['foreground'],
		fontsize = 14,
		max_chars = 50,
		parse_text = winName,
		padding = 6,
	),
        Wlan(
		fontsize = 13,
		foreground = custom['foreground'],
		format = '  {essid} {percent:2.0%}',
		disconnected_message = "󰖪 ",
		padding = 5,
		mouse_callbacks = {
			"Button1": lambda: qtile.cmd_spawn("/home/polter/.config/scripts/dmenu_wifi.sh")
                },
        ),
	Sep(
                padding = 12,
                linewidth = 5,
                size_percent = 10,
        ),
        Bluetooth(
		fontsize = 14,
		foreground = custom['foreground'],
		default_text = "  {connected_devices}",
		padding = 5,
		mouse_callbacks = {
			"Button1": lambda: qtile.cmd_spawn("/home/polter/.config/scripts/dmenu_bluetooth.sh")
                },
        ),
	Sep(
                padding = 12,
                linewidth = 5,
                size_percent = 10,
        ),
        Volume(
		fontsize = 16,
		foreground = custom['foreground'],
		padding = 5,
		emoji = True,
		emoji_list = ["󰝟", "", "", ""],
        ),
        Volume(),
	Sep(
                padding = 12,
                linewidth = 5,
                size_percent = 10,
        ),
        Battery(
		fontsize = 14,
		format = "{char} {percent:2.0%}",
		discharge_char = " ",
		empty_char = " ",
		full_char = " ",
		charge_char = "",
		update_interval = 1,
		low_percentage = 0.2,
		notify_below = 20,
		foreground = custom['foreground'],
		low_foreground = rose_pine_moon['Rose'],
		mouse_callbacks = {
			"Button1": lambda: qtile.cmd_spawn("xfce4-power-manager-settings"),
                },
        ),
        Sep(
                padding = 12,
                linewidth = 5,
                size_percent = 10,
        ),
        Clock(
		format='  %d-%m-%y',
		fontsize = 14,
		foreground = custom['foreground'],
		mouse_callbacks = {
			"Button1": lambda: qtile.cmd_spawn("kitty -c /home/polter/.config/kitty/themes/rose-pine-moon.conf calcurse"),
                },
        ),
        Sep(
                padding = 12,
                linewidth = 5,
                size_percent = 10,
        ),
        Clock(
		format=' %H:%M',
		fontsize = 14,
		foreground = custom['foreground'],
        ),
        Sep(
                padding = 12,
                linewidth = 0,
                size_percent = 10,
        ),
        Systray(),
        Sep(
                padding = 12,
                linewidth = 0,
                size_percent = 10,
        ),
    ],
        size = 36,
        margin = [5, 5, 5, 5],
        background = custom['background'],
        opacity = 1,
)
