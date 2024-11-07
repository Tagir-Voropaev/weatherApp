$(document).ready(function(){

    var minClick = 2;
    var click = 0;
    $( ".scroll-button-left" ).on( "click", function() {
        
        if (click >= 1){
            click-=1;
            $(".scroll-week").animate({ left: "+=180" }, 200);
        }
    } );

    $( ".scroll-button-right" ).on( "click", function() {
        if (click <= minClick){
            click+=1;
            $(".scroll-week").animate({ left: "-=180" }, 200);
        }
    } );
});