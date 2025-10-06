from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import hiking_info_controller
from my_project.auth.domain import HikingInfo

hiking_info_bp = Blueprint('hiking-info', __name__, url_prefix='/hiking-info')


@hiking_info_bp.get('')
def get_all_hiking_info() -> Response:
    """
    Get all hiking info
    ---
    tags:
      - HikingInfo
    responses:
      200:
        description: List of all hiking info
    """
    return make_response(jsonify(hiking_info_controller.find_all()), HTTPStatus.OK)


@hiking_info_bp.post('')
def create_hiking_info() -> Response:
    """
    Create new hiking info
    ---
    tags:
      - HikingInfo
    parameters:
      - in: body
        name: hiking_info
        description: Hiking info data
        required: true
        schema:
          type: object
          properties:
            route_id:
              type: integer
              description: Route ID
            difficulty_level:
              type: string
              description: Difficulty level
            distance_km:
              type: number
              format: float
              description: Distance in kilometers
            elevation_gain_m:
              type: integer
              description: Elevation gain in meters
    responses:
      201:
        description: Hiking info created successfully
    """
    content = request.get_json()
    hiking_info = HikingInfo.create_from_dto(content)
    hiking_info_controller.create(hiking_info)
    return make_response(jsonify(hiking_info.put_into_dto()), HTTPStatus.CREATED)


@hiking_info_bp.get('/<int:hiking_info_id>')
def get_hiking_info(hiking_info_id: int) -> Response:
    """
    Get hiking info by ID
    ---
    tags:
      - HikingInfo
    parameters:
      - in: path
        name: hiking_info_id
        type: integer
        required: true
        description: Hiking info ID
    responses:
      200:
        description: Hiking info data
      404:
        description: Hiking info not found
    """
    return make_response(jsonify(hiking_info_controller.find_by_id(hiking_info_id)), HTTPStatus.OK)


@hiking_info_bp.put('/<int:hiking_info_id>')
def update_hiking_info(hiking_info_id: int) -> Response:
    """
    Update hiking info by ID
    ---
    tags:
      - HikingInfo
    parameters:
      - in: path
        name: hiking_info_id
        type: integer
        required: true
        description: Hiking info ID
      - in: body
        name: hiking_info
        description: Updated hiking info data
        required: true
        schema:
          type: object
          properties:
            route_id:
              type: integer
              description: Route ID
            difficulty_level:
              type: string
              description: Difficulty level
            distance_km:
              type: number
              format: float
              description: Distance in kilometers
            elevation_gain_m:
              type: integer
              description: Elevation gain in meters
    responses:
      200:
        description: Hiking info updated successfully
      404:
        description: Hiking info not found
    """
    content = request.get_json()
    hiking_info = HikingInfo.create_from_dto(content)
    hiking_info_controller.update(hiking_info_id, hiking_info)
    return make_response("HikingInfo updated", HTTPStatus.OK)


@hiking_info_bp.patch('/<int:hiking_info_id>')
def patch_hiking_info(hiking_info_id: int) -> Response:
    """
    Partially update hiking info by ID
    ---
    tags:
      - HikingInfo
    parameters:
      - in: path
        name: hiking_info_id
        type: integer
        required: true
        description: Hiking info ID
      - in: body
        name: hiking_info
        description: Partial hiking info data
        required: true
        schema:
          type: object
          properties:
            route_id:
              type: integer
              description: Route ID
            difficulty_level:
              type: string
              description: Difficulty level
            distance_km:
              type: number
              format: float
              description: Distance in kilometers
            elevation_gain_m:
              type: integer
              description: Elevation gain in meters
    responses:
      200:
        description: Hiking info updated successfully
      404:
        description: Hiking info not found
    """
    content = request.get_json()
    hiking_info_controller.patch(hiking_info_id, content)
    return make_response("HikingInfo updated", HTTPStatus.OK)


@hiking_info_bp.delete('/<int:hiking_info_id>')
def delete_hiking_info(hiking_info_id: int) -> Response:
    """
    Delete hiking info by ID
    ---
    tags:
      - HikingInfo
    parameters:
      - in: path
        name: hiking_info_id
        type: integer
        required: true
        description: Hiking info ID
    responses:
      200:
        description: Hiking info deleted successfully
      404:
        description: Hiking info not found
    """
    hiking_info_controller.delete(hiking_info_id)
    return make_response("HikingInfo deleted", HTTPStatus.OK)


@hiking_info_bp.get('/find-hiking-after-route/<int:route_id>')
def get_hiking_after_route(route_id: int) -> Response:
    """
    Find hiking info by route ID
    ---
    tags:
      - HikingInfo
    parameters:
      - in: path
        name: route_id
        type: integer
        required: true
        description: Route ID
    responses:
      200:
        description: List of hiking info for the route
      404:
        description: Route not found
    """
    return make_response(jsonify(hiking_info_controller.get_hiking_after_route(route_id)), HTTPStatus.OK)
