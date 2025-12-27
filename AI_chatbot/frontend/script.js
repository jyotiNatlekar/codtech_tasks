let lastQuestion = "";

function addMessage(sender, text) {
    const box = document.getElementById("chat-box");
    box.innerHTML += `<p><b>${sender}:</b> ${text}</p>`;
    box.scrollTop = box.scrollHeight;
}

function sendMessage() {
    const input = document.getElementById("user-input");
    const message = input.value;
    input.value = "";

    addMessage("You", message);
    lastQuestion = message;

    fetch("http://127.0.0.1:5000/chat", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({message})
    })
    .then(res => res.json())
    .then(data => {
        addMessage("Bot", data.reply);

        if (data.learn) {
            const answer = prompt("Teach me the correct answer:");
            fetch("http://127.0.0.1:5000/teach", {
                method: "POST",
                headers: {"Content-Type": "application/json"},
                body: JSON.stringify({
                    question: lastQuestion,
                    answer: answer
                })
            })
            .then(res => res.json())
            .then(data => addMessage("Bot", data.reply));
        }
    });
}
