var Card = {
	build: function(user){
    console.log(user)
		var card = $(".card-reference").clone().removeClass("card-reference");
		card.find(".profile-photo").attr("src","http://graph.facebook.com/"+user.uid+"/picture?type=square");
		card.find(".name").text(user.first_name);
		card.find(".lastname").text(user.last_name);
		return card;
	}
}