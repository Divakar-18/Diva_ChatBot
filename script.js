const chatBox = document.getElementById("chat-box");
const typing = document.getElementById("typing");
let lastAnswer = null;

function addMessage(text, sender) {
    const msg = document.createElement("div");
    msg.classList.add("message", sender);
    msg.innerHTML = text;
    chatBox.appendChild(msg);
    chatBox.scrollTop = chatBox.scrollHeight;
}

async function sendMessage() {
    const input = document.getElementById("user-input");
    const message = input.value.trim();

    if (!message) return;

    addMessage(message, "user");
    input.value = "";

    typing.style.display = "block";

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

    setTimeout(() => {
        typing.style.display = "none";
        addMessage(data.reply, "bot");
    }, 800); // typing delay
}

/* Enter key support */
document.getElementById("user-input").addEventListener("keypress", function (e) {
    if (e.key === "Enter") {
        sendMessage();
    }
});
