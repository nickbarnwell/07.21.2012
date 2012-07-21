$(document).ready -> 
    
  get_location()
  return

get_location = ->
  navigator.geolocation.getCurrentPosition(geo_success_handler, geo_error_handler, 
    {enableHighAccuracy: true, timeout: 3000, maxiumAge: 6*(10^5)});
  return

show_map = (position) ->
  latitude = position.coords.latitude;
  longitude = position.coords.longitude;
  console.log(latitude, longitude)
  return

geo_error_handler = (error) ->
  console.log(error)
  return

geo_success_handler = (location) -> 
  dict = {
    timestamp: location.timestamp,
    lat: location.coords.latitude,
    lon: location.coords.longitude,
    acc: location.coords.accuracy, #acc in meters
    uid: 1
  }
  console.log(dict)
  return
