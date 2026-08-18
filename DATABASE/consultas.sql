-- Consultas de tablas cruzadas para el sistema de gestion de cabanas.
-- Base usada: SQLite / Django.
-- Tablas principales:
--   reservas_cliente: clientes
--   reservas_reserva: reservas
--   reservas_pago: pagos
--   reservas_cabana: cabanas


-- 1. CLIENTES + PAGOS
-- Muestra cada pago con los datos del cliente, la reserva y la Cabanas
.
SELECT
    c.id AS cliente_id,
    c.nombre_apellido AS cliente,
    c.dni,
    c.telefono,
    r.id AS reserva_id,
    ca.nombre AS Cabanas
,
    r.fecha_inicio,
    r.fecha_fin,
    r.estado,
    p.id AS pago_id,
    p.fecha_pago,
    p.monto,
    p.metodo_pago
FROM reservas_cliente AS c
INNER JOIN reservas_reserva AS r
    ON r.cliente_id = c.id
INNER JOIN reservas_pago AS p
    ON p.reserva_id = r.id
INNER JOIN reservas_cabana AS ca
    ON ca.id = r.cabana_id
ORDER BY p.fecha_pago DESC, c.nombre_apellido;


-- 2. CLIENTES + RESERVAS
-- Muestra las reservas realizadas por cada cliente.
SELECT
    c.id AS cliente_id,
    c.nombre_apellido AS cliente,
    c.dni,
    c.telefono,
    r.id AS reserva_id,
    ca.nombre AS Cabanas
,
    r.fecha_inicio,
    r.fecha_fin,
    r.estado
FROM reservas_cliente AS c
INNER JOIN reservas_reserva AS r
    ON r.cliente_id = c.id
INNER JOIN reservas_cabana AS ca
    ON ca.id = r.cabana_id
ORDER BY r.fecha_inicio DESC, c.nombre_apellido;


-- 3. CLIENTES + LLEGADAS
-- Usa fecha_inicio como fecha de llegada.
SELECT
    c.id AS cliente_id,
    c.nombre_apellido AS cliente,
    c.dni,
    c.telefono,
    r.id AS reserva_id,
    ca.nombre AS Cabanas
,
    r.fecha_inicio AS fecha_llegada,
    r.fecha_fin AS fecha_salida,
    r.estado
FROM reservas_cliente AS c
INNER JOIN reservas_reserva AS r
    ON r.cliente_id = c.id
INNER JOIN reservas_cabana AS ca
    ON ca.id = r.cabana_id
ORDER BY r.fecha_inicio ASC, c.nombre_apellido;


-- 4. CLIENTES + SALIDAS
-- Usa fecha_fin como fecha de salida.
SELECT
    c.id AS cliente_id,
    c.nombre_apellido AS cliente,
    c.dni,
    c.telefono,
    r.id AS reserva_id,
    ca.nombre AS Cabanas
,
    r.fecha_inicio AS fecha_llegada,
    r.fecha_fin AS fecha_salida,
    r.estado
FROM reservas_cliente AS c
INNER JOIN reservas_reserva AS r
    ON r.cliente_id = c.id
INNER JOIN reservas_cabana AS ca
    ON ca.id = r.cabana_id
ORDER BY r.fecha_fin ASC, c.nombre_apellido;


-- 5. RESUMEN POR CLIENTE
-- Cantidad de reservas, cantidad de pagos y total pagado por cliente.
SELECT
    c.id AS cliente_id,
    c.nombre_apellido AS cliente,
    c.dni,
    COUNT(DISTINCT r.id) AS cantidad_reservas,
    COUNT(p.id) AS cantidad_pagos,
    COALESCE(SUM(p.monto), 0) AS total_pagado
FROM reservas_cliente AS c
LEFT JOIN reservas_reserva AS r
    ON r.cliente_id = c.id
LEFT JOIN reservas_pago AS p
    ON p.reserva_id = r.id
