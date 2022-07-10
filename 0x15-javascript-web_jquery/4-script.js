#!/usr/bin/node
/** toggle classes */
const cls = window.$;
cls('DIV#red_header').click(function () {
  cls('HEADER').last().addClass('red');
});
