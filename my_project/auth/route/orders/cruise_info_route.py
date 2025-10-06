from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import cruise_info_controller
from my_project.auth.domain import CruiseInfo

cruise_info_bp = Blueprint('cruise-info', __name__, url_prefix='/cruise-info')


@cruise_info_bp.get('')
def get_all_cruise_info() -> Response:
    """
    Get all cruise info
    ---
    tags:
      - CruiseInfo
    responses:
      200:
        description: List of all cruise info
    """
    return make_response(jsonify(cruise_info_controller.find_all()), HTTPStatus.OK)


@cruise_info_bp.post('')
def create_cruise_info() -> Response:
    """
    Create new cruise info
    ---
    tags:
      - CruiseInfo
    parameters:
      - in: body
        name: cruise_info
        description: Cruise info data
        required: true
        schema:
          type: object
          properties:
            route_id:
              type: integer
              description: Route ID
            ship_name:
              type: string
              description: Ship name
            port_of_departure:
              type: string
              description: Port of departure
            port_of_arrival:
              type: string
              description: Port of arrival
    responses:
      201:
        description: Cruise info created successfully
    """
    content = request.get_json()
    cruise_info = CruiseInfo.create_from_dto(content)
    cruise_info_controller.create(cruise_info)
    return make_response(jsonify(cruise_info.put_into_dto()), HTTPStatus.CREATED)


@cruise_info_bp.get('/<int:cruise_info_id>')
def get_cruise_info(cruise_info_id: int) -> Response:
    """
    Get cruise info by ID
    ---
    tags:
      - CruiseInfo
    parameters:
      - in: path
        name: cruise_info_id
        type: integer
        required: true
        description: Cruise info ID
    responses:
      200:
        description: Cruise info data
      404:
        description: Cruise info not found
    """
    return make_response(jsonify(cruise_info_controller.find_by_id(cruise_info_id)), HTTPStatus.OK)


@cruise_info_bp.put('/<int:cruise_info_id>')
def update_cruise_info(cruise_info_id: int) -> Response:
    """
    Update cruise info by ID
    ---
    tags:
      - CruiseInfo
    parameters:
      - in: path
        name: cruise_info_id
        type: integer
        required: true
        description: Cruise info ID
      - in: body
        name: cruise_info
        description: Updated cruise info data
        required: true
        schema:
          type: object
          properties:
            route_id:
              type: integer
              description: Route ID
            ship_name:
              type: string
              description: Ship name
            port_of_departure:
              type: string
              description: Port of departure
            port_of_arrival:
              type: string
              description: Port of arrival
    responses:
      200:
        description: Cruise info updated successfully
      404:
        description: Cruise info not found
    """
    content = request.get_json()
    cruise_info = CruiseInfo.create_from_dto(content)
    cruise_info_controller.update(cruise_info_id, cruise_info)
    return make_response("CruiseInfo updated", HTTPStatus.OK)


@cruise_info_bp.patch('/<int:cruise_info_id>')
def patch_cruise_info(cruise_info_id: int) -> Response:
    """
    Partially update cruise info by ID
    ---
    tags:
      - CruiseInfo
    parameters:
      - in: path
        name: cruise_info_id
        type: integer
        required: true
        description: Cruise info ID
      - in: body
        name: cruise_info
        description: Partial cruise info data
        required: true
        schema:
          type: object
          properties:
            route_id:
              type: integer
              description: Route ID
            ship_name:
              type: string
              description: Ship name
            port_of_departure:
              type: string
              description: Port of departure
            port_of_arrival:
              type: string
              description: Port of arrival
    responses:
      200:
        description: Cruise info updated successfully
      404:
        description: Cruise info not found
    """
    content = request.get_json()
    cruise_info_controller.patch(cruise_info_id, content)
    return make_response("CruiseInfo updated", HTTPStatus.OK)


@cruise_info_bp.delete('/<int:cruise_info_id>')
def delete_cruise_info(cruise_info_id: int) -> Response:
    """
    Delete cruise info by ID
    ---
    tags:
      - CruiseInfo
    parameters:
      - in: path
        name: cruise_info_id
        type: integer
        required: true
        description: Cruise info ID
    responses:
      200:
        description: Cruise info deleted successfully
      404:
        description: Cruise info not found
    """
    cruise_info_controller.delete(cruise_info_id)
    return make_response("CruiseInfo deleted", HTTPStatus.OK)


@cruise_info_bp.get('/find-cruises-after-route/<int:route_id>')
def get_cruises_after_route(route_id: int) -> Response:
    """
    Find cruises by route ID
    ---
    tags:
      - CruiseInfo
    parameters:
      - in: path
        name: route_id
        type: integer
        required: true
        description: Route ID
    responses:
      200:
        description: List of cruises for the route
      404:
        description: Route not found
    """
    return make_response(jsonify(cruise_info_controller.get_cruises_after_route(route_id)), HTTPStatus.OK)
