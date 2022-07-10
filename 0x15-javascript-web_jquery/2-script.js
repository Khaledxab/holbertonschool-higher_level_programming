#!/usr/bin/node
/** change color on clicks */
const click = window.$;
click('DIV#red_header').click(function () {
  click('header').css('color', '#FF0000');
});
