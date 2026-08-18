// Funciones relacionadas con reservas
console.log("Reservas.js cargado correctamente");

function calcularDias(fechaInicio, fechaFin) {
    const pagina_principal = new Date(fechaInicio);
    const fin = new Date(fechaFin);
    const diferencia = (fin - pagina_principal) / (1000 * 60 * 60 * 24);
    return diferencia;
}
