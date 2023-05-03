$(document).ready(function(){
    $.ajax({
        method: 'GET',
        url: 'https://fourtonfish.com/hellosalut/?lang=fr',
        accept: 'application/json',

        success: function (result) {
            $('div#hello').text(result.hello)
        }
    })
})

