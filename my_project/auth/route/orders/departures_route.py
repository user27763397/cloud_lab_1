from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import departures_controller
from my_project.auth.domain import Departures

departures_bp = Blueprint('departures', __name__, url_prefix='/departures')


@departures_bp.get('')
def get_all_departures() -> Response:
    """
    Get all departures
    ---
    tags:
      - Departures
    responses:
      200:
        description: List of all departures
    """
    return make_response(jsonify(departures_controller.find_all()), HTTPStatus.OK)


@departures_bp.post('')
def create_departures() -> Response:
    """
    Create new departure
    ---
    tags:
      - Departures
    parameters:
      - in: body
        name: departure
        description: Departure data
        required: true
        schema:
          type: object
          properties:
            route_id:
              type: integer
              description: Route ID
            departure_date:
              type: string
              format: date
              description: Departure date
    responses:
      201:
        description: Departure created successfully
    """
    content = request.get_json()
    departures = Departures.create_from_dto(content)
    departures_controller.create(departures)
    return make_response(jsonify(departures.put_into_dto()), HTTPStatus.CREATED)


@departures_bp.get('/<int:departures_id>')
def get_departures(departures_id: int) -> Response:
    """
    Get departure by ID
    ---
    tags:
      - Departures
    parameters:
      - in: path
        name: departures_id
        type: integer
        required: true
        description: Departure ID
    responses:
      200:
        description: Departure data
      404:
        description: Departure not found
    """
    return make_response(jsonify(departures_controller.find_by_id(departures_id)), HTTPStatus.OK)


@departures_bp.put('/<int:departures_id>')
def update_departures(departures_id: int) -> Response:
    """
    Update departure by ID
    ---
    tags:
      - Departures
    parameters:
      - in: path
        name: departures_id
        type: integer
        required: true
        description: Departure ID
      - in: body
        name: departure
        description: Updated departure data
        required: true
        schema:
          type: object
          properties:
            route_id:
              type: integer
              description: Route ID
            departure_date:
              type: string
              format: date
              description: Departure date
    responses:
      200:
        description: Departure updated successfully
      404:
        description: Departure not found
    """
    content = request.get_json()
    departures = Departures.create_from_dto(content)
    departures_controller.update(departures_id, departures)
    return make_response("Departures updated", HTTPStatus.OK)


@departures_bp.patch('/<int:departures_id>')
def patch_departures(departures_id: int) -> Response:
    """
    Partially update departure by ID
    ---
    tags:
      - Departures
    parameters:
      - in: path
        name: departures_id
        type: integer
        required: true
        description: Departure ID
      - in: body
        name: departure
        description: Partial departure data
        required: true
        schema:
          type: object
          properties:
            route_id:
              type: integer
              description: Route ID
            departure_date:
              type: string
              format: date
              description: Departure date
    responses:
      200:
        description: Departure updated successfully
      404:
        description: Departure not found
    """
    content = request.get_json()
    departures_controller.patch(departures_id, content)
    return make_response("Departures updated", HTTPStatus.OK)


@departures_bp.delete('/<int:departures_id>')
def delete_departures(departures_id: int) -> Response:
    """
    Delete departure by ID
    ---
    tags:
      - Departures
    parameters:
      - in: path
        name: departures_id
        type: integer
        required: true
        description: Departure ID
    responses:
      200:
        description: Departure deleted successfully
      404:
        description: Departure not found
    """
    departures_controller.delete(departures_id)
    return make_response("Departures deleted", HTTPStatus.OK)


@departures_bp.get('/find-departures-after-route/<int:route_id>')
def get_departures_after_route(route_id: int) -> Response:
    """
    Find departures by route ID
    ---
    tags:
      - Departures
    parameters:
      - in: path
        name: route_id
        type: integer
        required: true
        description: Route ID
    responses:
      200:
        description: List of departures for the route
      404:
        description: Route not found
    """
    return make_response(jsonify(departures_controller.get_departures_after_route(route_id)), HTTPStatus.OK)


