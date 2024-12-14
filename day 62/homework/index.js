const userInput = prompt();
let b = "";

for (let i = 0; i < userInput.length; i++) {
  let char = userInput[i];

  if (char >= "0" && char <= "9") {
    console.log("error");
  } else {
    b += char;
    if(b === userInput){
        console.log("წარმატებული ოპერაცია");
    } else {
        console.log("error")
    }
  }
}