GROUP BY
    c.id,
    c.nombre_apellido,
    c.dni
ORDER BY total_pagado DESC, c.nombre_apellido;


-- 6. INFORME DIARIO
-- Cambiar la fecha '2026-05-14' por el dia que se quiera consultar.

-- Reservas que ingresan en el dia.
SELECT
    r.id AS reserva_id,
    c.nombre_apellido AS cliente,
    c.dni,
    c.telefono,
    ca.nombre AS Cabanas
,
    r.fecha_inicio AS llegada,
    r.fecha_fin AS salida,
    r.estado
FROM reservas_reserva AS r
INNER JOIN reservas_cliente AS c
    ON c.id = r.cliente_id
INNER JOIN reservas_cabana AS ca
    ON ca.id = r.cabana_id
WHERE r.fecha_inicio = '2026-05-14'
ORDER BY c.nombre_apellido;

-- Alquileres que ingresan en el dia.
-- Si existe la tabla intermedia alquileres_cabanias, usarla para obtener las cabanas asociadas.
SELECT
    a.id AS alquiler_id,
    c.nombre_apellido AS cliente,
    c.dni,
    c.telefono,
    COALESCE(ca_intermedia.nombre, ca.nombre) AS Cabanas
,
    a.fecha_inicio AS llegada,
    a.fecha_fin AS salida,
    a.estado
FROM reservas_alquiler AS a
INNER JOIN reservas_cliente AS c
    ON c.id = a.cliente_id
INNER JOIN reservas_cabana AS ca
    ON ca.id = a.cabana_id
LEFT JOIN alquileres_cabanias AS ac
    ON ac.id_Alquileres = a.id
LEFT JOIN reservas_cabana AS ca_intermedia
    ON ca_intermedia.id = ac.id_Cabanas
WHERE a.fecha_inicio = '2026-05-14'
ORDER BY c.nombre_apellido;

-- Pagos registrados en el dia.
SELECT
    p.id AS pago_id,
    p.fecha_pago,
    c.nombre_apellido AS cliente,
    c.dni,
    ca.nombre AS Cabanas
,
    p.metodo_pago,
    p.monto
FROM reservas_pago AS p
INNER JOIN reservas_reserva AS r
    ON r.id = p.reserva_id
INNER JOIN reservas_cliente AS c
    ON c.id = r.cliente_id
INNER JOIN reservas_cabana AS ca
    ON ca.id = r.cabana_id
WHERE p.fecha_pago = '2026-05-14'
ORDER BY p.fecha_pago DESC, c.nombre_apellido;

-- Salidas del dia, unificando reservas y alquileres.
SELECT
    'Reserva' AS tipo,
    r.id AS operacion_id,
    c.nombre_apellido AS cliente,
    c.dni,
    c.telefono,
    ca.nombre AS Cabanas
,
    r.fecha_fin AS salida,
    r.estado
FROM reservas_reserva AS r
INNER JOIN reservas_cliente AS c
    ON c.id = r.cliente_id
INNER JOIN reservas_cabana AS ca
    ON ca.id = r.cabana_id
WHERE r.fecha_fin = '2026-05-14'

UNION ALL

SELECT
    'Alquiler' AS tipo,
    a.id AS operacion_id,
    c.nombre_apellido AS cliente,
    c.dni,
    c.telefono,
    COALESCE(ca_intermedia.nombre, ca.nombre) AS Cabanas
,
    a.fecha_fin AS salida,
    a.estado
FROM reservas_alquiler AS a
INNER JOIN reservas_cliente AS c
    ON c.id = a.cliente_id
INNER JOIN reservas_cabana AS ca
    ON ca.id = a.cabana_id
LEFT JOIN alquileres_cabanias AS ac
    ON ac.id_Alquileres = a.id
LEFT JOIN reservas_cabana AS ca_intermedia
    ON ca_intermedia.id = ac.id_Cabanas
WHERE a.fecha_fin = '2026-05-14'
ORDER BY salida, cliente;
