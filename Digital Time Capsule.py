<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Digital Time Capsule</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #f0f0f0;
            margin: 0;
        }
        .container {
            background-color: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
            width: 400px;
        }
        h1 {
            text-align: center;
        }
        textarea {
            width: 100%;
            height: 100px;
            margin-bottom: 10px;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
        input[type="datetime-local"] {
            width: 100%;
            padding: 10px;
            margin-bottom: 10px;
            border-radius: 5px;
            border: 1px solid #ccc;
        }
        button {
            width: 100%;
            padding: 10px;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        button:hover {
            background-color: #45a049;
        }
        .message {
            margin-top: 20px;
            text-align: center;
            font-size: 18px;
            font-weight: bold;
            color: #333;
        }
    </style>
</head>
<body>

<div class="container">
    <h1>Digital Time Capsule</h1>
    <textarea id="message" placeholder="Write your message..."></textarea><br>
    <input type="datetime-local" id="revealTime"><br>
    <button onclick="storeMessage()">Store Message</button>
    <div id="messageBox" class="message"></div>
</div>

<script>
    function storeMessage() {
        const message = document.getElementById("message").value;
        const revealTime = new Date(document.getElementById("revealTime").value).getTime();
        const currentTime = new Date().getTime();

        if (!message || !revealTime) {
            alert("Please fill in both the message and the reveal time.");
            return;
        }

        if (revealTime <= currentTime) {
            alert("Please set a reveal time in the future.");
            return;
        }

        localStorage.setItem('timeCapsuleMessage', message);
        localStorage.setItem('revealTime', revealTime);

        setTimeout(function() {
            displayMessage();
        }, revealTime - currentTime);
        
        alert("Your message has been stored and will be revealed at the set time.");
    }

    function displayMessage() {
        const message = localStorage.getItem('timeCapsuleMessage');
        const messageBox = document.getElementById("messageBox");
        messageBox.innerHTML = "Your Time Capsule Message: " + message;
    }

    window.onload = function() {
        const revealTime = localStorage.getItem('revealTime');
        const currentTime = new Date().getTime();
        if (revealTime && currentTime >= revealTime) {
            displayMessage();
        }
    };
</script>

</body>
</html>
