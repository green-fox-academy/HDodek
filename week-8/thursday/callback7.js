"use strict";

var fs = require("fs");

var out = "";

fs.readFile("apple.txt", function(error, almaContent) {
  fs.readFile("pear.txt", function(error, pearContent) {
    console.log(almaContent + pearContent);
  })
})
