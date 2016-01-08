"use strict";

function range(from, to, steps) {
  var output = [];
  if (steps > 0) {
  for (var i = from; i < to; i+=steps){
    output.push(i);
  }
} else { for(var i = from; i > to; i+=steps){
  output.push(i);
}
  return output;
}

console.log(range(8, 4, -1));
