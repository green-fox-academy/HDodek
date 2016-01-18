"use strict"

var createCandie = document.querySelector(".candiebutton");
var buyLollipop = document.querySelector(".lollibutton");
var currentCandy = 500;
var currentLolli = 0;
var timecount = 0;

function updateCandies() {
  document.querySelector(".candies").innerHTML=("Your candies: " + currentCandy);
};

function updateLollies() {
  document.querySelector(".lollipops").innerHTML=("Your lollipops: " + currentLolli);
};

function updateCount() {
  document.querySelector(".candiespersec").innerHTML=("Candy/Second: " + timecount);
};

function addCandie() {
  currentCandy++;
  updateCandies();
  if(currentCandy >= 10000) {
    alert("YoU aRe tHe WiNnEeEr!");
    restartGame();
  }
};

function buyLolli() {
  if (currentCandy >= 10) {
    currentCandy -= 10;
    currentLolli++;
    updateLollies();
    updateCandies();
  }
};

function restartGame() {
  currentCandy = 0;
  currentLolli = 0;
  updateLollies();
  updateCandies();
};

function increasespeed() {
  timecount = Math.floor(currentLolli / 10)
  currentCandy += timecount;
  updateCandies();
  updateCount();
};

function setSpeed() {
setInterval(increasespeed, 1000);
};

createCandie.addEventListener("click", addCandie);
buyLollipop.addEventListener("click", buyLolli);
setSpeed();
