import os
import subprocess

from colors import colors
from screens import screens

from os import environ

from libqtile.config import (
    # KeyChord,
    Key,
    # Screen,
    Group,
    Drag,
    Click,
    ScratchPad,
    DropDown,
    Match,
)

from libqtile.command import lazy
from libqtile import layout, bar, widget, hook
from libqtile.lazy import lazy

# from libqtile import qtile
# from typing import List  # noqa: F401
from custom.bsp import Bsp as CustomBsp
from custom.bsp import Bsp as CustomBspMargins
from custom.zoomy import Zoomy as CustomZoomy

# from custom.stack import Stack as CustomStack
# from custom.windowname import WindowName as CustomWindowName

mod = "mod4"
mod1 = "mod1"
terminal = "alacritty"
browser = "firefox"
fileManager = "thunar"


@hook.subscribe.client_new
def floating_dialogs(window):
    dialog = window.window.get_wm_type() == "tk"
    transient = window.window.get_wm_transient_for()
    if dialog or transient:
        window.floating = True


@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser("~/.config/qtile/autostart.sh")
    subprocess.call([home])



keys = [ 
    Key(
        [mod, "control"],
        "l",
        lazy.spawn("switch l"),
        desc="Switch theme to light",
    ),
    Key(
        [mod, "control"],
        "n",
        lazy.spawn("switch n"),
        desc="Switch theme to dark",
    ),
 
    # Window controls
    # Switch between windows
    # Key([mod], "h", lazy.layout.left()),
    # Key([mod], "l", lazy.layout.right()),
    # Key([mod], "j", lazy.layout.down()),
    # Key([mod], "k", lazy.layout.up()),
    # Key([mod], "space", lazy.layout.next()),

    # Controls for Max layout ("a" and "d") to change focus windows
    Key([mod], "a", lazy.layout.up().when(layout="max")),
    Key([mod], "d", lazy.layout.down().when(layout="max")),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left()),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),

    #### Grow windows. ####
    # MonadTall
    Key([mod], "Up", lazy.layout.grow()),
    Key([mod], "Down", lazy.layout.shrink()),
    # reset position
    Key([mod], "n", lazy.layout.reset()),
    
    # Columns
    # Key([mod, "control"], "h", lazy.layout.grow_left()),
    # Key([mod, "control"], "l", lazy.layout.grow_right()),
    # Key([mod, "control"], "j", lazy.layout.grow_down()),
    # Key([mod, "control"], "k", lazy.layout.grow_up()),
    # # reset position
    # Key([mod, "control"], "n", lazy.layout.normalize()),
    
    Key([mod], "m", lazy.layout.maximize(), desc='toggle window between minimum and maximum sizes'),
    Key([mod, "shift"], "f", lazy.window.toggle_floating(), desc='toggle floating'),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc='toggle fullscreen'),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout()),
    Key([mod], "q", lazy.window.kill()),
    Key([mod, "control"], "r", lazy.reload_config()),
    Key([mod, "control"], "q", lazy.shutdown()),

    # Apps
    Key([mod], "Return", lazy.spawn(terminal)),
    Key([mod], "e", lazy.spawn(fileManager)),
    # Run "rofi-theme-selector" in terminal to select a theme
    Key([mod], "r", lazy.spawn("rofi -show drun -show-icons")),
    Key([mod], "b", lazy.spawn(browser)),
    Key([mod], "g", lazy.spawn("pavucontrol")),

    # Screenshot
    Key(
        [mod, "shift"],
        "s",
        lazy.spawn("flameshot gui"),
        desc="Launches flameshot",
    ),
    Key(
        [],
        "Print",
        lazy.spawn("flameshot screen -n 0 -c"),
        desc="Shot display 0",
    ),
    Key(
        [mod],
        "Print",
        lazy.spawn("flameshot screen -n 1 -c"),
        desc="Shot display 1",
    ),
    # Audio bindings specifically for Logitech G915 media buttons
    Key(
        [],
        "XF86AudioNext",
        lazy.spawn("playerctl next"),
        desc="Play next audio",
    ),
    Key(
        [],
        "XF86AudioPlay",
        lazy.spawn("playerctl play-pause"),
        desc="Toggle play/pause audio",
    ),
    Key(
        [],
        "XF86AudioPrev",
        lazy.spawn("playerctl previous"),
        desc="Play previous audio",
    ),
    Key(
        [],
        "XF86AudioMute",
        lazy.spawn("amixer -q -D pulse sset Master toggle"),
        desc="Mute audio",
    ),
    Key(
        [],
        "XF86AudioRaiseVolume",
        lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +1%"),
        desc="Raise volume",
    ),
    Key(
        [],
        "XF86AudioLowerVolume",
        lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -1%"),
        desc="Lower volume",
    ),
    Key(
        [mod, "shift"],
        "Return",
        lazy.group["scratchpad"].dropdown_toggle("term"),
        desc="Toggle scratchpad",
    ),
]

