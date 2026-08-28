// Script para manejar interacción con el chatbot

function enviarMensaje() {
    const mensaje = document.querySelector("#chat-input").value;
    fetch("/chatbot/send/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ mensaje: mensaje })
    })
    .then(response => response.json())
    .then(data => {
        const chatBox = document.querySelector("#chat-box");
        chatBox.innerHTML += `<p><strong>Tú:</strong> ${mensaje}</p>`;
        chatBox.innerHTML += `<p><strong>Bot:</strong> ${data.respuesta}</p>`;
    })
    .catch(error => console.error("Error:", error));
}
