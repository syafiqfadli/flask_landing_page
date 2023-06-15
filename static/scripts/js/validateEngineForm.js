function validateEngineForm() {
    var letters = /^[A-Za-z]+$/;
    var inputText = document.getElementById("form-input").value;

    if (inputText == ""){
        alert("Please do not leave input empty.");
        return false;
    }

    if (inputText.match(letters))
    {
        alert("Please enter numbers only");
        return false;
    }
}