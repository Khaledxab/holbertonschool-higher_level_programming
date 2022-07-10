#!/usr/bin/node
/** title fetcher from link */
const fetch = window.$;
fetch.get('https://swapi-api.hbtn.io/api/films/?format=json', (data) => {
  for (const i in data.results) {
    fetch('UL#list_movies').append('<li>' + data.results[i].title + '</li>');
  }
});
