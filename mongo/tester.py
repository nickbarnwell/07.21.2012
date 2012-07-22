import json
import urllib
import save_event
import subprocess as sub
import common as c
import unittest
import time
import get_group
import save_event
from mongoengine import connect

#test data
t1 = int(time.time())
lat1 = 37.7991206718683
lon1 = -122.35498517668354

#duplicate, should just get overwritten by first
e1_dup = { "timestamp" : t1,
		"lat" : lat1,
		"lon" : lon1,
		"uid" : '1111'
	}
e1 = { "timestamp" : t1,
		"lat" : lat1,
		"lon" : lon1,
		"uid" : '1111'
	}
e2 = { "timestamp" : t1 - c.TIME_DIFF_THRESHOLD / 2,
		"lat" : lat1 - c.GEO_DIFF_THRESHOLD / 400,
		"lon" : lon1 - c.GEO_DIFF_THRESHOLD / 4,
		"uid" : '2222'
	}
e3 = { "timestamp" : t1 - c.TIME_DIFF_THRESHOLD / 4,
		"lat" : lat1 + c.GEO_DIFF_THRESHOLD / 400,
		"lon" : lon1 - c.GEO_DIFF_THRESHOLD / 400,
		"uid" : '3333'
	}
e4 = { "timestamp" : t1 + c.TIME_DIFF_THRESHOLD / 4,
		"lat" : lat1 + c.GEO_DIFF_THRESHOLD / 400,
		"lon" : lon1 - c.GEO_DIFF_THRESHOLD / 400,
		"uid" : '4444'
	}
#geo outlier, but in range
e5 = { "timestamp" : t1 + c.TIME_DIFF_THRESHOLD / 2,
		"lat" : lat1 + c.GEO_DIFF_THRESHOLD / 4,
		"lon" : lon1 + c.GEO_DIFF_THRESHOLD / 4,
		"uid" : '5555'
	}
#too late
e6 = { "timestamp" : t1 + c.TIME_DIFF_THRESHOLD * 2,
		"lat" : lat1 + c.GEO_DIFF_THRESHOLD / 4,
		"lon" : lon1 + c.GEO_DIFF_THRESHOLD / 4,
		"uid" : '6666'
	}
#out of geo range (using circular radius)
e7 = { "timestamp" : t1 + c.TIME_DIFF_THRESHOLD / 2,
		"lat" : lat1 + c.GEO_DIFF_THRESHOLD,
		"lon" : lon1 + c.GEO_DIFF_THRESHOLD,
		"uid" : '7777'
	}

test_events = [e1_dup, e1, e2, e3, e4, e5, e6, e7]

class MainTest(unittest.TestCase):

	def setUp(self):
		connect('handsin', host='localhost:27017', auto_start_request = False)
		for e in test_events:
			save_event.main(json.dumps(e))
	
	@staticmethod
	def count_events(): return Event.objects.count()

	def test_add(self):
		''' Checks that all events were saved in the file
			except for the duplicate. '''
		self.assertEqual(MainTest.count_events(), len(test_events) - 1)

	def test_group_cluster(self):
		''' Checks that the grouping and clustering works '''
		group, cluster = get_group.main(e1['uid'])
		#two of them are out of range for grouping
		self.assertEqual(len(group), len(test_events) - 3)
		#one more of them is out of range for clustering
		self.assertEqual(len(cluster), len(test_events) - 4)

	def test_timeout(self):
		''' Checks that events are deleted from the file after
			the timeout time '''
		old_timeout = c.DELETE_USER_TIMEOUT

		c.DELETE_USER_TIMEOUT = 3
		timestamps = [e['timestamp'] for e in test_events]
		latest = max(timestamps)
		while time.time() - latest < c.DELETE_USER_TIMEOUT:
			pass
		self.assertEqual(MainTest.count_events(), 0)

		c.DELETE_USER_TIMEOUT = old_timeout

if __name__ == '__main__':
	unittest.main()


'''
#setup
sub.call(['rm', '-rf', c.DATA_FILE])
uids = []


#test adds
for i in range(15):
	js = urllib.urlopen('http://192.168.0.250:3000/test').read()
	print js
	d = json.loads(js)
	uids.append(d['uid'])
	sub.call(['python', 'save_event.py', js])

#sub.call(['cat', c.DATA_FILE])

#test queries
from urlparse import urlparse, parse_qs

for uid in uids:
	url = 'http://192.168.0.250/?uid=' + str(uid)
	query = parse_qs(urlparse(url).query)
	uid = query['uid'][0]
'''