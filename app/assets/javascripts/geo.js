var Geo = {
	getLocation: function(success, error){
		navigator.geolocation.getCurrentPosition(success, error, 
			{enableHighAccuracy: true, timeout: 10000, maximumAge: 6*(10^4)});
		return;
	},
	extract: function(location){
	  return {
	    timestamp: location.timestamp,
	    lat: location.coords.latitude,
	    lon: location.coords.longitude,
	    acc: location.coords.accuracy
	  }	
	}
}