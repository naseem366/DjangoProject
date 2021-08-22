$(document).ready(function(){$('.theme-loader').animate({'opacity':'0',},1200);setTimeout(function(){$('.theme-loader').remove();},2000);});

$(document).ready(function(){
	$('#mobile-collapse').click(function(){
      $('.pcoded.iscollapsed').toggleClass('expanded');
      $('.pcoded.iscollapsed').toggleClass('offcanvas');
    });
    $(".mobile-options").on("click",function(){
      $(".navbar-container .nav-right").slideToggle("slow")
    });
    $('.pcoded-submenu li a').on('click', function(){
      $('html, body').animate({
        scrollTop: 0
      }, 500);
    });
    if($(window).width() <= 767){
      $('.pcoded-submenu li a').on('click', function(){
        $('.pcoded.iscollapsed').toggleClass('expanded');
        $('.pcoded.iscollapsed').toggleClass('offcanvas');
      });
    }

    $('.lng-dropdown li a').click(function(){
      var aaa = this.innerHTML;
      $('.lng-dropdown #dropdown-active-item').html(aaa);
    });  

    $("#more-details").on("click",function(){
      $(".more-details").slideToggle(500);
    });
    
    $(".pcoded-hasmenu > a").on("click",function(e){
      if($(this).parent('.pcoded-hasmenu').hasClass('pcoded-trigger')){
        $(".pcoded-hasmenu").removeClass('pcoded-trigger active');
        $('.pcoded-hasmenu ul.pcoded-submenu').hide();
      }else{
        $(".pcoded-hasmenu").removeClass('pcoded-trigger');
        $('.pcoded-hasmenu ul.pcoded-submenu').hide();
        $(this).parent('.pcoded-hasmenu').addClass('pcoded-trigger active');
        $(this).parent('.pcoded-hasmenu').children('ul.pcoded-submenu').slideDown();
      }
    });
});