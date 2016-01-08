"use strict";

//1.
var benaszavak = ["kuty",
"macsk",
"alm",
"gabon"];

var faszaszavak = [];

for (var i = 0; i < benaszavak.length; i++) {
  faszaszavak.push(benaszavak[i] + "a");
};
console.log(faszaszavak);

//2.
var faszaszavak2 = [];

benaszavak.forEach(function (szo) {
  faszaszavak2.push(szo + "a");
});

console.log(faszaszavak2);

//3.
var faszaszavak3 = benaszavak.map(function (szo) {
  return szo + "a";
});

console.log(faszaszavak3);
