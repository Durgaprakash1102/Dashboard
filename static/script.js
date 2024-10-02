// script.js
document.addEventListener("DOMContentLoaded", function() {
    fetch('http://127.0.0.1:8000/some_api_endpoint/')
        .then(response => response.json())
        .then(data => {
            document.getElementById('content').innerText = JSON.stringify(data);
        })
        .catch(error => console.error('Error:', error));
});