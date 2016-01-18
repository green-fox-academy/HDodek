"use strict"

var fs = require("fs");

function countLetterP(callback) {
  fs.readFile("alma.txt", function(err, content) {
    var count = 0;
    var stringoutput = String(content);
    for (var i = 0; i < stringoutput.length; i++) {
      if (stringoutput[i] === "p") {
        count++;
      }
    }
    callback(count);
  })
}

countLetterP(function(count) {
  console.log(count); //2//
});
