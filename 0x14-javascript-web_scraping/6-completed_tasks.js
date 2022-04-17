#!/usr/bin/node
const request = require('request');
request('https://jsonplaceholder.typicode.com/users', function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const x = {};
  let k = 0;
  for (const user of JSON.parse(body)) {
    request(process.argv[2], function (error, response, body) {
      if (error) {
        console.log(error);
      }
      let i = 0;
      for (const todo of JSON.parse(body)) {
        if (user.id === todo.userId) {
          if (todo.completed === true) {
            i++;
          }
        }
      }
      k++;
      x[user.id] = i;
      if (k === 10) {
        console.log(x);
      }
    });
  }
});
