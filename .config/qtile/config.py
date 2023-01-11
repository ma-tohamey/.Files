# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
import sys
import os
import subprocess
from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

#from widgets.nx_prayer import test_prayer
from widgets.expanding_clock import ExpandingClock
from widgets.nx_prayer import Prayer

mod = "mod4"
alt = "mod1"
terminal = "kitty"

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key(
        [mod], "h",
        lazy.layout.left(),
        desc="Move focus to left"
        ),

    Key(
        [mod], "l",
        lazy.layout.right(),
        desc="Move focus to right"
        ),
    
    Key(
        [mod], "j",
        lazy.layout.down(),
        desc="Move focus down"
        ),
    
    Key(
        [mod], "k",
        lazy.layout.up(),
        desc="Move focus up"
        ),

    #Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),

    Key(
        [mod], 'f',
        lazy.window.toggle_floating(),
        desc = 'Put the focused window to/from floating mode',
    ),

    Key(
        [mod], 'm',
        lazy.window.toggle_minimize(),
        desc = 'Put the focused window to/from minimize mode',
    ),

    Key(
        [mod], "n",
        lazy.layout.normalize(),
        desc="Reset all window sizes"
        ),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    
    Key(
        [mod, "shift"], "h",
        lazy.layout.shuffle_left(),
        desc="Move window to the left"
        ),

    Key(
        [mod, "shift"], "l",
        lazy.layout.shuffle_right(),
        desc="Move window to the right"
        ),

    Key(
        [mod, "shift"], "j",
        lazy.layout.shuffle_down(),
        desc="Move window down"
        ),

    Key(
        [mod, "shift"], "k",
        lazy.layout.shuffle_up(),
        desc="Move window up"
        ),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    
    Key(
        [mod, "control"], "h",
        lazy.layout.grow_left(),
        desc="Grow window to the left"
        ),

    Key(
        [mod, "control"], "l",
        lazy.layout.grow_right(),
        desc="Grow window to the right"
        ),

    Key(
        [mod, "control"], "j",
        lazy.layout.grow_down(),
        desc="Grow window down"
        ),

    Key(
        [mod, "control"], "k",
        lazy.layout.grow_up(),
        desc="Grow window up"
        ),

    
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"], "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),

    Key(
        [mod], "Return",
        lazy.spawn(terminal),
        desc="Launch terminal"
        ),
    
    # Toggle between different layouts as defined below
    
    Key(
        [mod], "Tab",
        lazy.next_layout(),
        desc="Toggle between layouts"
        ),

    Key(
        [mod], "w",
        lazy.window.kill(),
        desc="Kill focused window"
        ),

    Key(
        [mod, "control"], "r",
        lazy.reload_config(),
        desc="Reload the config"
        ),

    Key(
        [mod, "control"], "q",
        lazy.shutdown(),
        desc="Shutdown Qtile"
        ),

    Key(
        [mod], "r",
        lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"
        ),

    Key(
        [mod], "space",
        lazy.widget["keyboardlayout"].next_keyboard(),
        desc="Next keyboard layout.",
    ),
    
    # lcoking the screen with dm-tool 
    Key(
        [mod, "control"], "x",
        lazy.spawn('dm-tool lock'),
        desc="Locking the screen with dm-tool",
        ),
    
]


#lazy.screen.set_wallpaper("~/wallpapers/nord_background.png", mode = "fill")

group_names = [ ("one"),
                ("two"),
                ("three"),
                ("four"),
                ("five"),
                ("six"),
                ("seven"),
                ("eight"),
                ("nine")
              ]
groups = [Group(name) for name in group_names]

