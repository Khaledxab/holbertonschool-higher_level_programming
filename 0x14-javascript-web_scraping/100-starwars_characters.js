#!/usr/bin/node
/** show charactersof sw movie */
const request = require('request');
const Id = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + Id;
let result = [];
request.get(url, (err, respponse, body) => {
  (err) ? console.log(err) : result = JSON.parse(body).characters;
  for (const charId in result) {
    request.get(result[charId], (err, response, body) => {
      (err) ? console.log(err) : console.log(JSON.parse(body).name);
    });
  }
});
