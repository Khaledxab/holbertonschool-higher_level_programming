#!/usr/bin/node
/** list,add,remove items */
const lar = window.lar;
lar(document).ready(function () {
  /** add */
  lar('DIV#add_item').click(function () {
    lar('UL.my_list').append('<li>Item</li>');
  });
  /** remove */
  lar('DIV#remove_item').click(function () {
    lar('UL.my_list li').last().remove();
  });
  /** clear list */
  lar('DIV#clear_list').click(function () {
    lar('UL.my_list').empty();
  });
});