# Command to find out wm_class of window: xprop | grep WM_CLASS
workspaces = [
    {
        "name": "1",
        "key": "1",
        "label": "",
        "layout": "monadtall",
    },
    {
        "name": "2",
        "key": "2",
        "label": "",
        "layout": "monadtall",
    },
    {
        "name": "3",
        "key": "3",
        "label": "",
        "layout": "monadtall",
        "matches": [
            Match(wm_class="microsoft-edge"),
            Match(wm_class="google-chrome"),
            Match(wm_class="firefox"),
        ],
    },
    {
        "name": "4",
        "key": "4",
        "label": "",
        "layout": "monadtall",
    },
    {
        "name": "5",
        "key": "5",
        "label": "",
        "layout": "monadtall",
    },
    {
        "name": "6",
        "key": "6",
        "label": "",
        "layout": "monadtall",
    },
    {
        "name": "7",
        "key": "7",
        "label": "",
        "layout": "monadtall",
    },
    {
        "name": "8",
        "key": "8",
        "label": "",
        "layout": "monadtall",
    },
    {
        "name": "9",
        "key": "9",
        "label": "",
        "layout": "floating",
    },
]

groups = []
for workspace in workspaces:
    matches = workspace["matches"] if "matches" in workspace else None
    groups.append(
        Group(
            workspace["name"],
            matches=matches,
            layout=workspace["layout"],
            #spawn=workspace["spawn"],
            label=workspace["label"],
        )
    )
    keys.append(
        Key(
            [mod],
            workspace["key"],
            lazy.group[workspace["name"]].toscreen(),
            desc="Focus certain workspace",
        )
    )
    keys.append(
        Key(
            [mod, "shift"],
            workspace["key"],
            lazy.window.togroup(workspace["name"]),
            desc="Move focused window to another workspace",
        )
    )

groups.append(
    ScratchPad(
        "scratchpad",
        [
            DropDown(
                "term",
                "alacritty",                
                x=0.1,
                y=0.1,
                width=0.8,
                height=0.7,
                on_focus_lost_hide=False,
            ),
        ],
    )
)

layout_theme = {
    "border_width": 3,
    "margin": 5,
    "border_focus": "3b4252",
    "border_normal": "3b4252",
    "font": "FiraCode Nerd Font",
    "grow_amount": 4,
}

layout_theme_margins = {
    "name": "bsp-margins",
    "border_width": 3,
    "margin": [150, 300, 150, 300],
    "border_focus": "3b4252",
    "border_normal": "3b4252",
    "font": "FiraCode Nerd Font",
    "grow_amount": 4,
}

layout_audio = {
    "name": "monadwide-audio",
    "border_width": 3,
    "margin": 100,
    "border_focus": "3b4252",
    "border_normal": "3b4252",
    "font": "FiraCode Nerd Font",
    "ratio": 0.65,
    "new_client_position": "after_current",
}

layouts = [
    # layout.Bsp(**layout_theme, fair=False),
    #CustomBsp(**layout_theme, fair=False),
    layout.Max(**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.MonadWide(**layout_theme),
    layout.Floating(
        float_rules=[
            Match(wm_type="utility"),
            Match(wm_type="notification"),
            Match(wm_type="toolbar"),
            Match(wm_type="splash"),
            Match(wm_type="dialog"),
            Match(wm_class="file_progress"),
            Match(wm_class="confirm"),
            Match(wm_class="dialog"),
            Match(wm_class="download"),
            Match(wm_class="error"),
            Match(wm_class="notification"),
            Match(wm_class="splash"),
            Match(wm_class="toolbar"),
            Match(func=lambda c: c.has_fixed_size()),
            Match(func=lambda c: c.has_fixed_ratio()),
            Match(wm_class="xdman-Main"),
            Match(wm_class="nitrogen"),
            Match(wm_class="lxappearance"),
        ],
        **layout_theme,
    ),
    # layout.Columns(
    #    **layout_theme,
    #    border_on_single=True,
    #    num_columns=3,
    #    # border_focus_stack=colors[2],
    #    # border_normal_stack=colors[2],
    #    split=False,
    # ),
    # layout.RatioTile(**layout_theme),
    # layout.VerticalTile(**layout_theme),
    # layout.Matrix(**layout_theme, columns=3),
    # layout.Slice(**layout_theme),
    # layout.Tile(shift_windows=True, **layout_theme),
    # CustomBspMargins(**layout_theme_margins),
]

# Setup bar

widget_defaults = dict(
    font="JetBrainsMono Nerd Font Mono Medium",
    fontsize=25,
    padding=3,
    background=colors[0],
)
extension_defaults = widget_defaults.copy()

# Drag floating layouts.
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

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None  # WARNING: this is deprecated and will be removed soon
follow_mouse_focus = True
bring_front_click = "floating_only"
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "focus"

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
