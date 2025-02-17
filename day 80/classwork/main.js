function sumOfDigits(num) {
    let sum = 0;
    let numStr = num.toString();
    for (let i = 0; i < numStr.length; i++) {
        sum += parseInt(numStr[i], 10);
    }
    return sum;
}

// Example usage:
console.log(sumOfDigits(1234)); // Output: 10