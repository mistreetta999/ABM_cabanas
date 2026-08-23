""" archivo clientes interfaz_gestion_cabanas"""
from sqlalchemy.orm import Session
from .models import Cliente

class CrearCliente:
    """ class para crear un cliente en la base de datos """
    def __init__(self, db: Session):
        self.db = db

    def crear_cliente(self, cliente_data: dict):
        """Crea un nuevo cliente en la base de datos."""
        nuevo_cliente = Cliente(**cliente_data)
        self.db.add(nuevo_cliente)
        self.db.commit()
        self.db.refresh(nuevo_cliente)
        return nuevo_cliente
class GuardarCliente:
    """ class para guardar un cliente en la base de datos """
    def __init__(self, db: Session):
        self.db = db

    def guardar_cliente(self, cliente: Cliente):
        """Guarda un cliente existente en la base de datos."""
        self.db.add(cliente)
        self.db.commit()
        self.db.refresh(cliente)
        return cliente
class ObtenerCliente:
    """ class para obtener un cliente en la base de datos """
    def __init__(self, db: Session):
        self.db = db

    def obtener_cliente(self, cliente_id: int):
        """Obtiene un cliente por su ID."""
        return self.db.query(Cliente).filter(Cliente.id == cliente_id).first()
class ActualizarCliente:
    """ class para actualizar un cliente en la base de datos """
    def __init__(self, db: Session):
        self.db = db

    def actualizar_cliente(self, cliente_id: int, cliente_data: dict):
        """Actualiza un cliente existente en la base de datos."""
        cliente = self.db.query(Cliente).filter(Cliente.id == cliente_id).first()
        if cliente:
            for key, value in cliente_data.items():
                setattr(cliente, key, value)
            self.db.commit()
            self.db.refresh(cliente)
        return cliente

class EliminarCliente:

    """ class para eliminar un cliente en la base de datos """
    def __init__(self, db: Session):
        self.db = db

    def eliminar_cliente(self, cliente_id: int):
        """Elimina un cliente por su ID."""
        cliente = self.db.query(Cliente).filter(Cliente.id == cliente_id).first()
        if cliente:
            self.db.delete(cliente)
            self.db.commit()
        return cliente
    


def boton (self)->Any:
    """Genera botones de acción para la Cabanas
 en el admin."""
    editar = reverse('admin:cabanas_cabana_change', args=[self.pk])
    eliminar = reverse('admin:cabanas_cabana_delete', args=[self.pk])
    crear = reverse('admin:cabanas_cabana_add')
    imprimir = reverse('admin:cabanas_cabana_print', args=[self.pk])
    buscar = reverse('admin:cabanas_cabana_changelist')
    salir = reverse('admin:index')
    return boton
