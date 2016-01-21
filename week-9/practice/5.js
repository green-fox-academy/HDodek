"use strict";

var kids = [
	{name: "Julika", age: 8, sex: "female"},
	{name: "Tiborka", age: 7, sex: "male"},
	{name: "Zsolti", age: 6, sex: "male"},
	{name: "Gerda", age: 9, sex: "female"},
	{name: "Zsomborka", age: 8, sex: "male"},
];

function filterNameBySex(kids, sex) {
  var output = [];
  kids.forEach(function(e) {
    if (e.sex === sex) {
      output.push(e.name);
    }
  })
  return output;
}

console.log(filterNameBySex(kids, "female")); //"Julika", "Gerda"
