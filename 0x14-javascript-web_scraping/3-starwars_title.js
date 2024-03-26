#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const endPoint = 'https://swapi-api.alx-tools.com/api/films/';
// Make a GET request to the Star Wars API
request.get(endPoint + movieId, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  const data = JSON.parse(body);
  console.log(data.title);
});
