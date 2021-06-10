"""
use the python-i3ipc to switch the language input

fork of https://github.com/nwg-piotr/autotiling.git but for switching input ime.

Dependencies: python-i3ipc>=2.0.1 (i3ipc-python)
"""
import argparse
import os
import sys
import subprocess
from functools import partial

from i3ipc import Connection, Event

try:
	from .__about__ import __version__
except ImportError:
	__version__ = "unknown"

def switch_ime(i3, e, debug):
	try:
		replies = i3.get_inputs()
		for reply in replies:
			if reply.identifier == "1:1:AT_Translated_Set_2_keyboard":
				if debug:
					print(reply.xkb_active_layout_name)
					
				if reply.xkb_active_layout_name == "Japanese":
					rc = subprocess.Popen(["test", "-z", "$(pgrep wlanthy)"]).wait()
					#print(rc)
					if rc == 1:
						subprocess.Popen(["wlanthy"])
				else:
					rc = subprocess.Popen(["test", "$(pgrep wlanthy)"]).wait()
					#print(rc)
					if rc == 0:
						subprocess.Popen(["killall", "wlanthy"])

	except Exception as e:
		print("Error: {}".format(e), file=sys.stderr)


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("-d",
			"--debug",
			action="store_true",
			help="Print debug messages to stderr")
	parser.add_argument("-v",
			"--version",
			action="version",
			version="%(prog)s {}, Python {}".format(__version__, sys.version),
			help="display version information", )

	args = parser.parse_args()

	handler = partial(switch_ime, debug=args.debug)
	i3 = Connection()
	i3.on(Event.INPUT, handler)
	i3.main()

if __name__ == "__main__":
	# execute only if run as a script
	main()
