#!/usr/bin/node

const fs = require('fs');
const filePath = process.argv[2];
const contentToWrite = process.argv[3];
// Write content to the file
fs.writeFile(filePath, contentToWrite, 'utf8', (err) => {
  if (err) {
    console.log(err);
  }
});
