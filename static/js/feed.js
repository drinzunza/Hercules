
function init() {
    console.log("Feed JS Works!");

    $(".u-avatar").hover(
        function(){
            // in
            $(this).parent().find('.popup').css({'visibility': 'visible'});
        },
        function() {
            //out
            $(this).parent().find('.popup').css({'visibility': 'hidden'});
        }
    );
}


window.onload = init;