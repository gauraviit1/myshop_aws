$(document).ready(function(){
  $("#products").LoadingOverlay("hide");
    $('.child_options a').on('click', function() {
    var url = $(this).attr('href');
    $.ajax({
        url: url,
        beforeSend: function(xhr){
          $("#products").LoadingOverlay("show");
        }
      }).done(function(html) {
        $("#products").LoadingOverlay("hide");
        $('#products').html('&nbsp;').load(url);
      });
    });
});
