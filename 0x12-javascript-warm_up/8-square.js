#!/usr/bin/node
const i = process.argv[2];
if (isNaN(i)) {
  console.log('Missing size');
} else {
  let x = 0;
  while (x < i) {
    let y = 0;
    let print = '';
    while (y < i) {
      print += 'X';
      y++;
    }
    console.log(print);
    x++;
  }
}
