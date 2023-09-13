#!/usr/bin/node
module.exports = class Square extends require('./5-square') {
  charPrint (c) {
    if (String(c) === 'undefined') {
      this.print();
    } else {
      for (let n = 0; n < this.height; n++) console.log(String(c).repeat(this.width));
    }
  }
};
