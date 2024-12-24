document.getElementById('submitButton').addEventListener('click', () => {
    // ველების მნიშვნელობების მიღება
    const firstName = document.getElementById('firstName').value.trim();
    const lastName = document.getElementById('lastName').value.trim();
    const email = document.getElementById('email').value.trim();
    const password = document.getElementById('password').value.trim();
    const terms = document.getElementById('terms').checked;

    // ველების შემოწმება
    if (!firstName || !lastName || !email || !password || !terms) {
        alert('გთხოვთ, შეავსოთ ყველა ველი');
        return;
    }

    // ვალიდური მონაცემების კონსოლში გამოტანა
    console.log('მომხმარებლის მონაცემები:');
    console.log(`სახელი: ${firstName}`);
    console.log(`გვარი: ${lastName}`);
    console.log(`ელფოსტა: ${email}`);
    console.log(`პაროლი: ${password}`);
    console.log('წესებს და პირობებს ეთანხმება');
});
