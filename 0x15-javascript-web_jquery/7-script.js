$(function () {
  $('DIV#character').load(
    'https://swapi-api.alx-tools.com/api/people/5/?format=json',
    function (resp, stat, err) {
      if (stat == 'success') {
        $('DIV#character').text(JSON.parse(resp).name);
      } else { alert('Error'); }
    });
});
