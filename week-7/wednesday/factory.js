"use strict";

function createCar(color, type, km) {
  return {
    color: color,
    type: type,
    km: km,
    ride: function(km) {
      this.km += km;
    }
  }
}

var lambo = createCar("sarga", "asffv", 500);
lambo.ride(100);

console.log(lambo.km);
