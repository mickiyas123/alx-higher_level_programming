#!/usr/bin/node

let i;
let fact = 1;
const num = parseInt(process.argv[2]);

if (isNaN(num) || num === 0 || num === 1) {
  console.log(1);
} else {
  for (i = num; i >= 1; i--) {
    fact = fact * i;
  }
  console.log(fact);
}
