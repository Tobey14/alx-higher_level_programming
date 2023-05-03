$.ajax({
    method: 'GET',
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    accept: 'application/json',

    success: function(result){
        movies = result.results;
        movies.forEach(movie => {
            $('ul#list_movies').append('<li>'+movie.title+'</li>')
        });
        
        // console.log(result.results)
        // $("#div1").html(result);
    }
})
