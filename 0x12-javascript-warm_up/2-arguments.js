#!/usr/bin/node
const noOfArgs = process.argv.length;
if (noOfArgs === 2) {
  console.log('No argument');
} else if (noOfArgs === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
