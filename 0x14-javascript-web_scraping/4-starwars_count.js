#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];
let num = 0;

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  const data = JSON.parse(body);
  // access to result information
  const data2 = data.results;
  for (let i = 0; i < data2.length; i++) {
    if (data2[i].characters) {
      for (const j of data2[i].characters) {
        if (j.includes('18')) {
          num++;
        }
      }
    }
  }
  console.log(num);
});
