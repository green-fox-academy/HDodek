"use strict";

console.log("mukodik");

var cim = document.querySelector(".majom");
console.log(cim);

cim.classList.add("piros");

var majomkep = document.querySelector("img");
majomkep.setAttribute("src", "https://41.media.tumblr.com/84729c469ca431c8c80dad1cd4281205/tumblr_o08zo7SJan1tx21ogo1_540.jpg");

function kepcsinalo(src) {
  var ujkep = document.createElement("img");
  ujkep.setAttribute("src", src);

  var bodyvaltozoban = document.querySelector("body")
  bodyvaltozoban.appendChild(ujkep);
}
for (var i = 0; i < 10; i++) {
kepcsinalo("https://41.media.tumblr.com/84729c469ca431c8c80dad1cd4281205/tumblr_o08zo7SJan1tx21ogo1_540.jpg");
};

var kepek = [
  "https://s-media-cache-ak0.pinimg.com/736x/eb/ff/38/ebff38063b30af2bd2abaa79827a3fd3.jpg",
  "http://cdn.meme.am/instances/500x/53203200.jpg",
  "http://lorempixel.com/image_output/cats-q-c-301-222-9.jpg",
  "http://lorempixel.com/image_output/animals-q-c-448-371-1.jpg",
  "http://lorempixel.com/image_output/city-q-c-448-371-2.jpg",
  "http://lorempixel.com/image_output/people-q-c-448-371-5.jpg",
  "http://lorempixel.com/image_output/food-q-c-448-371-6.jpg",
  "http://lorempixel.com/image_output/food-q-c-448-371-4.jpg",
  "http://lorempixel.com/image_output/nightlife-q-c-448-371-3.jpg",
  "http://lorempixel.com/image_output/nature-q-c-448-371-7.jpg"
]
for (var i = 0; i < kepek.length; i++) {
  kepcsinalo(kepek[i]);
};

var gomb = document.querySelector(".csing");

//gomb.addEventListener("click", function () {
//  alert("kattintottam!!");
//});

gomb.addEventListener("click", function () {
  kepcsinalo("https://media.giphy.com/media/vhsNmFjuN4WDS/giphy.gif")
});
window.addEventListener("scroll", function (){
  console.log("scroll"),
  console.log(window.scrollY);
});


var cicagomb = document.querySelector(".cicat");
var kajagomb = document.querySelector(".kajat");
var valtokep = document.querySelector(".cicakaja");

kajagomb.addEventListener("click", function() {
  valtokep.setAttribute("src", "http://lorempixel.com/image_output/nature-q-c-448-371-7.jpg");
});

cicagomb.addEventListener("click", function() {
  valtokep.setAttribute("src", "http://lorempixel.com/image_output/cats-q-c-301-222-9.jpg");
});
