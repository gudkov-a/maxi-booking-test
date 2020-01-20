function get_currency () {
    $.ajax({
        method: 'GET',
        url: '/get_currency',
        }).done(function(data, status, request_obj) {
            $('.text_container').text(data);
        });
}

function decrement_timer() {
    var current_value = $('.refresh_timer').text();
    if (current_value > 1) {
        current_value -= 1;
        $('.refresh_timer').text(current_value);
    } else if (current_value == 1) {
        get_currency();
        $('.refresh_timer').text(10);
    }
}

$(document).ready(function() {
    decrement_timer();
    window.setInterval(function(){
        decrement_timer();
    }, 1000);
});