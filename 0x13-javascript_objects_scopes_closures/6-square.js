#!/usr/bin/node
const Rectangle = require('./4-rectangle');
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      let i;
      let j;
      let output = '';
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
      let i;
      let j;
      let output = '';
      for (i = 0; i < this.height; i++) {
        for (j = 0; j < this.width; j++) {
          output += 'C';
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
