function human(name, age, ID) {
    this.name = name
    this.age = age
    this.ID = ID
}

var human_1 = new human("gela", 80, 123)
var human_2 = new human("sandro", 1, 44366)
var human_3 = new human("avtandili", 17, 838234)




function car(name, year, engine, HP, color, human) {
    this.name = name
    this.year = year
    this.engine = engine
    this.HP = HP
    this.color = color
    this.human = human

}
var car1 = new car("lamborgini", 2015, "idk", 150, "black", human_1)
var car2 = new car("tesla", 2020, "electro", 100, "white", human_2)
var car3 = new car("jiguli", 1990, "dizel", 50, "blue", human_3)




console.log(car1)
console.log(car2)
console.log(car3)