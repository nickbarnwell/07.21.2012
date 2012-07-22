from mongoengine import *
import common as c

class Event(Document):

	meta = {
		'allow_inheritance': False,
		'indexes' : ['user_id', 'loc'] #should automatically create a 2d geospatial index
	}

	user_id = StringField(required = True) #maybe replace _id later
	loc = GeoPointField(required = True) #[lat, lon]
	ts = IntField(required = True) #timestamp

	@staticmethod
	def add(user_id, lat, lon, timestamp):
		event = Event(user_id = user_id, loc = [lat, lon], ts = timestamp)
		print event.loc
		event.save()

	@staticmethod
	def get_group(user_id):
		event = Event.objects(user_id = user_id)
		print event
		print event.loc
		if event:
			nearby = Event.objects( 
				__raw__ = { 'loc' : { '$near' : event.loc },
							'ts' : { '$gt' : event.ts - c.TIME_DIFF_THRESHOLD },
							'ts' : { '$lt' : event.ts + c.TIME_DIFF_THRESHOLD }
						} 
			).limit(c.MAX_GROUP_SIZE)
			return [e.user_id for e in nearby]
			#maybe cluster / remove outliers here later
