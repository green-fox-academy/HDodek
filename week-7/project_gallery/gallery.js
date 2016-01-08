"use strict"

var nextbutton = document.querySelector(".next");
var previousbutton = document.querySelector(".previous");
var currentpicture = document.querySelector(".currentpicture");


var pictures = [
  "pictures/first.jpg",
  "pictures/ballett.jpg",
  "pictures/jazz.jpg",
  "pictures/thai.jpg"
];

var currentIndex = 0;

function nextPicture() {
  currentIndex++;
  if (currentIndex > pictures.length -1) {
    currentIndex = 0;
  }
  currentpicture.setAttribute("src", pictures[currentIndex]);
};

function previousPicture() {
  currentIndex--;
  if (currentIndex === -1) {
    currentIndex = pictures.length -1;
  }
  currentpicture.setAttribute("src", pictures[currentIndex]);
};

nextbutton.addEventListener("click", function() {
  nextPicture();
});

previousbutton.addEventListener("click", function() {
  previousPicture();
});

currentpicture.addEventListener("click", function() {
  nextPicture();
});
