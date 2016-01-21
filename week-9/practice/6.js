"use strict";

var kids = [
	{name: "Julika", age: 8, sex: "female"},
	{name: "Tiborka", age: 7, sex: "male"},
	{name: "Zsolti", age: 6, sex: "male"},
	{name: "Gerda", age: 9, sex: "female"},
	{name: "Zsomborka", age: 8, sex: "male"},
];


function countBySex(kids) {
  var output = {female: 0, male: 0};
  kids.forEach(function(e) {
    if (e.sex === "female") {
      output["female"]++;
    } else {
      output["male"]++;
    }
  })
  return output;
}

console.log(countBySex(kids)); //{female: 2, male: 3}

function countBySex(kids) {
  var output = {female: 0, male: 0};
  kids.forEach(function(e) {
      output[e.sex]++;
    })
  return output;
}

console.log(countBySex(kids)); //{female: 2, male: 3}
