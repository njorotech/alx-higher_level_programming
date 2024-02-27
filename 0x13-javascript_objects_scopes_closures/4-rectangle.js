#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const toPrint = 'X'.repeat(this.width);
    for (let i = 0; i < this.height; i++) {
      console.log(toPrint);
    }
  }

  rotate () {
    const tempWidth = this.width;
    const tempHeight = this.height;
    this.width = tempHeight;
    this.height = tempWidth;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
};
