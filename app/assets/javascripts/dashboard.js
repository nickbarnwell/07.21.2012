var Dashboard = {
	loadResults: function(){
		
	},
	geoFailed: function(){
		alert("retrieving second geo failed");
	},
	submitGeo: function(location){
		console.log(Geo.extract(location));
		$.post('/asdfasdfasdf.php', Geo.extract(location));
	},
	onPressStart: function(){
		Geo.getLocation(Dashboard.submitGeo, Dashboard.geoFailed)
	},
	onPressFinish: function(){
		$.get('/loading.php', Dashboard.loadResults);
	},
	initWithGeo: function(){
		Dashboard.presser = 
		$(".loading").hide();
		$(".main").show();
		Presser.init(Dashboard.onPressStart, Dashboard.onPressFinish);	
	},
	initNoGeo: function(){
		$(".loading").hide();
		$(".nogeo").show();	
	},
	init: function(){
		Geo.getLocation(Dashboard.initWithGeo, Dashboard.initNoGeo)	
	}
}