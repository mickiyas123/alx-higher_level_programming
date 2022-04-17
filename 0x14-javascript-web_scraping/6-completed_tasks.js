#!/usr/bin/node
const request = require('request');
request('https://jsonplaceholder.typicode.com/users', function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const x = {};
  let c = 0;
  const users = JSON.parse(body);
  for (let k = 0; k < users.length; k++) {
    request(process.argv[2], function (error, response, body) {
      if (error) {
        console.log(error);
      }
      let i = 0;
      for (const todo of JSON.parse(body)) {
        if (users[k].id === todo.userId) {
          if (todo.completed === true) {
            i++;
          }
        }
      }
      c++;
      x[users[k].id] = i;
      if (c === users.length) {
        console.log(x);
      }
    });
  }
});
