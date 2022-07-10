#!/usr/bin/node
/** store a content in a file */
/** chr= characters m= movie i= count */
const request = require('request');
const url = process.argv[2];
let result = [];
request.get(url, (error, body) => {
  (error) ? console.log(error) : result = JSON.parse(body).results;
  let i = 0;
  for (const m in result) {
    const chr = result[m].chr;
    for (const char in chr) {
      if (chr[char].endsWith('/18/')) {
        i += 1;
      }
    }
  }
  console.log(i);
});
