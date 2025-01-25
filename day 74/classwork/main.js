function human(name, age, ID) {
    this.name = name
    this.age = age
    this.ID = ID
}

var human_1 = new human("gela", 80, 123)
var human_2 = new human("sandro", 1, 44366)
var human_3 = new human("avtandili", 17, 838234)

console.log(human_1)
console.log(human_2)
console.log(human_3)