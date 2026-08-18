-- Listados principales del sistema de gestion de cabanas.
-- Base usada: SQLite / Django.
-- Tablas:
--   reservas_cliente
--   reservas_reserva
--   reservas_alquiler
--   reservas_pago
--   reservas_cabana


-- 1. LISTADO DE CLIENTES
SELECT
    id,
    nombre_apellido,
    dni,
    direccion,
    telefono,
    ingreso,
    salida
FROM reservas_cliente
ORDER BY nombre_apellido;


-- 2. LISTADO DE RESERVAS
SELECT
    r.id AS reserva_id,
    c.nombre_apellido AS cliente,
    c.dni,
    ca.nombre AS Cabanas
,
    r.fecha_inicio,
    r.fecha_fin,
    r.estado
FROM reservas_reserva AS r
INNER JOIN reservas_cliente AS c
    ON c.id = r.cliente_id
INNER JOIN reservas_cabana AS ca
    ON ca.id = r.cabana_id
ORDER BY r.fecha_inicio DESC;


-- 3. LISTADO DE ALQUILERES
SELECT
    a.id AS alquiler_id,
    c.nombre_apellido AS cliente,
    c.dni,
    ca.nombre AS Cabanas
,
    a.fecha_inicio,
    a.fecha_fin,
    a.estado
FROM reservas_alquiler AS a
INNER JOIN reservas_cliente AS c
    ON c.id = a.cliente_id
INNER JOIN reservas_cabana AS ca
    ON ca.id = a.cabana_id
ORDER BY a.fecha_inicio DESC;


-- 4. LISTADO DE PAGOS
SELECT
    p.id AS pago_id,
    p.fecha_pago,
    p.monto,
    p.metodo_pago,
    r.id AS reserva_id,
    c.nombre_apellido AS cliente,
    c.dni,
    ca.nombre AS Cabanas
,
    r.fecha_inicio,
    r.fecha_fin,
    r.estado
FROM reservas_pago AS p
INNER JOIN reservas_reserva AS r
    ON r.id = p.reserva_id
INNER JOIN reservas_cliente AS c
    ON c.id = r.cliente_id
INNER JOIN reservas_cabana AS ca
    ON ca.id = r.cabana_id
ORDER BY p.fecha_pago DESC;


-- 5. LISTADO DE CABANAS
SELECT
    id,
    nombre,
    descripcion,
    capacidad,
    precio_por_noche,
    disponible,
    fecha_creacion,
    fecha_actualizacion
FROM reservas_cabana
ORDER BY nombre;


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
SELECT
    a.id AS alquiler_id,
    c.nombre_apellido AS cliente,
    c.dni,
    c.telefono,
    ca.nombre AS Cabanas
,
    a.fecha_inicio AS llegada,
    a.fecha_fin AS salida,
    a.estado
FROM reservas_alquiler AS a
INNER JOIN reservas_cliente AS c
    ON c.id = a.cliente_id
INNER JOIN reservas_cabana AS ca
    ON ca.id = a.cabana_id
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
    ca.nombre AS Cabanas
,
    a.fecha_fin AS salida,
    a.estado
FROM reservas_alquiler AS a
INNER JOIN reservas_cliente AS c
    ON c.id = a.cliente_id
INNER JOIN reservas_cabana AS ca
    ON ca.id = a.cabana_id
WHERE a.fecha_fin = '2026-05-14'
ORDER BY salida, cliente;
