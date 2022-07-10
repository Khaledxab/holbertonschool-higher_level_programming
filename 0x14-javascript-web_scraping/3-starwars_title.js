#!/usr/bin/node
/** print a title of an ep from api */
const request = require('request');
const Id = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + Id;
request(url, (error, body) => {
  (error) ? console.log(error) : console.log(JSON.parse(body).title);
});
