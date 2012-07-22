var Presser = {
	o: null,
	live: false,
	finishCallback: null,
	transEvents: 'webkitTransitionEnd oTransitionEnd transitionEnd transitionend',
	finished: function(){
		Presser.unbindTrans();
		Presser.finishCallback();	
	},
	retreated: function(){
		Presser.unbindTrans();
	},
	bindTrans: function(complete){
		Presser.o.bind(Presser.transEvents, complete);
		return Presser;
	},
	unbindTrans: function(){
		Presser.o.unbind(Presser.transEvents);
		return Presser;
	},
	init: function(pressStart, pressFinish){
		Presser.startCallback = pressStart;
		Presser.finishCallback = pressFinish;
		Presser.o = $('.presser');
		Presser.o.bind('mousedown touchstart', function(e){
			e.preventDefault();
			Presser.startCallback();
			Presser.live = true;
			Presser.o.addClass("active");
			Presser.unbindTrans().bindTrans(Presser.finished);
		}).attr('unselectable', 'on');
		$(document).bind('mouseup touchend', function(e){
			if(Presser.live){
				Presser.live = false;
				Presser.o.removeClass("active");
				Presser.unbindTrans().bindTrans(Presser.retreated);
			}
		});
	}
}