"""
use the python-i3ipc to switch the language input engine

fork of https://github.com/nwg-piotr/autotiling.git but for switching input ime.

Dependencies: python-i3ipc>=2.0.1 (i3ipc-python)
"""
import shlex
import configparser
import argparse
import os
import sys
import subprocess
from functools import partial

from i3ipc import Connection, Event


# global LANG
LANG=[]

try:
	from .__about__ import __version__
except ImportError:
	__version__ = "unknown"

def switch_ime(i3, e, debug, ime):
	try:
		replies = i3.get_inputs()
		for reply in replies:
			if reply.xkb_layout_names and len(reply.xkb_layout_names) > 1:
				active = reply.xkb_active_layout_name
				if debug:
					print(active)
				for lang in LANG:
					if lang == active:
						subprocess.Popen(shlex.split(ime[lang]["enable"]))
					else:
						subprocess.Popen(shlex.split(ime[lang]["disable"]))
	except Exception as e:
		print("Error: {}".format(e), file=sys.stderr)

def parse_config(config_path, debug):
	path = os.path.expanduser(config_path)
	if os.path.isfile(path):
		config = configparser.RawConfigParser()
		config.read(path)

		if not hasattr(parse_config, 'ime'):
			parse_config.ime = {}

			for lang in config.sections():
				LANG.append(lang)
				parse_config.ime[lang] = dict(config.items(lang))
				#parse_config.ime[lang]["active"] = False
		if debug:
			print(parse_config.ime)
		return parse_config.ime
	else:
		print("no config file found: ", config_path)
		quit()

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("-d",
			"--debug",
			action="store_true",
			help="Print debug messages to stderr")
	parser.add_argument("-c",
			"--config",
			help="load the config file",
			type=str,
			default="~/.config/autoime/config")
	parser.add_argument("-v",
			"--version",
			action="version",
			version="%(prog)s {}, Python {}".format(__version__, sys.version),
			help="display version information", )

	args = parser.parse_args()

	# parse config file
	ime_engines = parse_config(args.config, args.debug)

	handler = partial(switch_ime, debug=args.debug, ime=ime_engines)
	i3 = Connection()
	i3.on(Event.INPUT, handler)
	i3.main()

if __name__ == "__main__":
	# execute only if run as a script
	main()
