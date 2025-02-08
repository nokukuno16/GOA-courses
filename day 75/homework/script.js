function car(brand, model, year, engineVolume) {
    this.brand = brand;
    this.model = model;
    this.year = year;
    this.engineVolume = engineVolume;
    this.Return = function(Return) {
        console.log(brand, model, year, engineVolume)
    }
}

var carInput = new car("Toyota", "rav4", 2008, 100)
carInput.Return(carInput)


function book(title, author, pages, year) {
    this.title = title;
    this.author = author;
    this.pages = pages;
    this.year = year;
    this.bookInformation = function(bookInformation) {
        console.log(title, author, pages, year)
    }
}

var bookInput = new book("me bebia iliko da ilarioni", "nodar dumbadze", 200, 1957)

bookInput.bookInformation(bookInput)





function Athlete(name, age, sport, trainingHours) {
    return {
        name: name,
        age: age,
        sport: sport,
        trainingHours: trainingHours,
        weeklyTrainingNeeded: function (WeeklyTrainingNeeded) {
            console.log(name, age, sport, trainingHours)
        }
    };
}


var athlete = Athlete("გიორგი", 22, "ფეხბურთი", 2);
athlete.weeklyTrainingNeeded(athlete)