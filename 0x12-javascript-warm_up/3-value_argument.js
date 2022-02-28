#!/usr/bin/node
const argLen = process.argv.length;

if (argLen > 2) {
  let i;

  for (i = 2; i < argLen; i++) {
    console.log(process.argv[i]);
  }
} else {
  console.log('No argument');
}
