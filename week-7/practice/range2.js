"use strict";

function range(first, last) {
  var output = [];
  for (var i = first; i <= last; i++){
    output.push(i);
  }
  return output;
}

console.log(range(3, 6));
