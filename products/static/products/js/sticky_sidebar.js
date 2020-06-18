
function stickySidebar() {
	var top = 1;
	if ($( window ).width() < 768) {
		top = 60;
	}
	
	if($(this).scrollTop() >= top) {
          $('nav.sidebar').addClass('stickytop');
      }
      else{
          $('nav.sidebar').removeClass('stickytop');
      } 

      var scrollBottom = $(document).height() - $(window).scrollTop();
    	var baseOffset = 90;
      var offset = 0;
      var navbarHeight =  0;
    	var footerHeight =  0;

    	if ($( window ).outerWidth()< 768) {
    		baseOffset = 0; }
    	else {
    		baseOffset = 90; 
    	}
    	navbarHeight =  $('nav.sidebar').outerHeight() + baseOffset;
	footerHeight =  $('#mainFooter').outerHeight();
	
      if ((scrollBottom-footerHeight) <= navbarHeight) {
      	offset = (baseOffset + (scrollBottom-footerHeight) - navbarHeight).toString() + 'px';
      } else {
      	offset = baseOffset.toString() + 'px'
    	};
      $('nav.sidebar').css('top',  offset);

      var h = '100%'
      var windowHeight = $( window ).height()
      if (windowHeight > (scrollBottom-footerHeight)) {
      	h = (   windowHeight + (scrollBottom-windowHeight-footerHeight)    ).toString() + 'px' ;
  	}
	$('.hidden-sidebar-content').css('height',  h);
}


$(function(){
    $(window).scroll( stickySidebar );
    $(document).ready( stickySidebar );
});

