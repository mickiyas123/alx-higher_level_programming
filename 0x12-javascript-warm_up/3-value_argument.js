#!/usr/bin/node
const argLen = process.argv.length;

if (argLen >= 3) {
    console.log(process.argv[2]);
} else {
  console.log('No argument');
}
