const counterElement = document.getElementById("counter");
const decrementButton = document.getElementById("decrement");
const incrementButton = document.getElementById("increment");
const resetButton = document.getElementById("reset");

let count = 0;

decrementButton.addEventListener("click", () => {
  count--;
  counterElement.textContent = count;
});

incrementButton.addEventListener("click", () => {
  count++;
  counterElement.textContent = count;
});

resetButton.addEventListener("click", () => {
  count = 0;
  counterElement.textContent = count;
});
