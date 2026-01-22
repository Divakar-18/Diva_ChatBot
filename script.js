const chatBox = document.getElementById("chat-box");
let lastAnswer = null;

function addMessage(text, sender) {
    const msg = document.createElement("div");
    msg.className = sender;
    msg.innerText = text;
    chatBox.appendChild(msg);
    chatBox.scrollTop = chatBox.scrollHeight;
}

async function sendMessage() {
    const input = document.getElementById("user-input");
    const message = input.value.trim();

    if (!message) return;

    addMessage(message, "user");
    input.value = "";

    const response = await fetch("http://localhost:5000/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            message: message,
            last_answer: lastAnswer
        })
    });

    const data = await response.json();
    lastAnswer = data.reply;

    addMessage(data.reply, "bot");
}
