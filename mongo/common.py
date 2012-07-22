from collections import defaultdict
import json
import math
import time
from mongoengine import connect
import os

DATA_FILE = 'events.dat'
TIME_DIFF_THRESHOLD = 10 #seconds utc
RADIUS_THRESHOLD = 0.05 #1/100 # degrees (approx 1km)
MAX_GROUP_SIZE = 100

def connect_db():
	port = 'localhost:27017'
	env = os.getenv('RACK_ENV')
	if env == 'production':
		port = os.getenv('MONGOLAB_URI')
	connect('handsin', host = port, auto_start_request = False)
