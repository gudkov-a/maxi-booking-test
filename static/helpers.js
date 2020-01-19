function get_currency () {
    $.ajax({
        method: 'GET',
        url: '/get_currency',
        }).done(function(data, status, request_obj) {
            $('.text_container').text(data);
        });
}

$(document).ready(function() {
    window.setInterval(function(){
        get_currency();
    }, 10000);
});