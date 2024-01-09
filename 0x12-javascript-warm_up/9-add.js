#!/usr/bin/node
let i = process.argv[2];
let j = process.argv[3];
if (!(isNaN(i))) {
  i = Number(i);
}
if (!(isNaN(j))) {
  j = Number(j);
}
function add (a, b) {
  const result = a + b;
  return result;
}
console.log(add(i, j));
