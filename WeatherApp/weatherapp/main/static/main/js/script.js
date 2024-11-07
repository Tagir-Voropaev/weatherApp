$(document).ready(function(){

    var minClick = 3;
    var click = 0;
    $( ".scroll-button-left" ).on( "click", function() {
        
        if (click >= 1){
            click-=1;
            $(".scroll-week").animate({ left: "+=230" }, 200);
        }
    } );

    $( ".scroll-button-right" ).on( "click", function() {
        if (click <= minClick){
            click+=1;
            $(".scroll-week").animate({ left: "-=230" }, 200);
        }
    } );
});