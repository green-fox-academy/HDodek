"use strict";

var numbers = [5, 6, 3, 10];

var sum = numbers.reduce(function (acc, num) {
  return acc + num;
}, 0);

console.log(sum);
