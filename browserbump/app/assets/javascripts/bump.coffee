$(document).ready -> 
  window.addEventListener("devicemotion", onDeviceMotion, false)

onDeviceMotion = (event) ->
  accel = event.accelerationIncludingGravity
  console.log(accel)