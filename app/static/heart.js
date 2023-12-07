$(document).ready(function () {
    $(".heart").click(function (event) {
        event.preventDefault();

        let post_id = $(this).closest('.post').find('input[name="postID"]').val();
        let heart = $(this).closest('.post').find('input[name="heart"]').val();
        if(!heart){
            heart = true;
        }
        else {
            heart = false;
        }
        let container = $(".heart-form" + post_id);
        console.log(heart)

        $.ajax({
            url: "/heart/" + post_id,
            method: "POST",
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({ 'heart': heart }),
            dataType: 'json',
            success: function (response) {
                if (response.result === "success") {
                    // Update the UI based on the response, e.g., change the heart button image
                    if (response.heart) {
                        container.find('input[name="heart"]').attr('src', '../static/hearted.png');
                    } else {
                        container.find('input[name="heart"]').attr('src', '../static/heart.png');
                    }
                }
            }
        });
    });
});