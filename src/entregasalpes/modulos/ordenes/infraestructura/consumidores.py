import pulsar,_pulsar  
from pulsar.schema import *
import uuid
import time
import logging
import traceback

from entregasalpes.modulos.ordenes.infraestructura.schema.v1.eventos import EventoOrdenCreada, EventoEjecutaSaga
from entregasalpes.modulos.ordenes.infraestructura.schema.v1.comandos import ComandoCrearOrden
from entregasalpes.seedwork.infraestructura import utils
from entregasalpes.seedwork.dominio.eventos import EventoDominio
from entregasalpes.modulos.ordenes.aplicacion.comandos.crear_orden import CrearOrden
from entregasalpes.seedwork.aplicacion.comandos import ejecutar_commando

from entregasalpes.modulos.ordenes.dominio.eventos import OrdenCreada
from entregasalpes.seedwork.infraestructura.schema.v1.mensajes import Mensaje
from entregasalpes.modulos.sagas.aplicacion.coordinadores.saga_orden import CoordinadorOrdenes

def suscribirse_a_eventos():
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('eventos-orden', consumer_type=_pulsar.ConsumerType.Shared,subscription_name='entregasalpes-sub-eventos', schema=AvroSchema(EventoOrdenCreada))

        while True:
            mensaje = consumidor.receive()
            print(f'Evento recibido: {mensaje.value().data}')
            consumidor.acknowledge(mensaje)

        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de eventos!')
        traceback.print_exc()
        if cliente:
            cliente.close()

def suscribirse_a_comandos():
    cliente = None
    try:
        cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
        consumidor = cliente.subscribe('comandos-orden', consumer_type=_pulsar.ConsumerType.Shared, subscription_name='entregasalpes-sub-comandos', schema=AvroSchema(ComandoCrearOrden))

        while True:
            mensaje = consumidor.receive()
            valor = mensaje.value()
            print(f'Comando recibido: {mensaje.value().data}')
            fecha_creacion = utils.millis_a_datetime(valor.data.fecha_creacion)
            fecha_actualizacion = utils.millis_a_datetime(valor.data.fecha_actualizacion)

            id = str(uuid.uuid4())
            try:
                with app.test_request_context():
                    comando = CrearOrden(fecha_creacion, fecha_actualizacion, id)
                    ejecutar_commando(comando)
            except:
                logging.error('ERROR: Procesando eventos!')
                traceback.print_exc()

            consumidor.acknowledge(mensaje)
            
        cliente.close()
    except:
        logging.error('ERROR: Suscribiendose al tópico de comandos!')
        traceback.print_exc()
        if cliente:
            cliente.close()


def oir_mensaje(mensaje):
    if isinstance(mensaje, EventoDominio):
        coordinador = CoordinadorOrdenes()
        coordinador.inicializar_pasos()
        coordinador.procesar_evento(mensaje)
    else:
        raise NotImplementedError("El mensaje no es un evento de dominio")

    def_subscribirse_ejecutar_saga(app=None):
        cliente = None
        try:
            cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
            consumidor = cliente.subscribe('ejecutar-saga', consumer_type=_pulsar.ConsumerType.Shared, subscription_name='entregasalpes-sub-comandos-orden', schema=AvroSchema(ComandoCrearOrden))

            while: True

            mensaje = consumidor.receive()
            print(f'Evento recibido: {mensaje.value().data}')

            order = OrdenCreada(id="abc01abc02", id_orden=01,estado="1")
            oir_mensaje(order)
            print(f'Mensaje oído: {mensaje.value().data}')
            consumidor.acknowledge(mensaje)
            cliente.close()

        except:
            logging.error('ERROR: Suscribiendose al tópico ejecutar-saga')
            traceback.print_exc()
            if cliente:
                cliente.close()