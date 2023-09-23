const chatMessages = document.getElementById('chatMessages');
const userInput = document.getElementById('userInput');
const sendButton = document.getElementById('sendButton');
const fileUpload = document.getElementById('fileUpload');
const typingIndicator = document.getElementById('typingIndicator');

sendButton.addEventListener('click', function () {
    const userMessage = userInput.value.trim();

    if (userMessage !== "") {
        displayUserMessage(userMessage);
        sendMessageToServer(userMessage);
    }
});

function displayUserMessage(message) {
    // Create and display a div for the user's message
    let userMessageDiv = document.createElement('div');
    userMessageDiv.className = 'message user-message';
    userMessageDiv.textContent = message;
    chatMessages.appendChild(userMessageDiv);
    chatMessages.scrollTop = chatMessages.scrollHeight;

    // Clear the user input field
    userInput.value = '';
}

function sendMessageToServer(message) {
    // Show the typing indicator
    typingIndicator.style.display = 'block';

    console.log("Sending message to server:", message);
    fetch('http://127.0.0.1:5000/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ message: message })
    })
        .then(response => response.json())
        .then(handleServerResponse)
        .catch(handleError);
}

function handleServerResponse(data) {
    // Hide the typing indicator
    typingIndicator.style.display = 'none';

    // Create and display a div for the server's response
    let serverResponseDiv = document.createElement('div');
    serverResponseDiv.className = 'message server-response';
    serverResponseDiv.textContent = data.response;
    chatMessages.appendChild(serverResponseDiv);
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

function handleError(error) {
    console.error('Error:', error);
    typingIndicator.style.display = 'none';
}


userInput.addEventListener('keydown', function (e) {
    if (e.key === "Enter" && !e.shiftKey) {  // Checks if the pressed key is "Enter" and ensures "Shift" is not pressed (useful if you want Shift+Enter for a new line)
        e.preventDefault();  // Prevents any default action associated with the "Enter" key press
        sendButton.click();  // Triggers the sendButton's click event
    }
});

document.getElementById('uploadButton').addEventListener('click', function () {
    const file = document.getElementById('fileInput').files[0];
    const filePreviewContainer = document.getElementById('filePreview');
    const selectedFileName = this.file[0] ? this.file[0].name : 'No file chosen';

    document.getElementById('fileName').textContent = selectedFileName;

    if (file) {
        // If you want to preview the file before sending
        // This example only handles images for preview
        if (file.type.startsWith('image/')) {
            const fileReader = new FileReader();
            fileReader.onload = function (event) {
                const imgElement = document.createElement('img');
                imgElement.src = event.target.result;
                filePreviewContainer.appendChild(imgElement);
            };
            fileReader.readAsDataURL(file);
        } else {
            // For non-image files, you can simply show the filename or some icon
            filePreviewContainer.textContent = file.name;
        }

        // Sending the file to the Flask server
        let formData = new FormData();
        formData.append('file', file);

        fetch('http://127.0.0.1:5000/upload', {
            method: 'POST',
            body: formData
        })
            .then(response => response.json())
            .then(data => {
                console.log(data);  // Handle the server's response here
            })
            .catch(error => {
                console.error('Error:', error);
            });
    } else {
        alert("No file selected!");
    }
});

