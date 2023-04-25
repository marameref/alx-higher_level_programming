#!/usr/bin/node

const fs = require('fs');
const request = require('request');

const args = process.argv;
const requestURL = args[2];

request.get(requestURL, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const data = body;
    fs.writeFile(args[3], data, 'utf-8', (err) => {
      if (err) { console.log(err); }
    });
  }
});
