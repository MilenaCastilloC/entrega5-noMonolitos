""" Mapeadores para la capa de infrastructura del dominio de vuelos

En este archivo usted encontrará los diferentes mapeadores
encargados de la transformación entre formatos de dominio y DTOs

"""

from entregasalpes.seedwork.dominio.repositorios import Mapeador
# from entregasalpes.seedwork.infraestructura.utils import unix_time_millis

from entregasalpes.modulos.ordenes.dominio.entidades import Orden
# from entregasalpes.modulos.ordenes.dominio.eventos import ReservaAprobada, ReservaCancelada, ReservaAprobada, ReservaPagada, ReservaCreada, EventoReserva

from .dto import Orden as OrdenDTO
# from .excepciones import NoExisteImplementacionParaTipoFabricaExcepcion
# from pulsar.schema import *

class MapadeadorEventosOrden(Mapeador):

    def obtener_tipo(self) -> type:
        return EventoOrden.__class__

#     def es_version_valida(self, version):
#         for v in self.versions:
#             if v == version:
#                 return True
#         return False


    def entidad_a_dto(self, entidad: Orden) -> OrdenDTO:
        orden_dto = OrdenDTO()
        orden_dto.id = str(entidad.id)
        orden_dto.fecha_creacion = entidad.fecha_creacion
        orden_dto.fecha_actualizacion = entidad.fecha_actualizacion
        return orden_dto

    def dto_a_entidad(self, dto: OrdenDTO) -> Orden:
        orden = Orden(dto.id, dto.fecha_creacion, dto.fecha_actualizacion)



        return orden