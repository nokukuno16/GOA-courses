function checkAge() {
    let name = document.getElementById('name').value;
    let surname = document.getElementById('surname').value;
    let age = document.getElementById('age').value;

    let result = age >= 18 
        ? `მოგესალმებით, ${name} ${surname}, თქვენ სრულწლოვანი ხართ` 
        : `${name} ${surname}, თქვენ ვერ გამოიყენებთ ამ პროგრამას.`;

    document.getElementById('result').textContent = result;
}