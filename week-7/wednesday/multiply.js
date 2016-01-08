"use strict";

function multiply(number) {
  for (var i = 1; i <= 10; i++)
  console.log(String(i), '*', String(number), '=', number * i);
}

multiply(5);


function multiplyAll() {
  for (var a = 1; a <= 10; a++) {
    for (var b = 1; b <= 10; b++) {
      console.log(String(b), '*', String(a), '=', a * b);
    }
  }
}

multiplyAll()

//for, forEach, map, reduce

var szorzotabla1 = "";

for (var i = 1; i <= 10; i++) {
  szorzotabla1 += i + "*" + 4 + "=" + i*4 + '\n';
}
console.log(szorzotabla1);

var szamok = [1, 2, 3, 4, 5, 6, 7, 8, 10];
var szorzotabla2 = "";
szamok.forEach(function (e) {
  szorzotabla2 += e + "*" + 4 + "=" + e * 4 + '\n';
})
console.log(szorzotabla2);

var szorzotabla3 = "";
var sorok = szamok.map(function (e) {
  return e + "*" + 4 + "=" + e * 4;
});
szorzotabla3 = sorok.join('\n');
console.log(szorzotabla3);
