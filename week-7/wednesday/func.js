"use strict";

function greet(name) {
  console.log("Hello ", name);
}

greet("Dorka");


var koszontes = greet;
koszontes("Geza");

var print = console.log;
print("svbb")


function greeter(name, log) {
  log ("csako", name);
}
greeter("lajcsi", print);


var add = function (a, b) { return(a + b); } ;
console.log(add(1, 2));
