#!/usr/bin/node
const request = require('request');
const id = Number(process.argv[2]);
request(`https://swapi-api.hbtn.io/api/films/${id}`, function (error, response, body) {
  if (error) {
    return;
  }
  const characters = JSON.parse(body).characters;
  const characterName = [];
  let j = 0;
  for (let i = 0; i < characters.length; i++) {
    request(characters[i], function (error, response, body) {
      if (error) {
        return;
      }
      j++;
      characterName.push(JSON.parse(body).name);
      if (j === characters.length) {
        for (const name of characterName) {
          console.log(name);
        }
      }
    });
  }
});
