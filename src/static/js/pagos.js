/ /pago.js - Payments app features
document.addEventListener("DOMContentLoaded", function() {
    const metodo = document.getElementById("metodoPago");
    if (metodo) {
        metodo.addEventListener("change", function() {
            alert("Método de pago seleccionado: " + metodo.value);
        });
    }
});
