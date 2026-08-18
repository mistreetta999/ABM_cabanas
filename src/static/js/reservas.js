/ /reservas.js - Booking app features
function calcularTotal() {
    const dias = document.getElementById("dias");
    const precio = document.getElementById("precio");
    const total = document.getElementById("total");

    if (dias && precio && total) {
        let resultado = parseInt(dias.value || 0) * parseFloat(precio.value || 0);
        total.textContent = "Total: $" + resultado.toFixed(2);
    }
}

document.addEventListener("DOMContentLoaded", function() {
    const dias = document.getElementById("dias");
    const precio = document.getElementById("precio");

    if (dias && precio) {
        dias.addEventListener("input", calcularTotal);
        precio.addEventListener("input", calcularTotal);
    }
});
