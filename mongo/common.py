from collections import defaultdict
import json
import math
import time

DATA_FILE = 'events.dat'
TIME_DIFF_THRESHOLD = 10 #seconds utc
RADIUS_THRESHOLD = 0.05 #1/100 # degrees (approx 1km)
MAX_GROUP_SIZE = 100
