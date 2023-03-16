from enum import Enum 
from __future__ import annotations

 

class EstadoOrden(str, Enum):
    APROBADA = "Aprobada"
    PENDIENTE = "Pendiente"
    CANCELADA = "Cancelada"
    PAGADA = "Pagada"