const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
$(function () {
  $.get(url, function (data, statusTxt) {
    if (statusTxt === 'success') {
      $('#hello').text(data.hello);
    }
  });
});
