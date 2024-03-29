#!/usr/bin/node

const fs = require('fs');
const request = require('request');
const url = process.argv[2];
const filePath = process.argv[3];

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  fs.writeFile(filePath, body, 'utf8', (err, data) => {
    if (err) {
      console.log(err);
    }
  });
});
