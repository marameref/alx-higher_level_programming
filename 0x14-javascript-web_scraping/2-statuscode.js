#!/usr/bin/node

const request = require('request');
const args = process.argv;

request(args[2], function (error, response, body) {
  if (error) { console.log(error); }
  console.log('code:', response && response.statusCode);
});
