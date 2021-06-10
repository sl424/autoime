# autoime
This script uses the [i3ipc-python library](https://github.com/altdesktop/i3ipc-python)
switch input ime

fork of https://github.com/nwg-piotr/autotiling.git

```text
### Autostart
  exec autoime
```

## Installation

1. Install autoime. Possible methods:

   * _Manually_

     1. Install the `python-i3ipc>=2.0.1` package (or whatever it's called in your Linux
        distribution).
     2. Save the `main.py` file anywhere, make executable and autostart in your
        i3/sway config file: `exec /path/to/the/script/main.py` on sway or
        `exec_always --no-startup-id /path/to/the/script/main.py` on i3. You can give the `main.py` file another name.

   _NOTE:_ The current release and master branch is compatible with sway >= 1.5. 

2. Add `exec autoime` to the `~/.config/sway/config` or `exec_always --no-startup-id
   autoime` to the `~/.config/i3/config` file.

## Usage

```text
$ autoime -h
usage: autoime [-h] [-d] [-v]

optional arguments:
  -h, --help            show this help message and exit
  -d, --debug           Print debug messages to stderr
  -v, --version         display version information
```
