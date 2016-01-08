//bármilyen tantárgy lehet,

var dezso = new Student();

dezso.addGrade("matek", 2);
dezso.addGrade("matek", 3);
dezso.addGrade("rajz", 4);
dezso.addGrade("rajz", 2);
dezso.getCount() // { "rajz": 4, "matek": 2};
dezso.getAverage() //2,8
