import entregasalpes.seedwork.presentacion.api as api
import json
from entregasalpes.modulos.ordenes.aplicacion.dto import ReservaDTO
from entregasalpes.seedwork.dominio.excepciones import ExcepcionDominio

from flask import redirect, render_template, request, session, url_for
from flask import Response

from entregasalpes.modulos.ordenes.aplicacion.mapeadores import MapeadorOrdenDTOJson
from entregasalpes.modulos.ordenes.aplicacion.comandos.crear_orden import CrearOrden

from entregasalpes.seedwork.aplicacion.comandos import ejecutar_commando


bp = api.crear_blueprint('ordenes', '/ordenes')

@bp.route('/orden', methods=('POST',))
def ordenar_usando_comando():
    try:
        # NOTE Asignamos el valor 'pulsar' para usar la Unidad de trabajo de Pulsar y 
        # no la defecto de SQLAlchemy
        session['uow_metodo'] = 'pulsar'

        orden_dict = request.json

        map_orden = MapeadorOrdenDTOJson()
        reserva_dto = map_reserva.externo_a_dto(orden_dict)

        comando = CrearOrden(orden_dto.fecha_creacion, orden_dto.fecha_actualizacion, orden_dto.id)
        
        # TODO Reemplaze es todo código sincrono y use el broker de eventos para propagar este comando de forma asíncrona
        # Revise la clase Despachador de la capa de infraestructura
        ejecutar_commando(comando)
        
        return Response('{}', status=202, mimetype='application/json')
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')
#
# @bp.route('/orden', methods=('GET',))
# @bp.route('/orden/<id>', methods=('GET',))
# def dar_reserva_usando_query(id=None):
#     if id:
#         query_resultado = ejecutar_query(ObtenerReserva(id))
#         map_reserva = MapeadorOrdenDTOJson()
#
#         return map_reserva.dto_a_externo(query_resultado.resultado)
#     else:
#         return [{'message': 'GET!'}]