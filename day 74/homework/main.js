function student(name, age, ID) {
    this.name = name
    this.age = age
    this.ID = ID
}

var student_1 = new student("rostevani", 10, 13623)
var student_2 = new student("luarsabi", 12, 44366)
var student_3 = new student("neimari", 17, 838234)

function animal(type, name, age, owner) {
    this.type = type
    this.name = name
    this.age = age
    this.owner = owner
}

var animal_1 = new animal("dog", "rex", 5, student_1)
var animal_2 = new animal("cat", "mimi", 2, student_2)
var animal_3 = new animal("bird", "tweety", 1, student_3)


function car(model, year, engine, HP, color, owner) {
    this.model = model
    this.year = year
    this.engine = engine
    this.HP = HP
    this.color = color
    this.owner = owner

}

var car_1 = new car("lamborgini", 2015, "idk", 150, "black", student_1)
var car_2 = new car("tesla", 2020, "electro", 100, "white", student_2)
var car_3 = new car("jiguli", 1990, "dizel", 50, "blue", student_3)

console.log(animal_1, car_1)
console.log(animal_2, car_2)
console.log(animal_3, car_3)