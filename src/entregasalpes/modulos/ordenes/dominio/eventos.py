from __future__ import annotations
from dataclasses import dataclass, field
from entregasalpes.seedwork.dominio.eventos import (EventoDominio)
from datetime import datetime

import uuid

 
@dataclass
class OrdenCreada(EventoOrden):
    id_orden: uuid.UUID = None
    estado: str = None
    fecha_creacion: datetime = None
 
 