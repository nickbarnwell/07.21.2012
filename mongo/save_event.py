import sys
import common as c
import json
from Event import Event

def main(json_event):
	json_event
	d = json.loads(json_event)
	uid = d['uid']
	lat = d['lat']
	lon = d['lon']
	timestamp = d['timestamp']
	Event.add(uid, lat, lon, timestamp)

if __name__ == '__main__':
	if len(sys.argv) == 2:
		c.connect_db()
		main(sys.argv[1])
	else:
		print 'Usage: python save_event.py <json_event>'