var Card = {
	build: function(user){
		var card = $(".card-reference").clone().removeClass("card-reference").addClass('bump-result');
    var fields = $(card).find('.fields')[0];
    console.log(fields)

		card.find(".profile-photo").attr("src","http://graph.facebook.com/"+user.uid+"/picture?type=square");
		card.find(".name").text(user.first_name);
		card.find(".lastname").text(user.last_name);
    html = '<a class="save-contacts" href="/share" data-id="' + user.id +  '">Save to Contacts</a>';
    console.log(html)
    $(card).find('.bottom').append(html);
    $.each(user.share_fields, function(i, item) {
      (Field.create(item.id, fields))
    })
    
		return card;
	}
  
}

var Field = {
  create: function(id, fields) {
    $.get('/field/'+id, function(data) {
      $(fields).append(data);
    })
  }
}