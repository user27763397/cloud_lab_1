from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import guides_controller
from my_project.auth.domain import Guides

guides_bp = Blueprint('guides', __name__, url_prefix='/guides')


@guides_bp.get('')
def get_all_guides() -> Response:
    """
    Get all guides
    ---
    tags:
      - Guides
    responses:
      200:
        description: List of all guides
    """
    return make_response(jsonify(guides_controller.find_all()), HTTPStatus.OK)


@guides_bp.post('')
def create_stops() -> Response:
    """
    Create new guide
    ---
    tags:
      - Guides
    parameters:
      - in: body
        name: guide
        description: Guide data
        required: true
        schema:
          type: object
          properties:
            first_name:
              type: string
              description: Guide first name
            last_name:
              type: string
              description: Guide last name
            contact_info:
              type: string
              description: Guide contact information
    responses:
      201:
        description: Guide created successfully
    """
    content = request.get_json()
    guides = Guides.create_from_dto(content)
    guides_controller.create(guides)
    return make_response(jsonify(guides.put_into_dto()), HTTPStatus.CREATED)


@guides_bp.get('/<int:guides_id>')
def get_guides(guides_id: int) -> Response:
    """
    Get guide by ID
    ---
    tags:
      - Guides
    parameters:
      - in: path
        name: guides_id
        type: integer
        required: true
        description: Guide ID
    responses:
      200:
        description: Guide data
      404:
        description: Guide not found
    """
    return make_response(jsonify(guides_controller.find_by_id(guides_id)), HTTPStatus.OK)


@guides_bp.put('/<int:guides_id>')
def update_guides(guides_id: int) -> Response:
    """
    Update guide by ID
    ---
    tags:
      - Guides
    parameters:
      - in: path
        name: guides_id
        type: integer
        required: true
        description: Guide ID
      - in: body
        name: guide
        description: Updated guide data
        required: true
        schema:
          type: object
          properties:
            first_name:
              type: string
              description: Guide first name
            last_name:
              type: string
              description: Guide last name
            contact_info:
              type: string
              description: Guide contact information
    responses:
      200:
        description: Guide updated successfully
      404:
        description: Guide not found
    """
    content = request.get_json()
    guides = Guides.create_from_dto(content)
    guides_controller.update(guides_id, guides)
    return make_response("Guides updated", HTTPStatus.OK)


@guides_bp.patch('/<int:guides_id>')
def patch_guides(guides_id: int) -> Response:
    """
    Partially update guide by ID
    ---
    tags:
      - Guides
    parameters:
      - in: path
        name: guides_id
        type: integer
        required: true
        description: Guide ID
      - in: body
        name: guide
        description: Partial guide data
        required: true
        schema:
          type: object
          properties:
            first_name:
              type: string
              description: Guide first name
            last_name:
              type: string
              description: Guide last name
            contact_info:
              type: string
              description: Guide contact information
    responses:
      200:
        description: Guide updated successfully
      404:
        description: Guide not found
    """
    content = request.get_json()
    guides_controller.patch(guides_id, content)
    return make_response("Guides updated", HTTPStatus.OK)


@guides_bp.delete('/<int:guides_id>')
def delete_guides(guides_id: int) -> Response:
    """
    Delete guide by ID
    ---
    tags:
      - Guides
    parameters:
      - in: path
        name: guides_id
        type: integer
        required: true
        description: Guide ID
    responses:
      200:
        description: Guide deleted successfully
      404:
        description: Guide not found
    """
    guides_controller.delete(guides_id)
    return make_response("Guides deleted", HTTPStatus.OK)

