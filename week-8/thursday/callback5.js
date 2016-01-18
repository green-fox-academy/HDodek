"use strict";


var fs = require("fs");
function countLetterInAlmaTxt(letter, callback) {
  fs.readFile("apple.txt", function(err, content) {
    var stringContent = String(content);
    var count = 0;
    for (var i = 0; i < stringContent.length; i++) {
      if (stringContent[i] === letter) {
        count++;
      }
    }
    callback(count);
  })
}

countLetterInAlmaTxt("a", function(count) {
  console.log(count);
});
