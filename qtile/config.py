import subprocess

from bar import bar
from color import rose_pine_moon
from libqtile import hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.layout.columns import Columns
from libqtile.layout.floating import Floating
from libqtile.layout.stack import Stack
from libqtile.layout.verticaltile import VerticalTile
from libqtile.layout.xmonad import MonadTall
from libqtile.lazy import lazy

# Keybindings
mod = "mod4"
terminal = "kitty"
browser = "google-chrome-stable"
files = "Thunar"
editor = "geany"

keys = [
    # Basic Applications
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod, "shift"], "f", lazy.spawn(files), desc="Launch Thunar"),
    Key([mod, "shift"], "w", lazy.spawn(browser), desc="Launch Thunar"),
    Key([mod, "shift"], "e", lazy.spawn(editor), desc="Launch Thunar"),
    Key(
        [mod],
        "d",
        lazy.spawn("rofi -theme ~/.config/rofi/themes/launcher.rasi -show drun"),
        desc="Launch Rofi",
    ),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    # Qtile Control
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "shift"], "r", lazy.reload_config(), desc="Reload the config"),
    Key(
        [mod],
        "x",
        lazy.spawn("/home/polter/.config/scripts/powermenu"),
        desc="Rofi Power Menu",
    ),
    # Toggle Float and Fullscreen
    Key(
        [mod],
        "f",
        lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen on the focused window",
    ),
    Key(
        [mod],
        "t",
        lazy.window.toggle_floating(),
        desc="Toggle floating on the focused window",
    ),
    # Resizing windows in MonadTall
    Key([mod], "i", lazy.layout.grow()),
    Key([mod], "m", lazy.layout.shrink()),
    Key([mod], "n", lazy.layout.normalize()),
    Key([mod], "o", lazy.layout.maximize()),
    Key([mod, "control"], "space", lazy.layout.flip()),
    # Switch Windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Moving windows in Columns and Stacks
    Key(
        [mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"
    ),
    Key(
        [mod, "shift"],
        "l",
        lazy.layout.shuffle_right(),
        desc="Move window to the right",
    ),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow Windows
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key(
        [mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"
    ),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
]

# Groups
groups = [
    Group(
        "1",
        label="一",
        matches=[
            Match(wm_class="firefox"),
            Match(wm_class="Brave-browser"),
            Match(wm_class="Google-chrome"),
        ],
        layout="stack",
    ),
    Group(
        "2",
        label="二",
        matches=[
            Match(wm_class="Thunar"),
        ],
        layout="monadtall",
    ),
    Group(
        "3",
        label="三",
        matches=[
            Match(wm_class="processing-app-Base"),
            Match(wm_class="Geany"),
        ],
        layout="monadtall",
    ),
    Group("4", label="四", layout="stack"),
    Group(
        "5",
        label="五",
        matches=[
            Match(wm_class="obsidian"),
        ],
        layout="stack",
    ),
    Group("6", label="六", matches=[Match(wm_class="thunderbird")], layout="monadtall"),
    Group("7", label="七", layout="monadtall"),
    Group("8", label="八", layout="monadtall"),
    Group(
        "9",
        label="九",
        matches=[
            Match(wm_class="Spotify"),
        ],
        layout="stack",
    ),
    Group(
        "0",
        label="十",
        matches=[
            Match(wm_class="discord"),
            Match(wm_class="TelegramDesktop"),
        ],
        layout="stack",
    ),
]

for i in groups:
    keys.extend(
        [
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Move focused window to group {}".format(i.name),
            ),
        ]
    )

# Layouts
layouts = [
    MonadTall(
        border_normal=rose_pine_moon["Subtle"],
        border_focus=rose_pine_moon["Text"],
        margin=10,
        border_width=2,
        single_border_width=2,
        single_margin=10,
        ratio=0.5,
    ),
    Columns(
        border_normal=rose_pine_moon["Subtle"],
        border_focus=rose_pine_moon["Text"],
        border_width=2,
        border_normal_stack=rose_pine_moon["Subtle"],
        border_focus_stack=rose_pine_moon["Text"],
        border_on_single=2,
        margin=8,
        margin_on_single=10,
        num_columns=3,
    ),
    VerticalTile(
        border_normal=rose_pine_moon["Subtle"],
        border_focus=rose_pine_moon["Text"],
        border_width=2,
        border_on_single=2,
        margin=8,
        margin_on_single=10,
    ),
    Stack(
        border_normal=rose_pine_moon["Subtle"],
        border_focus=rose_pine_moon["Text"],
        border_width=2,
        num_stacks=1,
        margin=10,
    ),
]

# Bar
widget_defaults = dict(
    font="JetBrainsMono Nerd Font Bold",
    fontsize=14,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(top=bar),
]

# Mouse Drag
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

# Floating layouts
floating_layout = Floating(
    border_normal=rose_pine_moon["Subtle"],
    border_focus=rose_pine_moon["Text"],
    border_width=2,
    float_rules=[
        *Floating.default_float_rules,
        Match(wm_class="blueman-manager"),
        Match(wm_class="xarchiver"),
    ],
)

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wl_input_rules = None
wmname = "LG3D"


@hook.subscribe.startup_once
def autostart_once():
    subprocess.run("/home/polter/.config/qtile/autostart.sh")  # autostart
