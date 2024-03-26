#!/usr/bin/node

const fs = require('fs');
const filePath = process.argv[2];
// Read the content of the file
fs.readFile(filePath, 'utf8', (err, data) => {
  if (err) {
    console.log(err);
  }
  console.log(data);
});
