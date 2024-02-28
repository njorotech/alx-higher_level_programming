#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  const size = list.length;
  for (let i = 0; i < size; i++) {
    if (list[i] === searchElement) {
      count++;
    }
  }
  return count;
};
