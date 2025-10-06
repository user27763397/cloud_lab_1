from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import hotel_info_controller
from my_project.auth.domain import HotelInfo

hotel_info_bp = Blueprint('hotel-info', __name__, url_prefix='/hotel-info')


@hotel_info_bp.get('')
def get_all_hotel_info() -> Response:
    """
    Get all hotel info
    ---
    tags:
      - HotelInfo
    responses:
      200:
        description: List of all hotel info
    """
    return make_response(jsonify(hotel_info_controller.find_all()), HTTPStatus.OK)


@hotel_info_bp.post('')
def create_hotel_info() -> Response:
    """
    Create new hotel info
    ---
    tags:
      - HotelInfo
    parameters:
      - in: body
        name: hotel_info
        description: Hotel info data
        required: true
        schema:
          type: object
          properties:
            route_id:
              type: integer
              description: Route ID
            hotel_name:
              type: string
              description: Hotel name
            address:
              type: string
              description: Hotel address
            amenities:
              type: string
              description: Hotel amenities
    responses:
      201:
        description: Hotel info created successfully
    """
    content = request.get_json()
    hotel_info = HotelInfo.create_from_dto(content)
    hotel_info_controller.create(hotel_info)
    return make_response(jsonify(hotel_info.put_into_dto()), HTTPStatus.CREATED)


@hotel_info_bp.get('/<int:hotel_info_id>')
def get_hotel_info(hotel_info_id: int) -> Response:
    """
    Get hotel info by ID
    ---
    tags:
      - HotelInfo
    parameters:
      - in: path
        name: hotel_info_id
        type: integer
        required: true
        description: Hotel info ID
    responses:
      200:
        description: Hotel info data
      404:
        description: Hotel info not found
    """
    return make_response(jsonify(hotel_info_controller.find_by_id(hotel_info_id)), HTTPStatus.OK)


@hotel_info_bp.put('/<int:hotel_info_id>')
def update_hotel_info(hotel_info_id: int) -> Response:
    """
    Update hotel info by ID
    ---
    tags:
      - HotelInfo
    parameters:
      - in: path
        name: hotel_info_id
        type: integer
        required: true
        description: Hotel info ID
      - in: body
        name: hotel_info
        description: Updated hotel info data
        required: true
        schema:
          type: object
          properties:
            route_id:
              type: integer
              description: Route ID
            hotel_name:
              type: string
              description: Hotel name
            address:
              type: string
              description: Hotel address
            amenities:
              type: string
              description: Hotel amenities
    responses:
      200:
        description: Hotel info updated successfully
      404:
        description: Hotel info not found
    """
    content = request.get_json()
    hotel_info = HotelInfo.create_from_dto(content)
    hotel_info_controller.update(hotel_info_id, hotel_info)
    return make_response("HotelInfo updated", HTTPStatus.OK)


@hotel_info_bp.patch('/<int:hotel_info_id>')
def patch_hotel_info(hotel_info_id: int) -> Response:
    """
    Partially update hotel info by ID
    ---
    tags:
      - HotelInfo
    parameters:
      - in: path
        name: hotel_info_id
        type: integer
        required: true
        description: Hotel info ID
      - in: body
        name: hotel_info
        description: Partial hotel info data
        required: true
        schema:
          type: object
          properties:
            route_id:
              type: integer
              description: Route ID
            hotel_name:
              type: string
              description: Hotel name
            address:
              type: string
              description: Hotel address
            amenities:
              type: string
              description: Hotel amenities
    responses:
      200:
        description: Hotel info updated successfully
      404:
        description: Hotel info not found
    """
    content = request.get_json()
    hotel_info_controller.patch(hotel_info_id, content)
    return make_response("HotelInfo updated", HTTPStatus.OK)


@hotel_info_bp.delete('/<int:hotel_info_id>')
def delete_hotel_info(hotel_info_id: int) -> Response:
    """
    Delete hotel info by ID
    ---
    tags:
      - HotelInfo
    parameters:
      - in: path
        name: hotel_info_id
        type: integer
        required: true
        description: Hotel info ID
    responses:
      200:
        description: Hotel info deleted successfully
      404:
        description: Hotel info not found
    """
    hotel_info_controller.delete(hotel_info_id)
    return make_response("HotelInfo deleted", HTTPStatus.OK)


@hotel_info_bp.get('/find-hotels-after-route/<int:route_id>')
def get_hotels_after_route(route_id: int) -> Response:
    """
    Find hotels by route ID
    ---
    tags:
      - HotelInfo
    parameters:
      - in: path
        name: route_id
        type: integer
        required: true
        description: Route ID
    responses:
      200:
        description: List of hotels for the route
      404:
        description: Route not found
    """
    return make_response(jsonify(hotel_info_controller.get_hotels_after_route(route_id)), HTTPStatus.OK)
