"use strict";

function Student() {
  this.grades = {'matek': [], 'rajz': []};
  this.addGrade = function(subject, grade) {
    this.grades[subject].push(grade);
  }
  this.getCount = function() {
    var output = {};
    for ( var subject in this.grades) {
      output[subject] = this.grades[subject].length;
    }
    return output;
  }
  this.getAverage = function() {
    var sum = 0;
    var count = 0;
    for (var subject in this.grades) {
      this.grades[subject].forEach(function(grade));
      sum += grade;
      count += 1;
    }
    return sum / count;
  }
}


var dezso = new Student();
dezso.addGrade("matek", 3);
dezso.addGrade("matek", 5);
dezso.addGrade("rajz", 4);
dezso.addGrade("rajz", 1);

console.log(dezso.getCount())
