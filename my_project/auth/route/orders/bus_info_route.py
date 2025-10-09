from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import bus_info_controller
from my_project.auth.domain import BusInfo

bus_info_bp = Blueprint('bus-info', __name__, url_prefix='/bus-info')


@bus_info_bp.get('')
def get_all_bus_info() -> Response:
    """
    Get all bus info
    ---
    tags:
      - BusInfo
    responses:
      200:
        description: List of all bus info
    """
    return make_response(jsonify(bus_info_controller.find_all()), HTTPStatus.OK)


@bus_info_bp.post('')
def create_bus_info() -> Response:
    """
    Create new bus info
    ---
    tags:
      - BusInfo
    parameters:
      - in: body
        name: bus_info
        description: Bus info data
        required: true
        schema:
          type: object
          properties:
            bus_company:
              type: string
              description: Bus company
            route_id:
              type: integer
              description: Route ID
            vehicle_type:
              type: string
              description: Vehicle type
    responses:
      201:
        description: Bus info created successfully
    """
    content = request.get_json()
    bus_info = BusInfo.create_from_dto(content)
    bus_info_controller.create(bus_info)
    return make_response(jsonify(bus_info.put_into_dto()), HTTPStatus.CREATED)


@bus_info_bp.get('/<int:bus_info_id>')
def get_bus_info(bus_info_id: int) -> Response:
    """
    Get bus info by ID
    ---
    tags:
      - BusInfo
    parameters:
      - in: path
        name: bus_info_id
        type: integer
        required: true
        description: Bus info ID
    responses:
      200:
        description: Bus info data
      404:
        description: Bus info not found
    """
    return make_response(jsonify(bus_info_controller.find_by_id(bus_info_id)), HTTPStatus.OK)


@bus_info_bp.put('/<int:bus_info_id>')
def update_bus_info(bus_info_id: int) -> Response:
    """
    Update bus info by ID
    ---
    tags:
      - BusInfo
    parameters:
      - in: path
        name: bus_info_id
        type: integer
        required: true
        description: Bus info ID
      - in: body
        name: bus_info
        description: Updated bus info data
        required: true
        schema:
          type: object
          properties:
            bus_number:
              type: string
              description: Bus number
            capacity:
              type: integer
              description: Bus capacity
    responses:
      200:
        description: Bus info updated successfully
      404:
        description: Bus info not found
    """
    content = request.get_json()
    bus_info = BusInfo.create_from_dto(content)
    bus_info_controller.update(bus_info_id, bus_info)
    return make_response("BusInfo updated", HTTPStatus.OK)


@bus_info_bp.patch('/<int:bus_info_id>')
def patch_bus_info(bus_info_id: int) -> Response:
    """
    Partially update bus info by ID
    ---
    tags:
      - BusInfo
    parameters:
      - in: path
        name: bus_info_id
        type: integer
        required: true
        description: Bus info ID
      - in: body
        name: bus_info
        description: Partial bus info data
        required: true
        schema:
          type: object
          properties:
            bus_number:
              type: string
              description: Bus number
            capacity:
              type: integer
              description: Bus capacity
    responses:
      200:
        description: Bus info updated successfully
      404:
        description: Bus info not found
    """
    content = request.get_json()
    bus_info_controller.patch(bus_info_id, content)
    return make_response("BusInfo updated", HTTPStatus.OK)


#@bus_info_bp.delete('/<int:bus_info_id>')
#def delete_bus_info(bus_info_id: int) -> Response:
    """
    Delete bus info by ID
    ---
    tags:
      - BusInfo
    parameters:
      - in: path
        name: bus_info_id
        type: integer
        required: true
        description: Bus info ID
    responses:
      200:
        description: Bus info deleted successfully
      404:
        description: Bus info not found
    """
    bus_info_controller.delete(bus_info_id)
    return make_response("BusInfo deleted", HTTPStatus.OK)


@bus_info_bp.get('/find-busses-after-route/<int:route_id>')
def get_busses_after_route(route_id: int) -> Response:
    """
    Find busses by route ID
    ---
    tags:
      - BusInfo
    parameters:
      - in: path
        name: route_id
        type: integer
        required: true
        description: Route ID
    responses:
      200:
        description: List of busses for the route
      404:
        description: Route not found
    """
    return make_response(jsonify(bus_info_controller.get_busses_after_route(route_id)), HTTPStatus.OK)

