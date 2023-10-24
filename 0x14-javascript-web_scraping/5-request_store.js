#!/usr/bin/node
const request = require('request');
const fs = require('fs');

if (process.argv.length !== 4) {
  console.error('Usage: ./5-request_store.js <URL> <file path>');
  process.exit(1);
}

const url = process.argv[2];
const filePath = process.argv[3];

request(url, function (error, response, body) {
  if (error) {
    console.error('Error:', error);
    process.exit(1);
  } else if (response.statusCode !== 200) {
    console.error('Error:', `HTTP Status Code ${response.statusCode}`);
    process.exit(1);
  } else {
    // Write the response body to the specified file
    fs.writeFileSync(filePath, body, 'utf-8');
  }
});
