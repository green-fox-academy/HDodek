"use strict"


var fs = require("fs");

fs.readFile("apple.txt", function(err, content) {
  console.log(String(content));
});
