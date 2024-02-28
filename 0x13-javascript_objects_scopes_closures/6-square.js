#!/usr/bin/node
const Square1 = require('./5-square');
module.exports = class Square extends Square1 {
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
