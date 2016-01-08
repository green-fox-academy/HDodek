"use strict";

function reverse(text) {
  var output = ""
  for (var i = text.length - 1; i > -1; i--) {
    output += text[i];
  }
    return output;
}

console.log(reverse("dorka"));
