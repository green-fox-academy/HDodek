"use strict";

var a = 123;

function printA() {
  console.log(a);
  a = 523;
}

printA();
console.log(a);


function printLocalA() {
  var a = 9;
  console.log(a);
}

printLocalA();
console.log(a);
