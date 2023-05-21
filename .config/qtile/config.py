from libqtile import qtile
import os
import subprocess
from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, DropDown, Group, Key, Match, ScratchPad, Screen
from libqtile.lazy import lazy
from widgets.expanding_clock import ExpandingClock

MOD = "mod4"
TERMINAL = "kitty"


if qtile.core.name == "x11":
    term = "urxvt"
elif qtile.core.name == "wayland":
    term = "foot"

keys = [
    Key([MOD], "Return", lazy.spawn(TERMINAL)),

    Key([MOD], "h", lazy.layout.left()),
    Key([MOD], "l", lazy.layout.right()),
    Key([MOD], "j", lazy.layout.down()),
    Key([MOD], "k", lazy.layout.up()),
    Key([MOD], "space", lazy.layout.next()),

    Key([MOD, "shift"], "h", lazy.layout.shuffle_left()),
    Key([MOD, "shift"], "l", lazy.layout.shuffle_right()),
    Key([MOD, "shift"], "j", lazy.layout.shuffle_down()),
    Key([MOD, "shift"], "k", lazy.layout.shuffle_up()),

    Key([MOD, "shift"], "Return", lazy.layout.toggle_split()),
    Key([MOD, "shift"], "space", lazy.widget["keyboardlayout"].next_keyboard()),

    Key([MOD, "control"], "h", lazy.layout.grow_left()),
    Key([MOD, "control"], "l", lazy.layout.grow_right()),
    Key([MOD, "control"], "j", lazy.layout.grow_down()),
    Key([MOD, "control"], "k", lazy.layout.grow_up()),
    Key([MOD, "control"], "r", lazy.reload_config()),
    Key([MOD, "control"], "q", lazy.shutdown()),
    Key([MOD, "control"], "x", lazy.spawn('dm-tool lock')),


    Key([MOD], "Tab", lazy.next_layout()),
    Key([MOD], "w", lazy.window.kill()),
    Key([MOD], "r", lazy.spawncmd()),
    Key([MOD], 'm', lazy.window.toggle_minimize()),
    Key([MOD], "n", lazy.layout.normalize()),
]

group_names = [
    ("one"),
    ("two"),
    ("three"),
    ("four"),
    ("five"),
    ("six"),
    ("seven"),
    ("eight"),
    ("nine"),
]
groups = [Group(i) for i in group_names]

groups.extend(
    [
        ScratchPad("scratchpad",
                   [DropDown("term", "kitty", opacity=0.7,
                             height=0.4, width=0.5, x=0.25)]
                   )])

for i, name in enumerate(group_names, 1):
    keys.extend(
        [
            # MOD1 + letter of group = switch to group
            Key([MOD], str(i), lazy.group[name].toscreen()),
            # MOD1 + shift + letter of group = switch to & move focused window to group
            Key([MOD, "shift"], str(i), lazy.window.togroup(
                name, switch_group=False)),
        ]
    )
keys.extend(
    [
        Key([MOD], "t", lazy.group['scratchpad'].dropdown_toggle('term')),
    ]
)


colors = [
    ["#d9d5d5"],  # 0
    ["#D9303E"],  # 1
    ["#A62E38"],  # 2
    ["#732F35"],  # 3
    ["#593434"],  # 4
    ["#262626"]   # 5
]
layout_theme = {
    "border_focus": colors[1],
    "border_width": 3,
    "border_normal": colors[5],
    "margin": 8,
    "fullscreen_border_width": 0,
    "single_border_width": 0,
    "single_margin": 0,
    # "margin_on_single": 10,
}

layouts = [
    layout.Columns(**layout_theme),
    layout.Max(**layout_theme),
]

widget_defaults = {
    "font": 'Fira Mono',
    "fontsize": 14,
    "padding": 3,
    "background": colors[5]
}

extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Sep(
                    linewidth=0,
                    padding=6,
                ),
                widget.Image(
                    margin_x=15,
                    background=colors[5],
                    filename="~/.config/qtile/icons/archicon8.png",
                    scale="False",
                    mouse_callbacks={"Button1": lazy.spawn("rofi -show drun")},
                ),

                widget.Sep(
                    linewidth=0,
                    padding=6,
                ),

                widget.CurrentLayoutIcon(
                    scale=0.8,
                    background=colors[5],
                    foreground=colors[5],
                ),

                widget.CheckUpdates(
                    update_interval=180,
                    distro="Arch_checkupdates",
                    display_format=" {updates} Updates",
                    foreground=colors[1],
                    mouse_callbacks={'Button1': lazy.spawn(
                        TERMINAL + " -e sudo pacman -Syu")},
                ),

                widget.TextBox(
                    text=' |',
                    background=colors[5],
                    foreground='474747',
                    padding=2,
                    fontsize=14
                ),

                widget.GroupBox(
                    active=colors[0],
                    background=colors[5],
                    this_current_screen_border=colors[1],
                    margin_y=3,
                    margin_x=0,
                    padding_x=10,
                    padding_y=5,
                    disable_drag=True,
                    highlight_method="block",
                    hide_unused="True"
                ),

                widget.TextBox(
                    text=' |',
                    background=colors[5],
                    foreground='474747',
                    padding=2,
                    fontsize=14
                ),

                widget.Prompt(
                    background='#1D2330',
                    prompt=' 🧑🏼‍💻  '
                ),

                widget.TaskList(
                    foreground=colors[0],
                    borderwidth=1.5,
                    border=colors[1],
                    margin_y=0,
                    margin_x=15,
                    padding_x=5,
                    padding_y=2,
                    icon_size=0,
                    max_title_width=150,
                ),

                widget.Systray(
                    padding=5,
                ),

                widget.TextBox(
                    text=' |',
                    background=colors[5],
                    foreground='474747',
                    padding=2,
                    fontsize=14
                ),

                widget.Volume(
                    emoji="True",
                    volume_app="pulseaudio-ctl",
                    fmt="Vol: {}",
                    mouse_callbacks={"Button1": lazy.spawn("pavucontrol")},
                    padding=5
                ),


                widget.Memory(
                    measure_mem="G",
                    mouse_callbacks={'Button1': lazy.spawn(
                        TERMINAL + " -e btop")},
                    fmt='Mem: {}',
                    padding=5
                ),

                widget.Net(
                    format='{down} {up}',
                    padding=5
                ),

                widget.ThermalSensor(
                    threshold=90,
                    fmt='Temp: {}',
                    padding=5
                ),

                widget.TextBox(
                    text=' |',
                    background=colors[5],
                    foreground='474747',
                    padding=2,
                    fontsize=14
                ),

                widget.KeyboardLayout(
                    configured_keyboards=["us", "ar"],
                    display_map={'us': ' US🇺🇸 ', 'ar': ' AR🇸🇦 '},
                    padding=5,
                ),

                widget.TextBox(
                    text=' |',
                    background=colors[5],
                    foreground='474747',
                    padding=2,
                    fontsize=14
                ),

                ExpandingClock(
                    format='⏰%I:%M', long_format="⏰ %I:%M | 🗓️%A %d %B %Y",
                ),

                widget.TextBox(
                    text=' |',
                    background=colors[5],
                    foreground='474747',
                    padding=2,
                    fontsize=14
                ),

                widget.Sep(
                    linewidth=0,
                    padding=6,
                    background=colors[1],
                ),

                widget.QuickExit(
                    default_text="󰐥",
                    fontsize=25,
                    countdown_format='[{} sec]',
                    background=colors[1],
                    foreground=colors[0]
                ),

                widget.Sep(
                    linewidth=0,
                    padding=6,
                    background=colors[1],
                ),

                widget.TextBox(
                    fmt="󰜉",
                    fontsize=25,
                    mouse_callbacks={'Button1': lazy.reload_config()},
                    background=colors[1],
                    foreground=colors[0]
                ),

                widget.Sep(
                    linewidth=0,
                    padding=10,
                    background=colors[1],
                ),
            ],
            24,
        ),
    ),
]


@ hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.Popen([home])


# Drag floating layouts.
mouse = [
    Drag([MOD], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([MOD], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([MOD], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
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
