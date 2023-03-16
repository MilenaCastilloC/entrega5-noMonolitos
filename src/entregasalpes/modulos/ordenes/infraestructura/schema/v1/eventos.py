from pulsar.schema import *
from entregasalpes.seedwork.infraestructura.schema.v1.eventos import EventoIntegracion
# from entregasalpes.seedwork.infraestructura.utils import time_millis
# import uuid

class OrdenCreadaPayload(Record):
    id_orden = String()
    id_cliente = String()
    estado = String()
    fecha_creacion = Long()

class EventoOrdenCreada(EventoIntegracion):
    # NOTE La librería Record de Pulsar no es capaz de reconocer campos heredados, 
    # por lo que los mensajes al ser codificados pierden sus valores
    # Dupliqué el los cambios que ya se encuentran en la clase Mensaje
    
    data = OrdenCreadaPayload()

class EventoEjecutaSaga(EventoDominio):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)