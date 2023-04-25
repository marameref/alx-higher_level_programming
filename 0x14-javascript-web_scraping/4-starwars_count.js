#!/usr/bin/node

const request = require('request');
const args = process.argv;
const requestURL = args[2];

request.get(requestURL, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const allData = JSON.parse(body);
    const results = allData.results;
    let count = 0;
    for (let i = 0; i < results.length; i++) {
      for (let j = 0; j < results[i].characters.length; j++) {
        if (results[i].characters[j].includes('18')) { count += 1; }
      }
    }

    console.log(count);
  }
});
