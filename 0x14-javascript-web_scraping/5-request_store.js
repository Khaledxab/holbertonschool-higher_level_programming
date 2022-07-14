#!/usr/bin/node
/**  gets contents of a webpage */
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const fileN = process.argv[3];
let r;
request.get(url, (err, respponse, body) => {
  (err) ? console.log(err) : r = body;
  fs.writeFile(fileN, r, 'utf-8', (err) => {
    if (err) {
      console.log(err);
    }
  });
});
