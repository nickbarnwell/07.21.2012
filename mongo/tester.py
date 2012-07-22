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
		''' Checks that all events were saved in the db
			except for the duplicate. '''
		self.assertEqual(MainTest.count_events(), len(test_events) - 1)

	def test_group_cluster(self):
		''' Checks that the grouping and clustering works '''
		group = get_group.main(e1['uid'])
		#two of them are out of range for grouping
		self.assertEqual(len(group), len(test_events) - 3)

if __name__ == '__main__':
	unittest.main()