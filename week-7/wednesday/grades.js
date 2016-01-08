"use strict";

function Students() {
  this.grade = [];
  this.average = 0;
  this.addGrade = function(grade) {
    this.grade.push(grade);
  }
  this.getAverage = function() {
    this.average = this.grade.reduce(function (acc, num) {
      return acc + num; },0) / this.grade.length;

  }
}


var belacska = new Students();

belacska.addGrade(5);
belacska.addGrade(3);
belacska.addGrade(1);
belacska.getAverage();


console.log(belacska.grade);
console.log(belacska.average);
