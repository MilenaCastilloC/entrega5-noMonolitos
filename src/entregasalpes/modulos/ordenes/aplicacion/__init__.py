from pydispatch import dispatcher

from .handlers import HandlerOrdenIntegracion

from entregasalpes.modulos.ordenes.dominio.eventos import ReservaCreada

dispatcher.connect(HandlerOrdenIntegracion.handle_orden_creada, signal=f'{OrdenCreada.__name__}Integracion')
