"use strict";

for (var i = 1; i < 11 ; i++) {
  console.log(i)
}



var dogs = ["berni", "tacskó", "pincs"]

for (var i = 0; i < dogs.length; i++) {
  console.log(dogs[i])
}


//csak objektumra!
var student = {
  kor: 12,
  name:"csaba",
  labmeret: 45
};

for (var key in student) {
console.log(student[key]);
}
