#!/usr/bin/node
/** say hello */
const prnt = window.$;
prnt(document).ready(function () {
  prnt.get('https://fourtonfish.com/hellosalut/?lang=fr', (data) => {
    prnt('DIV#hello').text(data.hello);
  });
});
