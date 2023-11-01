$(document).ready(function () {
  const url = 'https://www.fourtonfish.com/hellosalut/hello/';
  $('INPUT#btn_translate').click(function () {
    const lang = $('INPUT#language_code').val();
    $.get(url, { lang }, function (data) {
      $('DIV#hello').text(data.hello);
    });
  });
});
