// clientes.js - Features for the customer app
function validarFormularioCliente() {
    const dni = document.getElementById("dni");
    if (dni && dni.value.length < 7) {
        alert("El DNI debe tener al menos 7 dígitos.");
        return false;
    }
    return true;
}

document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById("formCliente");
    if (form) {
        form.addEventListener("submit", function(e) {
            if (!validarFormularioCliente()) {
                e.preventDefault();
            }
        });
    }
});
