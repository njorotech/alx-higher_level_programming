#!/usr/bin/node
if (isNaN(process.argv[2])) {
  console.log('Missing number of occurrencies');
} else {
  let i = 0;
  const x = process.argv[2];
  while (i < x) {
    console.log('C is fun');
    i++;
  }
}
