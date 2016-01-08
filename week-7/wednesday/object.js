"use strict";

var tesla = {
  type: "zX10",
  color: "white",
  km: 5000,
  ride: function(km) {
    this.km += 200;
  }
}


tesla.ride(200);

console.log(tesla.km);
console.log(tesla);
