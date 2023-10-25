#!/usr/bin/node
/* prints the title of a Star Wars movie where the
episode number matches a given integer. */
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2] + '/';
request.get(url).on('response', function (response) {
  console.log(JSON.parse(response.body).title);
});
