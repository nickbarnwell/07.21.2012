var Card = {
	build: function(user){
		var card = $(".card-reference").clone().removeClass("card-reference");
		card.find(".profile-photo").attr("src","http://graph.facebook.com/"+user.uid+"/picture?type=square");
		card.find(".name").text(user.first_name);
		card.find(".lastname").text(user.last_name);
		$.each(user.share_fields, function(i,share_field){
			field = card.find(".field-reference").clone().removeClass("field_reference");
			field.find(".field-icon").attr("src", $("#asset-path").val()+share_field.field_type+".png");
			var url = "";
			if(share_field.field_type.substr(0,4)=="mail"){
				url = "mailto:"+share_field.value;
			} else if(share_field.field_type.substr(0,3)=="tel"){
				url = "tel:"+share_field.value;
			}	else if(share_field.field_type == "twitter"){
				url = "http://www.twitter.com/"+share_field.value;
			} else if(share_field.field_type == "facebook"){
				url = user.raw['link'];
			} 
			field.find("a").attr("src",url).text(url);
			card.find(".fields").append(field);
		});
		return card;
	}
}