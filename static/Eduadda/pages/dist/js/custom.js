/**
 * AdminLTE Demo Menu
 * ------------------
 * You should not use this file in production.
 * This file is for demo purposes only.
 */

/* eslint-disable camelcase */

(function ($) {
  'use strict'

  $('.owl_1').owlCarousel({
    loop:true,
    margin:5, 
  responsiveClass:true,
  autoplayHoverPause:true,
  autoplay:false,
   slideSpeed: 400,
   dots:false,
      paginationSpeed: 400,
   autoplayTimeout:3000,
    responsive:{
        0:{
            items:3,
            nav:true,
        loop:false
        },
        600:{
            items:3,
            nav:true,
			loop:false
        },
        1000:{
            items:6,
            nav:true,
            dots:false,
            loop:false
        }
    }
})

$(document) .ready(function(){
var li =  $(".owl-item li ");
$(".owl-item li").click(function(){
li.removeClass('active');
});
});

$('.owl-item li > a').click(function() {
    $('li').removeClass('clicked');
    $(this).parent().addClass('clicked');
});

/*--------------------------------------------*/


  
  $(document).ready(function(){
  $('ul li a').click(function(){
    $('li a').removeClass("active");
    $(this).addClass("active");
		});
  });



})(jQuery)


function openRightMenus() {
  document.getElementById("rightMenus").style.display = "block";
}

function closeRightMenus() {
  document.getElementById("rightMenus").style.display = "none";
}
	
function openRightMenu() {
  document.getElementById("rightMenu").style.display = "block";
}

function closeRightMenu() {
  document.getElementById("rightMenu").style.display = "none";
}

