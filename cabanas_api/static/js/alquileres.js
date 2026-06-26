// Funciones relacionadas con alquileres
console.log("Alquileres.js cargado correctamente");

// Calcular el precio total de un alquiler
function calcularPrecioTotal(precioPorNoche, noches, descuento = 0) {
    let total = precioPorNoche * noches;
    if (descuento > 0) {
        total = total - (total * descuento / 100);
    }
    return total;
}

// Validar fechas de alquiler
function validarFechas(fechaInicio, fechaFin) {
    const inicio = new Date(fechaInicio);
    const fin = new Date(fechaFin);

    if (fin <= inicio) {
        alert("La fecha de fin debe ser posterior a la fecha de inicio");
        return false;
    }
    return true;
}

// Mostrar resumen del alquiler
function mostrarResumen(cabana, cliente, fechaInicio, fechaFin, precioTotal) {
    console.log(`Alquiler confirmado:
    Cabaña: ${cabana}
    Cliente: ${cliente}
    Desde: ${fechaInicio}
    Hasta: ${fechaFin}
    Precio total: $${precioTotal}`);
}
