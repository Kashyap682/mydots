import os
import subprocess

from libqtile import bar, layout, qtile, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen, KeyChord
from libqtile.lazy import lazy

mod = "mod4"
terminal = "kitty"
browser = "firefox"

keys = [
	
	# Basic Applications
	Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
	Key([mod, "shift"], "f", lazy.spawn("thunar"), desc="Launch Thunar"),
	Key([mod], "d", lazy.spawn("rofi -show drun"), desc="Launch Rofi"),	
	Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    
    
    # Qtile Control
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "shift"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod], "x", lazy.spawn("/home/polter/.config/scripts/rofi-power-menu.sh"), desc="Rofi Power Menu"),
	
    # Workspace Control
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen on the focused window"),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),    
]

groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend(
        [
            # mod1 + group number = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + group number = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + group number = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layout_theme = {
	"border-width": 2,
	"margin": 8,
	"border_focus": '#e8dfD6',
	"border_normal": '#021b21',
}

layouts = [
    layout.MonadTall(**layout_theme),
    layout.Columns(**layout_theme),
    layout.Max(**layout_theme),
    layout.Floating(**layout_theme),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

# Colors
colors = [
    ["#021b21", "#021b21"],  # 0
    ["#032c36", "#065f73"],  # 1
    # ["#032c36", "#61778d"],# 1 this one is bit lighter, it is for inactive workspace icons.
    ["#e8dfd6", "#e8dfd6"],  # 2
    ["#c2454e", "#c2454e"],  # 3
    ["#44b5b1", "#44b5b1"],  # 4
    ["#9ed9d8", "#9ed9d8"],  # 5
    ["#f6f6c9", "#f6f6c9"],  # 6
    ["#61778d", "#61778d"],  # 7
    ["#e2c5dc", "#e2c5dc"],  # 8
    ["#5e8d87", "#5e8d87"],  # 9
    ["#032c36", "#032c36"],  # 10
    ["#2e3340", "#2e3340"],  # 11
    ["#065f73", "#065f73"],  # 12
    ["#8a7a63", "#8a7a63"],  # 13
    ["#A4947D", "#A4947D"],  # 14
    ["#BDAD96", "#BDAD96"],  # 15
    ["#a2d9b1", "#a2d9b1"],  # 16
]


widget_defaults = dict(
    font="sans",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

def search():
    qtile.cmd_spawn("rofi -show drun")

def power():
    qtile.cmd_spawn("sh -c ~/.config/scripts/rofi-power-menu.sh")

def top_bar():
    return [
        widget.Sep(
            padding=6,
            linewidth=0,
            background=colors[6],
        ),
        widget.TextBox(
            # text="  ",
            text="  ",
            font="Iosevka Nerd Font",
            fontsize="18",
            background=colors[6],
            foreground=colors[0],
            mouse_callbacks={
                "Button1": lambda: qtile.cmd_spawn("rofi -show drun -modi drun")
            },
        ),
        widget.TextBox(
            text="\ue0be",
            font="Inconsolata for powerline",
            fontsize="33",
            padding=0,
            background=colors[6],
            foreground=colors[0],
        ),
        widget.GroupBox(
            font="Ubuntu Nerd Font",
            fontsize=16,
            margin_y=3,
            margin_x=6,
            padding_y=7,
            padding_x=6,
            borderwidth=4,
            active=colors[8],
            inactive=colors[1],
            rounded=False,
            highlight_color=colors[3],
            highlight_method="block",
            this_current_screen_border=colors[6],
            block_highlight_text_color=colors[0],
        ),
        widget.Prompt(
            background=colors[2],
            foreground=colors[0],
            font="Iosevka Nerd Font",
            fontsize=18,
        ),
        widget.Chord(
            chords_colors={
                "launch": ("#ff0000", "#ffffff"),
            },
            name_transform=lambda name: name.upper(),
        ),
        widget.TextBox(
            text="\ue0be",
            font="Inconsolata for powerline",
            fontsize=33,
            padding=0,
            background=colors[0],
            foreground=colors[2],
        ),
        widget.WindowName(
            font="Iosevka Nerd Font",
            fontsize=15,
            background=colors[2],
            foreground=colors[0],
        ),
        widget.TextBox(
            text="\ue0be",
            font="Inconsolata for powerline",
            fontsize="33",
            padding=0,
            background=colors[2],
            foreground=colors[0],
        ),
        widget.Spacer(length=200),
        widget.TextBox(
            text="\ue0be",
            font="Inconsolata for powerline",
            fontsize="33",
            padding=0,
            background=colors[0],
            foreground=colors[10],
        ),
        widget.CurrentLayoutIcon(
            custom_icon_paths=[os.path.expanduser("~/.config/qtile/icons")],
            scale=0.45,
            padding=0,
            background=colors[10],
            foreground=colors[2],
            font="Iosevka Nerd Font",
            fontsize=14,
        ),
        widget.CurrentLayout(
            font="Iosevka Nerd Font",
            fontsize=15,
            background=colors[10],
            foreground=colors[2],
        ),
        widget.TextBox(
            text="\ue0be",
            font="Inconsolata for powerline",
            fontsize="33",
            padding=0,
            background=colors[10],
            foreground=colors[11],
        ),
        widget.TextBox(
            text=" ",
            font="Iosevka Nerd Font",
            fontsize=18,
            padding=0,
            background=colors[11],
            foreground=colors[2],
        ),
        widget.DF(
            fmt=" {}",
            font="Iosevka Nerd Font",
            fontsize=15,
            partition="/home",
            format="{uf}{m} ({r:.0f}%)",
            visible_on_warn=False,
            background=colors[11],
            foreground=colors[2],
            padding=5,
            mouse_callbacks={"Button1": lambda: qtile.cmd_spawn("kitty -e bashtop")},
        ),
        widget.TextBox(
            text="\ue0be",
            font="Inconsolata for powerline",
            fontsize="33",
            padding=0,
            background=colors[11],
            foreground=colors[12],
        ),
        widget.TextBox(
            text=" ",
            font="Iosevka Nerd Font",
            fontsize=16,
            foreground=colors[2],
            background=colors[12],
            padding=0,
            mouse_callbacks={"Button1": lambda: qtile.cmd_spawn("kitty -e bashtop")},
        ),
        widget.Memory(
            background=colors[12],
            foreground=colors[2],
            font="Iosevka Nerd Font",
            fontsize=15,
            format="{MemUsed: .0f} MB",
            mouse_callbacks={"Button1": lambda: qtile.cmd_spawn("kitty -e bashtop")},
        ),
        widget.Sep(
            padding=8,
            linewidth=0,
            background=colors[12],
        ),
        widget.TextBox(
            text="\ue0be",
            font="Inconsolata for powerline",
            fontsize="33",
            padding=0,
            background=colors[12],
            foreground=colors[7],
        ),
        widget.Sep(
            padding=6,
            linewidth=0,
            background=colors[7],
        ),
        widget.Systray(
            background=colors[7],
            foreground=colors[2],
            icons_size=18,
            padding=4,
        ),
        widget.TextBox(
            text="\ue0be",
            font="Inconsolata for powerline",
            fontsize="33",
            padding=0,
            background=colors[7],
            foreground=colors[13],
        ),
        widget.TextBox(
            text="墳 ",
            font="Iosevka Nerd Font",
            fontsize=18,
            background=colors[13],
            foreground=colors[0],
        ),
        widget.Volume(
            background=colors[13],
            foreground=colors[0],
            font="Iosevka Nerd Font",
            fontsize=15,
            mouse_callbacks={"Button3": lambda: qtile.cmd_spawn("kitty -e pulsemixer")},
        ),
        # This one works with Spotify, enable if you want!
        # widget.Mpris2(
        #    background=colors[13],
        #    foreground=colors[0],
        #    name="spotify",
        #    objname="org.mpris.MediaPlayer2.spotify",
        #    fmt="\u2572   {}",
        #    display_metadata=["xesam:title", "xesam:artist"],
        #    scroll_chars=20,
        #    font="Iosevka Nerd Font",
        #    fontsize=15,
        # ),
        widget.TextBox(
            text="\ue0be",
            font="Inconsolata for powerline",
            fontsize="33",
            padding=0,
            background=colors[13],
            foreground=colors[14],
        ),
        widget.KeyboardLayout(
            fmt=" {} הּ ",
            font="Iosevka Nerd Font",
            configured_keyboards=["us", "in"],
            fontsize="14",
            padding=0,
            background=colors[14],
            foreground=colors[0],
        ),
        widget.TextBox(
            text="\ue0be",
            font="Inconsolata for powerline",
            fontsize="33",
            padding=0,
            background=colors[14],
            foreground=colors[15],
        ),
        widget.TextBox(
            text="   ",
            font="Iosevka Nerd Font",
            fontsize="14",
            padding=0,
            background=colors[15],
            foreground=colors[0],
        ),
        widget.Clock(
            font="Iosevka Nerd Font",
            foreground=colors[0],
            background=colors[15],
            fontsize=15,
            format="%d %b, %A",
        ),
        widget.Sep(
            padding=6,
            linewidth=0,
            background=colors[15],
        ),
        widget.TextBox(
            text="\ue0be",
            font="Inconsolata for powerline",
            fontsize="33",
            padding=0,
            background=colors[15],
            foreground=colors[16],
        ),
        widget.TextBox(
            text=" ",
            font="Iosevka Nerd Font",
            fontsize="18",
            padding=0,
            background=colors[16],
            foreground=colors[0],
        ),
        widget.Clock(
            font="Iosevka Nerd Font",
            foreground=colors[0],
            background=colors[16],
            fontsize=15,
            format="%I:%M %p",
        ),
        widget.TextBox(
            text="\ue0be",
            font="Inconsolata for powerline",
            fontsize="33",
            padding=0,
            background=colors[16],
            foreground=colors[6],
        ),
        widget.Sep(
            padding=6,
            linewidth=0,
            background=colors[6],
        ),
    ]


screens = [
    Screen(
        top=bar.Bar(
            top_bar(),
            size=28,
            opacity=0.95,
            background=colors[0],
            margin=[8, 8, 0, 8],
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
