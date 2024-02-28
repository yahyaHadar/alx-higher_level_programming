$(document).ready(function () {
  const url = 'https://hellosalut.stefanbohacek.dev/?lang=';
  $('#btn_translate').click(function () {
    $('#hello').empty();
    const lang = $('#language_code').val();
    $.get(url + lang, function (data) {
      $('#hello').append(data.hello);
    });
  });
});
