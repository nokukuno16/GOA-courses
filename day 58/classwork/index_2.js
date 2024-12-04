document.getElementById("submitButton").addEventListener("click", function() {
    const firstName = document.getElementById("firstName").value;
    const lastName = document.getElementById("lastName").value;
    const checkboxStatus = document.getElementById("agreeCheckbox").checked;

    console.log("სახელი:", firstName);
    console.log("გვარი:", lastName);
    console.log("Checkbox სტატუსი:", checkboxStatus);
});