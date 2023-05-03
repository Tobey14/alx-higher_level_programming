$.ajax({
    method: 'GET',
    url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
    accept: 'application/json',

    success: function(result){
        $('div#character').text(result.name)
    }

})