for i, name in enumerate (group_names, 1):
    keys.extend(
        [
            # mod1 + the index number of the group = switch to group
            Key(
                [mod],
                str(i),
                lazy.group[name].toscreen(),  
                desc="Switch to group {}",
            ),
            # mod1 + shift + the index number of the group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                str(i),
                lazy.window.togroup(name),
                desc="Switch to & move focused window to group {}",
                ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )




layout_theme = {
        "border_focus": "#5e81ac",
        #"border_focus_stack":"#04ff00",
        "border_width": 3,
        "border_normal": "#2E3440",
        "margin": 8,
        #"margin_on_single": 10,
        }


colors = [
        ["#81A1C1", "#5E81AC"],
        ["#434c5e", "#4c566a"],  
        ["#282c34", "#282c34"],
        ["#1c1f24", "#1c1f24"],
        ["#5e81ac"],
        ["#81a1c1"],
        ["#2e3440"]
]


layouts = [
    layout.Columns(**layout_theme),
    layout.Max(**layout_theme),
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


widget_defaults = dict(
    font = "Hack Nerd Font",
    fontsize = 14,
    padding = 2,
    background = colors[6]
)

extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top = bar.Bar(
            [

                widget.Spacer(
                    length = 8,
                    ),

                widget.Image(
                    margin_x = 15,
                    background = "FFFFFF",
                    filename = "~/.config/qtile/icons/archicon2.png",
                    scale = "False",
                    mouse_callbacks = {"Button1": lazy.spawn("rofi -show drun")},
                    ),
                
                widget.Spacer(
                    length = 8
                    ),

                widget.CurrentLayoutIcon(
                    scale = 1
                    ),

                widget.TextBox(
                       text = ' |',
                       background = colors[6],
                       foreground = '474747',
                       padding = 2,
                       fontsize = 14
                       ),

                widget.GroupBox(
                    margin_y = 3,
                    margin_x = 0,
                    padding_x = 10,
                    padding_y = 5,
                    border_width = 3,
                    disable_drag = True,
                    highlight_method = "block",
                    foreground = colors[2],
                    hide_unused = "True"
                    ),

                widget.TextBox(
                       text = '| ',
                       background = colors[6],
                       foreground = '474747',
                       padding = 2,
                       fontsize = 14
                       ),

                widget.Prompt(
                    background = '#1D2330',
                    prompt = ' 🧑🏼‍💻  '
                ),

                widget.TaskList(
                    margin_y = 0,
                    margin_x = 15,
                    padding_x = 5,
                    padding_y = 3,
                    border_width = 3,
                    icon_size = 0,
                    max_title_width = 150,
                ),
                
                widget.Systray(
                    padding = 5,
                        ),
                
                widget.TextBox(
                       text = ' |',
                       background = colors[6],
                       foreground = '474747',
                       padding = 2,
                       fontsize = 14
                       ),

                widget.Volume(
                        emoji = "True",
                        volume_app = "pulseaudio-ctl",
                        fmt = "Vol: {}",
                        mouse_callbacks = {"Button1": lazy.spawn("pavucontrol")},
                        padding = 5
                        ),

        
                widget.Memory(
                    measure_mem = "G",
                    mouse_callbacks = {'Button1': lazy.spawn(terminal + " -e btop")},
                    fmt = 'Mem: {}',
                    padding = 5
                ),

                widget.Net(
                    format = '{down} {up}',
                    padding = 5
                ),

                widget.ThermalSensor(
                       threshold = 90,
                       fmt = 'Temp: {}',
                       padding = 5
                       ),
                
                widget.TextBox(
                       text = '|',
                       background = colors[6],
                       foreground = '474747',
                       padding = 2,
                       fontsize = 14
                       ),

                Prayer(interval=60),

                widget.KeyboardLayout(
                    configured_keyboards=["us", "ar"],
                    display_map = {'us': ' US🇺🇸 ', 'ar': ' AR🇸🇦 '},
                    padding = 5,
                    ),
                
                #widget.GenPollText(
                    #func = test_prayer
                    #fmt = "{hell world}"
                    #),

                widget.TextBox(
                       text = '|',
                       background = colors[6],
                       foreground = '474747',
                       padding = 2,
                       fontsize = 14
                       ),

                ExpandingClock(
                    format = '⏰%I:%M',long_format="⏰ %I:%M | 🗓️%A %d %B %Y",
                ),

                widget.Spacer(
                    length = 8
                    ),

                widget.QuickExit(
                    default_text = '  ',
                    countdown_format = '[{} sec]'
                ),

                widget.TextBox(
                    fmt = ' ﰇ ',
                    mouse_callbacks = {'Button1': lazy.reload_config()},
                ),
            ],
            24,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
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


@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])


# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
