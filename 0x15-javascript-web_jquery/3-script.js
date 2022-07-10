#!/usr/bin/node
/** chng clr on click no dc.queSelect  */
const change = window.$;
change('DIV#red_header').click(function () {
  change('header').last().addClass('red');
});
