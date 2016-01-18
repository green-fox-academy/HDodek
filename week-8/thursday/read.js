"use strict"

var fs = require("fs");


function readAppleTxt(callback) {
  fs.readFile("apple.txt", function(error, content) {
    var output= String(content);
    callback(output);
  });
};


readAppleTxt(function(content) {
  console.log(content);
});
