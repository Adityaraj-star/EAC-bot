function sendToBot() {
    let inputBox = document.getElementById("msg-box");
    let messageText = inputBox.value.trim();
    let messageArea = document.getElementById("message-area");

    if (messageText === "") return;

    let userDiv = document.createElement("div");
    userDiv.textContent = "You: " + messageText;
    messageArea.appendChild(userDiv);
    inputBox.value = "";
}
