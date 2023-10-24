#!/usr/bin/node
const request = require('request');

if (process.argv.length !== 3) {
  console.error('Usage: ./101-starwars_characters.js <Movie ID>');
  process.exit(1);
}

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(apiUrl, function (error, response, body) {
  if (error) {
    console.error('Error:', error);
    process.exit(1);
  } else if (response.statusCode !== 200) {
    console.error('Error:', `HTTP Status Code ${response.statusCode}`);
    process.exit(1);
  } else {
    const movieData = JSON.parse(body);
    const characterUrls = movieData.characters;

    // Define a function to fetch and print character names
    function fetchCharacterName(index) {
      if (index < characterUrls.length) {
        const characterUrl = characterUrls[index];
        request(characterUrl, function (error, response, body) {
          if (!error && response.statusCode === 200) {
            const characterData = JSON.parse(body);
            console.log(characterData.name);
            fetchCharacterName(index + 1); // Recursively fetch the next character
          }
        });
      }
    }

    // Start fetching and printing character names from the first character
    fetchCharacterName(0);
  }
});
