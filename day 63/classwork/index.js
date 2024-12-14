const counterElement = document.getElementById("counter");
const decrementButton = document.getElementById("decrement");
const incrementButton = document.getElementById("increment");
const resetButton = document.getElementById("reset");
const plusValue = prompt();
const minusValue = prompt();
let increment = Number(plusValue);
let decrement = Number(minusValue);




let count = 0;

decrementButton.addEventListener("click", () => {
  count -= decrement;
  counterElement.textContent = count;
});

incrementButton.addEventListener("click", () => {
  count += increment;
  counterElement.textContent = count;
});

resetButton.addEventListener("click", () => {
  count = 0;
  counterElement.textContent = count;
});
