"use strict";

var number = [7, 8, 4, -1, 13, 55];
var a = number[0];

for (var i = 1; i < number.length; i++) {
  if (number[i] < a) {
    a = number[i];
  }
}

console.log(a);



var number = [7, 8, 4, -1, 13, 55];
var a = number[0];

for (var i = 1; i < number.length; i++) {
  a = (number[i] < a ? number[i] : a);
}

console.log(a);
