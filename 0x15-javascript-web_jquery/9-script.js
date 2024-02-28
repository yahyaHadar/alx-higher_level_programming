$(function () {
  $.ajax({
    url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
    type: 'GET',
    success: function (data) {
      $('DIV#hello').append(data.hello);
    },
    error: function (jqXHR, textStatus, errorThrown) {
      console.error('AJAX error:', textStatus, errorThrown);
    }
  });
});
