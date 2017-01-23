$(document).ready(function(event){
	url = $('#sidebar1').attr('data-url');
	$('iframe[name="map"]').attr('src',url);

});

$('.sidebar').click(function(){
	url = $(this).attr('data-url');
	$('iframe[name="map"]').attr('src',url);
	$('.sidebar').removeClass('active');
	$(this).addClass('active');

});