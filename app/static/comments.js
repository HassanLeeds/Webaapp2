$(document).ready( function () {
    $(".comment-container").submit(function(event) {
        event.preventDefault();

        let post_id = $(this).find('input[name="postID"]').val();
        let content = $(this).find('input[name="comment"]');
        let modal = $("#modal" + post_id);
        let container = modal.find(".comments-container");
        content_val = content.val();
        console.log(post_id);
        console.log(content_val);

        $.ajax({
            url: "/comment/" + post_id,
            method: "POST",
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({ 'comment': content_val }),
            dataType: 'json',
            success: function(response) {
                if (response.result === "success") {
                    let comment_append = `
                    <h2>${response.comment.username}</h2>
                    <h3>${response.comment.content}</h3>
                    `
                    container.prepend(comment_append);
                    content.val("");
                }
            }
        })
    })
});