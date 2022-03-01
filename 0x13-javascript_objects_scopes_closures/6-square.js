#!/usr/bin/node
const Rectangle = require('./5-square');
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let i;
    let j;
    let output = '';
    if (c === undefined) {
      for (i = 0; i < this.height; i++) {
        for (j = 0; j < this.width; j++) {
          output += 'X';
        }
        if (i !== this.height - 1) {
          output += '\n';
        }
      }
      console.log(output);
    } else {
      for (i = 0; i < this.height; i++) {
        for (j = 0; j < this.width; j++) {
          output += c;
        }
        if (i !== this.height - 1) {
          output += '\n';
        }
      }
      console.log(output);
    }
  }
}
module.exports = Square;
