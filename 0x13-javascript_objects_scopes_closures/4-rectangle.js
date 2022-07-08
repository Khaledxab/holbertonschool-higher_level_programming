#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
	  if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
	  }
  }

  print () {
	  let rec = '';
	  for (let a = 0; a < this.height; a++) {
      for (let b = 0; b < this.width; b++) {
		  rec += 'X';
      }
      if (i <= this.height - 2) {
		  rec += '\n';
      }
	  }
	  console.log(rec);
  }

  rotate () {
	  const a = this.height;
	  this.height = this.width;
	  this.width = a;
  }

  double () {
	  this.width *= 2;
	  this.height *= 2;
  }
};
