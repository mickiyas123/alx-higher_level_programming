#!/usr/bin/node
exports.esrever = function (list) {
  const reversedArray = [];
  let i;
  for (i = list.length - 1; i >= 0; i--) {
    reversedArray.push(list[i]);
  }
  return reversedArray;
};
