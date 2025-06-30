const emotionEmoji = {

    happy: "😊",
    sad: "😢",
    angry: "😠",
    neutral: "😐"
};

async function sendToBot() {

    const input = document.getElementById("msg-box");
    const chatArea = document.getElementById("message-area");
    const selectedLang = document.getElementById("lang").value;

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
            lang: selectedLang 
        })

    });

    const data = await res.json();

    typingDiv.remove();

    const emotion = data.emotion;
    const emoji = emotionEmoji[emotion] || "";

    const botDiv = document.createElement("div");
    botDiv.textContent = `Bot: ${data.reply} ${emoji}`;
    botDiv.classList.add("bot", emotion);
    chatArea.appendChild(botDiv);


    chatArea.scrollTop = chatArea.scrollHeight;

  } catch (error) {
    typingDiv.remove();

    const errorDiv = document.createElement("div");
    errorDiv.textContent = "❌ Error: Could not get response from bot.";
    chatArea.appendChild(errorDiv);
  }
}
