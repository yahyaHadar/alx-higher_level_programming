$(function () {
  $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    type: 'GET',
    success: function (data) {
      $.each(data.results, function (i, movie) {
        $('UL#list_movies').append('<li>' + movie.title + '</li>');
      }); // Correct placement of closing parenthesis
    },
    error: function (jqXHR, textStatus, errorThrown) {
      console.error('AJAX error:', textStatus, errorThrown);
    }
  });
});
