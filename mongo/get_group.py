import sys
import common as c
import json
import math
from Event import Event

def main(uid):
	return Event.get_group(uid)

if __name__ == '__main__':
	if len(sys.argv) == 2:
		c.connect_db()
		main(sys.argv[1])
	else:
		print 'Usage: python get_group.py <uid>'
