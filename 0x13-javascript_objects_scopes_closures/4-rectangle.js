#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (((w = parseInt(w)) > 0) && ((h = parseInt(h)) > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
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
  }

  rotate () {
    this.width = this.width - this.height;
    this.height = this.height + this.width;
    this.width = this.height - this.width;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}
module.exports = Rectangle;
