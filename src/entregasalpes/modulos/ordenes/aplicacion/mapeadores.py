from entregasalpes.seedwork.aplicacion.dto import Mapeador as AppMap
from entregasalpes.seedwork.dominio.repositorios import Mapeador as RepMap
from entregasalpes.modulos.ordenes.dominio.entidades import Orden

from .dto import OrdenDTO

from datetime import datetime

class MapeadorOrdenDTOJson(AppMap):
    
    def externo_a_dto(self, externo: dict) -> OrdenDTO:
        orden_dto = OrdenDTO(externo.get('id'), externo.get('fecha_creacion'),externo.get('fecha_actualizacion'))
        return orden_dto
 
    def dto_a_externo(self, dto: OrdenDTO) -> dict:
        return dto.__dict__

class MapeadorOrden(RepMap):

    def obtener_tipo(self) -> type:
        return Orden.__class__
      

    def entidad_a_dto(self, entidad: Orden) -> OrdenDTO:
        
        fecha_creacion = entidad.fecha_creacion.strftime(self._FORMATO_FECHA)
        fecha_actualizacion = entidad.fecha_actualizacion.strftime(self._FORMATO_FECHA)
        _id = str(entidad.id)

        return OrdenDTO(fecha_creacion, fecha_actualizacion, _id)

    def dto_a_entidad(self, dto: OrdenDTO) -> Orden:
        orden = Orden()
        
        return orden



