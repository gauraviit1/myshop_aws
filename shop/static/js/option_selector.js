$(document).ready(function(){
  $('.child_options a').click(function(){

    $('#products').html('&nbsp;').load($(this).attr('href'));

  });
});
