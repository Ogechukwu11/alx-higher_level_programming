/* global $ */
$(document).ready(function () {
  $('#btn_translate').click(function () {
    fetchTranslation();
  });

  $('#language_code').keypress(function (event) {
    if (event.which === 13) {
      fetchTranslation();
    }
  });

  function fetchTranslation () {
    const url = 'https://www.fourtonfish.com/hellosalut/hello/?';
    $.get(url + $.param({ lang: $('#language_code').val() }), function (data) {
      $('#hello').text(data.hello);
    });
  }
});
