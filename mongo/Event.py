from mongoengine import *
import common as c
from datetime import datetime
import time
import json
import cluster

class Event(Document):

  meta = {
    'allow_inheritance': False,
    'indexes' : ['user_id', 'loc'] #should automatically create a 2d geospatial index
  }

  user_id = StringField(required = True) #maybe replace _id later
  loc = GeoPointField(required = True) #[lat, lon]
  time = DateTimeField(required = True) #from timestamp
  timestamp = IntField(required = True)

  @staticmethod
  def add(user_id, lat, lon, timestamp):
    existing_event = Event.objects(user_id = user_id).first()
    if existing_event is not None:
      existing_event.delete()
    dt = datetime.fromtimestamp(timestamp)
    event = Event(user_id = user_id, loc = [lat, lon], timestamp = timestamp, time = dt)
    event.save()

  @staticmethod
  def get_group(user_id):
    e = Event.objects(user_id = user_id).first()
    if e:
      nearby = Event.objects( 
        __raw__ = { 'loc' : { '$within' : {"$center" : [e.loc, c.RADIUS_THRESHOLD]} },
              'timestamp' : { '$gt' : e.timestamp - c.TIME_DIFF_THRESHOLD },
              'timestamp' : { '$lt' : e.timestamp + c.TIME_DIFF_THRESHOLD }
            } 
      ).limit(c.MAX_GROUP_SIZE).all()
      group = [ (e.user_id, e.loc) for e in nearby]
      cl = cluster.get_cluster(group)
      return json.dumps([uid for (uid, loc) in cl])
