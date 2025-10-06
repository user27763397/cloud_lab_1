from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import stops_controller
from my_project.auth.domain import Stops

stops_bp = Blueprint('stops', __name__, url_prefix='/stops')


@stops_bp.get('')
def get_all_stops() -> Response:
    """
    Get all stops
    ---
    tags:
      - Stops
    responses:
      200:
        description: List of all stops
    """
    return make_response(jsonify(stops_controller.find_all()), HTTPStatus.OK)


@stops_bp.post('')
def create_stops() -> Response:
    """
    Create new stop
    ---
    tags:
      - Stops
    parameters:
      - in: body
        name: stop
        description: Stop data
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
              description: Stop name
            location:
              type: string
              description: Stop location
    responses:
      201:
        description: Stop created successfully
    """
    content = request.get_json()
    stops = Stops.create_from_dto(content)
    stops_controller.create(stops)
    return make_response(jsonify(stops.put_into_dto()), HTTPStatus.CREATED)


@stops_bp.get('/<int:stops_id>')
def get_stops(stops_id: int) -> Response:
    """
    Get stop by ID
    ---
    tags:
      - Stops
    parameters:
      - in: path
        name: stops_id
        type: integer
        required: true
        description: Stop ID
    responses:
      200:
        description: Stop data
      404:
        description: Stop not found
    """
    return make_response(jsonify(stops_controller.find_by_id(stops_id)), HTTPStatus.OK)


@stops_bp.put('/<int:stops_id>')
def update_stops(stops_id: int) -> Response:
    """
    Update stop by ID
    ---
    tags:
      - Stops
    parameters:
      - in: path
        name: stops_id
        type: integer
        required: true
        description: Stop ID
      - in: body
        name: stop
        description: Updated stop data
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
              description: Stop name
            location:
              type: string
              description: Stop location
    responses:
      200:
        description: Stop updated successfully
      404:
        description: Stop not found
    """
    content = request.get_json()
    stops = Stops.create_from_dto(content)
    stops_controller.update(stops_id, stops)
    return make_response("Stops updated", HTTPStatus.OK)


@stops_bp.patch('/<int:stops_id>')
def patch_stops(stops_id: int) -> Response:
    """
    Partially update stop by ID
    ---
    tags:
      - Stops
    parameters:
      - in: path
        name: stops_id
        type: integer
        required: true
        description: Stop ID
      - in: body
        name: stop
        description: Partial stop data
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
              description: Stop name
            location:
              type: string
              description: Stop location
    responses:
      200:
        description: Stop updated successfully
      404:
        description: Stop not found
    """
    content = request.get_json()
    stops_controller.patch(stops_id, content)
    return make_response("Stops updated", HTTPStatus.OK)


@stops_bp.delete('/<int:stops_id>')
def delete_stops(stops_id: int) -> Response:
    """
    Delete stop by ID
    ---
    tags:
      - Stops
    parameters:
      - in: path
        name: stops_id
        type: integer
        required: true
        description: Stop ID
    responses:
      200:
        description: Stop deleted successfully
      404:
        description: Stop not found
    """
    stops_controller.delete(stops_id)
    return make_response("Stops deleted", HTTPStatus.OK)

