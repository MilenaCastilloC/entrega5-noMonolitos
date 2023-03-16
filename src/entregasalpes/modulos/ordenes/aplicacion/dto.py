from dataclasses import dataclass, field
from entregasalpes.seedwork.aplicacion.dto import DTO

@dataclass(frozen=True)
class LegDTO(DTO):
    id: str
    fecha_creacion: str
    fecha_actualizacion: str
    