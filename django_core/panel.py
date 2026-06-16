class CabañaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'capacidad', 'precio_por_noche', 'disponible')

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('dni', 'nombre', 'apellido', 'telefono', 'email')

class ReservaAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'cabaña', 'fecha_ingreso', 'fecha_salida', 'estado')

class ServicioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'precio')

class PagoAdmin(admin.ModelAdmin):
    list_display = ('reserva', 'monto', 'fecha_pago', 'metodo')
