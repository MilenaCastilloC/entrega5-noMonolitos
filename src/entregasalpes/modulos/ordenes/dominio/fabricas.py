 
from .entidades import Orden
from .excepciones import TipoObjetoNoExisteEnDominioOrdenesExcepcion
from entregasalpes.seedwork.dominio.repositorios import Mapeador, Repositorio
from entregasalpes.seedwork.dominio.fabricas import Fabrica
from entregasalpes.seedwork.dominio.entidades import Entidad
from entregasalpes.seedwork.dominio.eventos import EventoDominio
from dataclasses import dataclass

@dataclass
class _FabricaOrden(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if isinstance(obj, Entidad) or isinstance(obj, EventoDominio):
            return mapeador.entidad_a_dto(obj)
        else:
            Orden: Orden = mapeador.dto_a_entidad(obj)

            return Orden

@dataclass
class FabricaOrdenes(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if mapeador.obtener_tipo() == Orden.__class__:
            fabrica_orden = _FabricaOrden()
            return fabrica_orden.crear_objeto(obj, mapeador)
        else:
            raise TipoObjetoNoExisteEnDominioOrdenesExcepcion()

