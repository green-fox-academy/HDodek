"use strict";

var express = require("express");
var url = require("url");
var app = express();

app.get("/", function(req, res) {
  res.send("Hello world");
});

app.get("/add", function(req, res) {
  var urlParts = url.parse(req.url, true);
  var query = urlParts.query;
  var a = parseInt(req.params["a"]);
  var b = parseInt(req.params["b"]);
  var result = a + b;

  console.log(a, b);
  console.log(query);
  res.send(result.toString() + "\n");
});

app.post("/add", function(req, res) {
  console.log(req.body);
  res.status(200);
})

app.get("/:name", function (req, res) {
  var name = req.params["name"];
  console.log("Name: " + name);
res.send("Hello, " + name + "\n;")
});

app.listen(3000);
