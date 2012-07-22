import sys
import common as c
import json
import math

def main(uid):
	Event.get_group(uid)

if __name__ == '__main__':
	if len(sys.argv) == 2:
		main(sys.argv[1])
	else:
		print 'Usage: python get_group.py <uid>'