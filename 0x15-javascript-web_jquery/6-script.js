#!/usr/bin/node
/** change text in header */
const chH = window.$;
chH('DIV#update_header').click(function () {
  chH('HEADER').text('New Header!!!');
});
