function addReaction(reaction, postId){
    console.log("Adding a", reaction, postId);

    $.ajax({
        url: '/post/react/' + postId,
        method: "POST",
        data: {
            'reaction': reaction,
            'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val()
        },
        success: function(response){
            console.log(response)
            $(".like-count").text(response.likes);
            $(".dislike-count").text(response.dislikes);
            $(".heart-count").text(response.heart);
        },
        error: function(error){
            console.log("failed", error)
        }
    })
}

function init() {
    console.log("Feed JS works!");

    $(".u-avatar").hover(
        function(){
            //in
            $(this).parent().find('.popup').css({'visibility': 'visible'});
        },
        function(){
            //out
            $(this).parent().find('.popup').css({'visibility': 'hidden'});
        }
    );

    $(".like").click(function () {
        const id = $(this).parent().parent().attr('id');
        addReaction('like', id);
    });

    $(".dislike").click(function () {
        const id = $(this).parent().parent().attr('id');
        addReaction('dislike', id);
    });

    $(".heart").click(function () {
        const id = $(this).parent().parent().attr('id');
        addReaction('heart', id);
    });

}


window.onload = init;