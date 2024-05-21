#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  const completed = {};
  const data = JSON.parse(body);
  data.forEach(task => {
    if (task.completed === true) {
      if (completed[task.userId] === undefined) {
        completed[task.userId] = 1;
      } else {
        completed[task.userId]++;
      }
    }
  });
  console.log(completed);
});
