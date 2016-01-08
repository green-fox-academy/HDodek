"use strict";

var kids = [
{name: "beluka", candies: 3},
{name: "katika", candies: 15},
{name: "sanyika", candies: 30},
{name: "petike", candies: 0},
{name: "cicuka", candies: 8}
];

function getRichestKidName(kids) {
  var richestkid = kids[0];
  for (var i = 1; i < kids.length; i++) {
    if ( richestkid.candies < kids[i].candies) {
      richestkid = kids[i];
      }
    }
    return richestkid.name;
  }
console.log(getRichestKidName(kids));
