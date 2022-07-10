#!/usr/bin/node
/** star war character */
const swchar = window.$;
swchar.get('https://swapi-api.hbtn.io/api/people/5/?format=json', (data) => {
  swchar('DIV#character').text(data.name);
});
