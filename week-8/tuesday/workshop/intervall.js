"use strict"

var count = 0;

setInterval(function() {
  count++;
  console.log("Yeyeee " + count)
}, 500);

setTimeout(function() {
  console.log("Bibiii")
}, 5000);
