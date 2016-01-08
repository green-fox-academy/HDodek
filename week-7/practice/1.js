"use strict";

var grades = [4, 3, 5, 2, 5, 5];

function count5s() {
  var output = 0;
  for (var i = 0; i < grades.length; i++) {
    if (grades[i] === 5) {
      output += 1;
    }
  }
  return output;
}

console.log(count5s());

function foreach() {
  var out = 0;
  grades.forEach(function(e) {
    if (e === 5) {
      out += 1;
  }
})
  return out;
};

console.log(foreach());
