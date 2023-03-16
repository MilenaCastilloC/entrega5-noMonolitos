
from __future__ import annotations
from dataclasses import dataclass, field

import entregasalpes.modulos.ordenes.dominio.objetos_valor as ov
from entregasalpes.modulos.ordenes.dominio.eventos import OrdenCreada
from entregasalpes.seedwork.dominio.entidades import AgregacionRaiz

@dataclass
class Orden(AgregacionRaiz):
     
    estado: ov.EstadoOrden = field(default=ov.EstadoOrden.PENDIENTE)
 

    def crear_orden(self, orden: Orden):
        self.estado = orden.estado

        self.agregar_evento(OrdenCreada(id_orden=self.id, id=self.id, estado=self.estado, fecha_creacion=self.fecha_creacion))
        # TODO Agregar evento de compensación

