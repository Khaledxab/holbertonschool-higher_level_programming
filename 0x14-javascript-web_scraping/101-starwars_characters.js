#!/usr/bin/node
/** print all characters of a Star Wars movie */
const request = require('request');
const Id = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + Id;
let chars;
const Names = {};
request.get(url, (err, respponse, body) => {
  (err) ? console.log(err) : chars = JSON.parse(body).characters;
  for (const id of chars) {
    request.get(id, (err, response, body) => {
      if (!err) {
        Names[id] = JSON.parse(body).name;
        if (Object.values(Names).length === chars.length) {
          for (const id of chars) {
            console.log(Names[id]);
          }
        }
      }
    });
  }
});
