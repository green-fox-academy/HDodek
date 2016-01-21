"use strict";

var kids = [
	{name: "Julika", age: 8, sex: "female"},
	{name: "Tiborka", age: 7, sex: "male"},
	{name: "Zsolti", age: 6, sex: "male"},
	{name: "Gerda", age: 9, sex: "female"},
	{name: "Zsomborka", age: 8, sex: "male"},
];

function getAgeByName(kids, name) {
	var output = 0;
	kids.forEach(function(e) {
		if(e.name === name) {
			output = e.age;
		}
	});
	return output;
}

console.log(getAgeByName(kids, "Gerda"));
