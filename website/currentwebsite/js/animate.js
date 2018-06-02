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
    $('.navbar').removeClass('scrolled');
    $('.navbar .navbar-logo img').attr('src','img/SCALE Labs white.png');
    $tex1.toggleClass('scrolled');
    x = document.getElementById('transition-timer-carousel');
    x.style.display = "block";
    $('#transition-timer-carousel').addClass(animPrefix+anim1).one(animateEnd,function() {
        x = $('#transition-timer-carousel .item h1');;
        x.removeClass('yo');
        $('#transition-timer-carousel .item h1').addClass(animPrefix+anim8).one(animateEnd,function(){
          x = $('#transition-timer-carousel .item p');
          x.removeClass('yo');
          $('#transition-timer-carousel .item p').addClass(animPrefix+anim8).one(animateEnd,function(){
            x = $('button');
            x.removeClass('yo');
            x = document.getElementById("std");
            x.style.visibility="visibile";
            $('button').addClass(animPrefix+anim8).one(animateEnd,function(){
              $('button').addClass(animPrefix+anim5).one(animateEnd,function(){});
          });
        });
      });
    });
  });
});