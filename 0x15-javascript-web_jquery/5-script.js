#!/usr/bin/node
/** li 'list of element' : add when click */
const addLi = window.$;
addLi('DIV#add_item').click(function () {
  addLi('UL.my_list').append('<li>Item</li>');
});
