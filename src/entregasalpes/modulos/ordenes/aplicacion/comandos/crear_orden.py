from entregasalpes.seedwork.aplicacion.comandos import Comando
from entregasalpes.modulos.ordenes.aplicacion.dto import OrdenDTO
from .base import CrearOrdenBaseHandler
from dataclasses import dataclass, field
from entregasalpes.seedwork.aplicacion.comandos import ejecutar_commando as comando

from entregasalpes.modulos.ordenes.dominio.entidades import Orden
from entregasalpes.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from entregasalpes.modulos.ordenes.aplicacion.mapeadores import MapeadorOrden
from entregasalpes.modulos.ordenes.infraestructura.repositorios import RepositorioOrdenes, RepositorioEventosOrdenes


@dataclass
class CrearOrden(Comando):
    fecha_creacion: str
    fecha_actualizacion: str
    id: str


class CrearOrdenHandler(CrearOrdenBaseHandler):
    
    def handle(self, comando: CrearOrden):
        orden_dto = OrdenDTO(
                fecha_actualizacion=comando.fecha_actualizacion
            ,   fecha_creacion=comando.fecha_creacion
            ,   id=comando.id
            )

        orden: Orden = self.fabrica_ordenes.crear_objeto(orden_dto, MapeadorOrden())
        orden.crear_orden(orden)

        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioOrdenes.__class__)
        repositorio_eventos = self.fabrica_repositorio.crear_objeto(RepositorioEventosOrdenes.__class__)

        UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, orden, repositorio_eventos_func=repositorio_eventos.agregar)
        UnidadTrabajoPuerto.savepoint()
        UnidadTrabajoPuerto.commit()


@comando.register(CrearOrden)
def ejecutar_comando_crear_orden(comando: CrearOrden):
    handler = CrearOrdenHandler()
    handler.handle(comando)
    