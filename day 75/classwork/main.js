function animal_cat(height, type) {
    this.height = height;
    this.type = type;
    this.willDie = function(age) {
        if (age > 7 && type == "cat") {
            console.log("soon")
        }else {
            console.log("your cat have time")
        }
    }
}
 
var anim = new animal_cat(12, "cat")
anim.willDie(5);
