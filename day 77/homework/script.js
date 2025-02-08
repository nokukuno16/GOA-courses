function arrayToObject(keys, values) {
    var obj = {};
    for (var i = 0; i < keys.length; i++) {
        if (values[i] !== undefined) {
            obj[keys[i]] = values[i];  
        } else {
            obj[keys[i]] = null;
        }
    }
    return obj; 
}


var result = arrayToObject(["name", "age", "city"], ["John", 25, "California"]);
console.log(result);

