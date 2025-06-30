async function sendToBot() {

    const input = document.getElementById("msg-box");
    const chatArea = document.getElementById("message-area");

    const userMsg = input.value.trim();

    if (!userMsg) return;

    const userDiv = document.createElement("div");
    userDiv.textContent = "You: " + userMsg;
    chatArea.appendChild(userDiv);

    input.value = "";

    const typingDiv = document.createElement("div");
    typingDiv.textContent = "Bot is typing...";
    chatArea.appendChild(typingDiv);

    chatArea.scrollTop = chatArea.scrollHeight;

    try {
        const res = await fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            message: userMsg,
            lang: "en"  
        })

    });

    const data = await res.json();

    typingDiv.remove();

    const botDiv = document.createElement("div");
    botDiv.textContent = "Bot: " + data.reply;
    chatArea.appendChild(botDiv);

    chatArea.scrollTop = chatArea.scrollHeight;

  } catch (error) {
    typingDiv.remove();

    const errorDiv = document.createElement("div");
    errorDiv.textContent = "⚠️ Bot failed to reply. Please try again.";
    chatArea.appendChild(errorDiv);
  }
}
