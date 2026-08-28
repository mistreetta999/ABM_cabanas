// Funciones para manejar facturas en el frontend

// Cargar listado de facturas
function cargarFacturas() {
    fetch("/django_local/facturas/")
        .then(response => response.json())
        .then(data => {
            const tabla = document.querySelector("#tabla-facturas");
            tabla.innerHTML = "";
            data.forEach(factura => {
                tabla.innerHTML += `
                    <tr>
                        <td>${factura.id}</td>
                        <td>${factura.cliente}</td>
                        <td>${factura.monto}</td>
                        <td>${factura.estado}</td>
                        <td>
                            <button onclick="verFactura(${factura.id})">Ver</button>
                            <button onclick="marcarPagada(${factura.id})">Marcar Pagada</button>
                        </td>
                    </tr>
                `;
            });
        })
        .catch(error => console.error("Error cargando facturas:", error));
}

// Ver detalle de una factura
function verFactura(id) {
    fetch(`/django_local/facturas/${id}/`)
        .then(response => response.json())
        .then(factura => {
            alert(`Factura #${factura.id}\nCliente: ${factura.cliente}\nMonto: ${factura.monto}\nEstado: ${factura.estado}`);
        })
        .catch(error => console.error("Error al obtener factura:", error));
}

// Marcar factura como pagada
function marcarPagada(id) {
    fetch(`/django_local/facturas/${id}/`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ estado: "pagada" })
    })
    .then(response => response.json())
    .then(result => {
        alert(`✅ Factura #${id} marcada como pagada.`);
        cargarFacturas(); // refrescar listado
    })
    .catch(error => console.error("Error al marcar pagada:", error));
}

// Inicializar al cargar la página
document.addEventListener("DOMContentLoaded", cargarFacturas);
