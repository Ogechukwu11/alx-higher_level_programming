/* global $ */
$(document).ready(function () {
  $('#btn_translate').click(function () {
    const url = 'https://www.fourtonfish.com/hellosalut/hello/?';
    $.get(url + $.param({ lang: $('#language_code').val() }), function (data) {
      $('#hello').text(data.hello);
    });
  });
});
