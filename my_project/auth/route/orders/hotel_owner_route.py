from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import hotel_owner_controller
from my_project.auth.domain import HotelOwner

hotel_owner_bp = Blueprint('hotel-owner', __name__, url_prefix='/hotel-owners')


@hotel_owner_bp.get('')
def get_all_hotel_owner() -> Response:
    """
    Get all hotel owners
    ---
    tags:
      - HotelOwner
    responses:
      200:
        description: List of all hotel owners
    """
    return make_response(jsonify(hotel_owner_controller.find_all()), HTTPStatus.OK)


@hotel_owner_bp.post('')
def create_hotel_owner() -> Response:
    """
    Create new hotel owner
    ---
    tags:
      - HotelOwner
    parameters:
      - in: body
        name: hotel_owner
        description: Hotel owner data
        required: true
        schema:
          type: object
          properties:
            hotel_id:
              type: integer
              description: Hotel ID
            name:
              type: string
              description: Owner name
    responses:
      201:
        description: Hotel owner created successfully
    """
    content = request.get_json()
    hotel_owner = HotelOwner.create_from_dto(content)
    hotel_owner_controller.create(hotel_owner)
    return make_response(jsonify(hotel_owner.put_into_dto()), HTTPStatus.CREATED)


@hotel_owner_bp.get('/<int:hotel_owner_id>')
def get_hotel_owner(hotel_owner_id: int) -> Response:
    """
    Get hotel owner by ID
    ---
    tags:
      - HotelOwner
    parameters:
      - in: path
        name: hotel_owner_id
        type: integer
        required: true
        description: Hotel owner ID
    responses:
      200:
        description: Hotel owner data
      404:
        description: Hotel owner not found
    """
    return make_response(jsonify(hotel_owner_controller.find_by_id(hotel_owner_id)), HTTPStatus.OK)


@hotel_owner_bp.put('/<int:hotel_owner_id>')
def update_hotel_owner(hotel_owner_id: int) -> Response:
    """
    Update hotel owner by ID
    ---
    tags:
      - HotelOwner
    parameters:
      - in: path
        name: hotel_owner_id
        type: integer
        required: true
        description: Hotel owner ID
      - in: body
        name: hotel_owner
        description: Updated hotel owner data
        required: true
        schema:
          type: object
          properties:
            hotel_id:
              type: integer
              description: Hotel ID
            name:
              type: string
              description: Owner name
    responses:
      200:
        description: Hotel owner updated successfully
      404:
        description: Hotel owner not found
    """
    content = request.get_json()
    hotel_owner = HotelOwner.create_from_dto(content)
    hotel_owner_controller.update(hotel_owner_id, hotel_owner)
    return make_response("HotelOwner updated", HTTPStatus.OK)


@hotel_owner_bp.patch('/<int:hotel_owner_id>')
def patch_hotel_owner(hotel_owner_id: int) -> Response:
    """
    Partially update hotel owner by ID
    ---
    tags:
      - HotelOwner
    parameters:
      - in: path
        name: hotel_owner_id
        type: integer
        required: true
        description: Hotel owner ID
      - in: body
        name: hotel_owner
        description: Partial hotel owner data
        required: true
        schema:
          type: object
          properties:
            hotel_id:
              type: integer
              description: Hotel ID
            name:
              type: string
              description: Owner name
    responses:
      200:
        description: Hotel owner updated successfully
      404:
        description: Hotel owner not found
    """
    content = request.get_json()
    hotel_owner_controller.patch(hotel_owner_id, content)
    return make_response("HotelOwner updated", HTTPStatus.OK)


@hotel_owner_bp.delete('/<int:hotel_owner_id>')
def delete_hotel_owner(hotel_owner_id: int) -> Response:
    """
    Delete hotel owner by ID
    ---
    tags:
      - HotelOwner
    parameters:
      - in: path
        name: hotel_owner_id
        type: integer
        required: true
        description: Hotel owner ID
    responses:
      200:
        description: Hotel owner deleted successfully
      404:
        description: Hotel owner not found
    """
    hotel_owner_controller.delete(hotel_owner_id)
    return make_response("HotelOwner deleted", HTTPStatus.OK)

