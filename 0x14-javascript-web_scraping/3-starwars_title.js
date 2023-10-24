#!/usr/bin/node
const request = require('request');

if (process.argv.length !== 3) {
  console.error('Usage: ./3-starwars_title.js <movie ID>');
  process.exit(1);
}

const movieID = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieID}`;

request(apiUrl, function (error, response, body) {
  if (error) {
    console.error('Error:', error);
    process.exit(1);
  } else if (response.statusCode !== 200) {
    console.error('Error:', `HTTP Status Code ${response.statusCode}`);
    process.exit(1);
  } else {
    const movieData = JSON.parse(body);
    console.log(movieData.title);
  }
});
