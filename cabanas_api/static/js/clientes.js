// Funciones relacionadas con clientes
console.log("Clientes.js cargado correctamente");

function validarCliente(nombre, email) {
    if (!nombre || !email) {
        alert("Nombre y email son obligatorios");
        return false;
    }
    return true;
}
