#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response, body) {
  let count = 0;
  if (error) {
    return;
  }
  const results = JSON.parse(body).results;
  for (const chx of results) {
    for (const ch of chx.characters) {
      if (ch.includes('18')) {
        count++;
      }
    }
  }
  console.log(count);
});
