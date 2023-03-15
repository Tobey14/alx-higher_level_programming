#!/usr/bin/node
/* class: Rectangle that defines a Rectangle takes two arguments
and evaluate if is an positive integer */
class Rectangle {
  constructor (w, h) {
    if (Number(w) > 0 && Number(h) > 0) {
      this.width = w;
      this.height = h;
    }
  }
}
module.exports = Rectangle;
