"use strict"

var fs = require("fs");

fs.readFile("alma.txt", function(error, content) {
  if (error) {
    console.log("para vaan");
  } else {
    console.log("butuska");
  }
});
