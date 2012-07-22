var Dashboard = {
	loadResults: function(users){
		console.log(users)
		if(users != [] && users != null){
			$.each(users, function(i,user){
				if(user != null) {
					$(".results").append(Card.build(user).fadeIn(1000));
				}
			});
		}
		$(".main").hide();
		$(".results").fadeIn(500);
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
		$.getJSON('/hump', Dashboard.loadResults)
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
		$('.edit').on('click', function(evt) {
			window.location = '/profile/edit'
		})
		$('#results-back').on('click', function(evt) {
			$('.results').hide();
			$('.main').fadeIn(500);
			$('.results .bump-result').remove();
		})

		$('.save-contacts').live('click', function(evt) {
			evt.preventDefault();
			var link = $(this)
			var uid = $(this).attr('data-id')
			$.post('/share', {user_id: uid}, function(res) {
				link.remove()
				alert('Saved to contacts')
			})
			return false;
		})
	}
}