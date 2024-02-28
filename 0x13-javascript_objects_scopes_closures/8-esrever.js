#!/usr/bin/node
exports.esrever = function (list) {
  const size = list.length;
  const reversedList = [];
  for (let i = size - 1; i >= 0; i--) {
    reversedList.push(list[i]);
  }
  return reversedList;
};
