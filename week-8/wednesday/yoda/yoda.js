"use strict"

var ACCESS_TOKEN = 'JNDzfN0Pz8mshV6DHISeFTRHJy00p1LvLoKjsnSUpz0krIeYGX';
var url = 'https://yoda.p.mashape.com/yoda';
var sentence = "I like chocolate ice cream";
var urlWithParams = url + '?sentence=' + encodeURIComponent(sentence);
var probaRequest = new XMLHttpRequest();

var responseContainer = document.querySelector(".yoda-response");


function createRequest(url, callback) {
  var probaRequest = new XMLHttpRequest;
  probaRequest.open('GET', urlWithParams);
  probaRequest.setRequestHeader('X-Mashape-Key', ACCESS_TOKEN);
  probaRequest.send();
  probaRequest.onreadystatechange = function() {
    console.log("allapot", probaRequest.readyState);
    if (probaRequest.readyState === 4) {
      callback(probaRequest.response);
    }
  }
};

function onDone(response) {
  responseContainer.innerText = response;
};

var yodaButton = document.querySelector(".yoda-button");
var yodaInput = document.querySelector(".yoda-input");

yodaButton.addEventListener("click", function() {
  var url = 'https://yoda.p.mashape.com/yoda';
  var sentence = yodaInput.value;
  var urlWithParams = url + '?sentence=' + encodeURIComponent(sentence);

  responseContainer.innerText = "loading..."
  createRequest(urlWithParams, onDone);
});
