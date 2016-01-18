"use strict";

var express = require("express");
var url = require('url');
var app = express();
var items = [
  {item: "buy milk"},
  {item: "do homework"},
  {item: "buy butter"},
];

app.get("/", function(req, res) {
  res.json(items);
});

app.post("/", function(req, res) {
  items.push(req.body);
  res.status(200);
});





app.listen(3000);
