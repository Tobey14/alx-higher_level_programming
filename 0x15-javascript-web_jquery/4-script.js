$('div#toggle_header').click(function(){
    myClass = $('header').attr("class");
    if(myClass == 'green'){
        $('header').removeClass('green');
        $('header').addClass('red');
        return;
    }
    $('header').removeClass('red');
    $('header').addClass('green');
    return;
})
