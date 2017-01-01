  var i =0 ;
  var testimonial_comment =[];
  var testimonial_name =[];
  {% for testimonial in testimonials %}
  testimonial_comment.push("{{testimonial.comment}}");
  testimonial_name.push("{{testimonial.name}}");

  {% endfor %}

function change_testimonial(){ 
   if (i == 0){
      $('p#testimonial').animate({'opacity':0}, 400, function(){
        $(this).html(testimonial_comment[1]).animate({'opacity':1},400);
      });
      $('p#testimonial_name').animate({'opacity':0}, 400, function(){
        $(this).html(testimonial_name[1]).animate({'opacity':1},400);
      });
      i++;
   } else    if (i == 1){
      $('p#testimonial').animate({'opacity':0}, 400, function(){
        $(this).html(testimonial_comment[0]).animate({'opacity':1},400);
      });
      $('p#testimonial_name').animate({'opacity':0}, 400, function(){
        $(this).html(testimonial_name[0]).animate({'opacity':1},400);
      });
      i = 0;
   }
                   };
window.setInterval(change_testimonial,4000);
  
