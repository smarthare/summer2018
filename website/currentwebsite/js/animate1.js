$(document).ready(function(){
  var animPrefix = 'animated ';
  var anim1 = 'zoomInUp';
  var anim2 = 'fadeInUp';
  var anim3 = 'bounce';
  var anim4 = 'shake';
  var anim5 = 'swing';
  var anim6 = 'bounceInRight';
  var anim7 = 'flipInX';
  var anim8 = 'slideInUp';
  var animateEnd = 'animationend oAnimationEnd MSAnimationEnd mozAnimationEnd webkitAnimationEnd';
  var $tex1 = $(".navbar-inverse .navbar-nav>li>a");
  $tex1.toggleClass('scrolled');
  $('.navbar .navbar-logo img').attr('src','img/SCALE Labs.png');
  $('.navbar').addClass(animPrefix+anim5).one(animateEnd,function(){
                
          });
});