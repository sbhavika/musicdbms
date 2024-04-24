// Sample user credentials
const validUsername = "admin";
const validPassword = "password";

// Event listener for login form submission
document.getElementById("loginForm").addEventListener("submit", function(event) {
    event.preventDefault();
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;
    if (username === validUsername && password === validPassword) {
        window.location.href = "index.html";
    } else {
        alert("Invalid username or password");
    }
});
