# autoime
This script uses the [i3ipc-python library](https://github.com/altdesktop/i3ipc-python)
to switch on/off input method based on the swaywm keyboard layout event. This makes it easier
to switch between [IMEs](https://github.com/swaywm/sway/wiki/Useful-add-ons-for-sway#input-method-editors)
using the `text-input-v3` protocol. Unfortunately, Qt apps are [not supported](https://wiki.qt.io/QtCS2021_-_Wayland_text-input-unstable-v4_protocol)
until `text-input-v4` wayland protocol is adopted.

fork of https://github.com/nwg-piotr/autotiling.git



## Installation

1. Install autoime. Possible methods:

   * _Manually_

     1. Install the `python-i3ipc>=2.0.1` package (or whatever it's called in your Linux
        distribution).
     2. make install

   _NOTE:_ The current release and master branch is compatible with sway >= 1.5. 

2. Add `exec autoime` to the `~/.config/sway/config` or `exec_always --no-startup-id
   autoime` to the `~/.config/i3/config` file.
   ```text
   ### Autostart
   exec autoime
   ```

## Usage

```text
$ autoime -h
usage: autoime [-h] [-d] [-c CONFIG] [-v]

optional arguments:
  -h, --help            show this help message and exit
  -d, --debug           Print debug messages to stderr
  -c CONFIG, --config CONFIG
                        load the ime config file.
  -v, --version         display version information
```

## Config 

Set the keyboard layout and toggle key in sway config:
Sway config path: `~/.config/sway/config`.

```text
input type:keyboard {
    xkb_layout us,jp
    xkb_options grp:alt_shift_toggle
}
```

Toggle IME on/off for the specified language.
Defaut config path: `~/.config/autoime/config`.
Example:
```text
[Japanese]
enable = sh -c 'test -z $(pgrep wlanthy) && wlanthy'
disable = sh -c 'test $(pgrep wlanthy) && killall wlanthy'
```
