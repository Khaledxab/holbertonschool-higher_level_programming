#!/usr/bin/node
/** STATUS check of GET request */
const request = require('request');
const url = process.argv[2];
request(url, (error, response, body) => {
  (error) ? console.log(error) : console.log('code:' + response.statusCode);
});
