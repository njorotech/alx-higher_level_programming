#!/usr/bin/node
const args = process.argv.length;
const argsList = process.argv;
if (args === 2) {
  console.log(0);
} else if (args === 3) {
  console.log(0);
} else {
  let big = 0;
  let second = 0;
  for (let counter = 2; counter <= args; counter++) {
    const argValue = Number(argsList[counter]);
    if (argValue > big) {
      big = argValue;
    }
  }
  for (let i = 2; i <= args; i++) {
    const argsValue = Number(argsList[i]);
    if (argsValue > second && argsValue < big) {
      second = argsValue;
    }
  }
  console.log(second);
}
