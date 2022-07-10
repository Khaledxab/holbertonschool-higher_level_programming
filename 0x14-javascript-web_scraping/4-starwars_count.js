#!/usr/bin/node
/** store a content in a file */
/** characters= characters movie= movieovie i= count */
const request = require('request');
const url = process.argv[2];
let result = [];
request.get(url, (err, response, body) => {
  (err) ? console.log(err) : result = JSON.parse(body).results;
  let count = 0;
  for (const movie in result) {
    const characters = result[movie].characters;
    for (const char in characters) {
      if (characters[char].endsWith('/18/')) {
        count += 1;
      }
    }
  }
  console.log(count);
});
