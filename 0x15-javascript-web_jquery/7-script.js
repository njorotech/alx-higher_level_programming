const url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
$(function () {
  $.get(url, function (responseTxt, statusTxt) {
    if (statusTxt === 'success') {
      $('#character').text(responseTxt.name);
    }
  });
});
