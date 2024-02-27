#!/usr/bin/node
const Rectangle = require('./4-rectangle');
module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let toPrint = 'X'.repeat(this.width);
    if (c) {
      toPrint = c.repeat(this.width);
    }

    for (let i = 0; i < this.height; i++) {
      console.log(toPrint);
    }
  }
};
