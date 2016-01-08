"use strict";

function Car(color, type, km) {
  this.color = color;
  this.type = type;
  this.km = km;
  this.ride = function(km) {
    this.km += km;
  }
}

var golf = new Car("fekete", "1.", 1000);

golf.ride(200);

console.log(golf.km);
