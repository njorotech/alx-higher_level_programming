const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
$(function () {
  $.get(url, function (data, statusTxt) {
    if (statusTxt === 'success') {
      const films = data.results;
      for (const item in films) {
        $('#list_movies').append('<li>' + films[item].title + '</li>');
      }
    }
  });
});
