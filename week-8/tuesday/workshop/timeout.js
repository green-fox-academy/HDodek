"use strict"

var timeout = setTimeout(function() {
  console.log("Yaay");
}, 10000);


clearTimeout(timeout);
