// toggle class scroll 
$(window).scroll(function() {
    if($(this).scrollTop() > 50)
    {
        $('.navbar-trans').addClass('afterscroll');
    } else
    {
        $('.navbar-trans').removeClass('afterscroll');
    }  

});
  
// demo only 
// open link in new tab without ugly target="_blank"
$("a[href^='http']").attr("target", "_blank");
