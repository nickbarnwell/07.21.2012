var Dashboard = {
	loadResults: function(users){
		if(users){
			$.each(users, function(i,user){
				$(".results").append(Card.build(user));
			});
		}
		$(".main").show();
		$(".results").show();
	},
	geoFailed: function(){
		alert("retrieving second geo failed");
	},
	submitGeo: function(location){
		$.post('/bump', Geo.extract(location));
	},
	onPressStart: function(){
		Geo.getLocation(Dashboard.submitGeo, Dashboard.geoFailed)
	},
	onPressFinish: function(){
		$.getJSON('/hump', Dashboard.loadResults);
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