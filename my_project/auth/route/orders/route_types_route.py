from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import route_types_controller
from my_project.auth.domain import RouteTypes

route_types_bp = Blueprint('route_types', __name__, url_prefix='/route-types')


@route_types_bp.get('')
def get_all_route_types() -> Response:
    """
    Get all route types
    ---
    tags:
      - RouteTypes
    responses:
      200:
        description: List of all route types
    """
    return make_response(jsonify(route_types_controller.find_all()), HTTPStatus.OK)


@route_types_bp.post('')
def create_route_types() -> Response:
    """
    Create new route type
    ---
    tags:
      - RouteTypes
    parameters:
      - in: body
        name: route_type
        description: Route type data
        required: true
        schema:
          type: object
          properties:
            type_name:
              type: string
              description: Route type name
    responses:
      201:
        description: Route type created successfully
    """
    content = request.get_json()
    type_name = content['type_name']
    route_types_controller.insert_route_type(type_name)
    return make_response(jsonify(route_types_controller.find_all()), HTTPStatus.CREATED)


@route_types_bp.get('/<int:route_types_id>')
def get_route_types(route_types_id: int) -> Response:
    """
    Get route type by ID
    ---
    tags:
      - RouteTypes
    parameters:
      - in: path
        name: route_types_id
        type: integer
        required: true
        description: Route type ID
    responses:
      200:
        description: Route type data
      404:
        description: Route type not found
    """
    return make_response(jsonify(route_types_controller.find_by_id(route_types_id)), HTTPStatus.OK)


@route_types_bp.put('/<int:route_types_id>')
def update_route_types(route_types_id: int) -> Response:
    """
    Update route type by ID
    ---
    tags:
      - RouteTypes
    parameters:
      - in: path
        name: route_types_id
        type: integer
        required: true
        description: Route type ID
      - in: body
        name: route_type
        description: Updated route type data
        required: true
        schema:
          type: object
          properties:
            type_name:
              type: string
              description: Route type name
    responses:
      200:
        description: Route type updated successfully
      404:
        description: Route type not found
    """
    content = request.get_json()
    route_types = RouteTypes.create_from_dto(content)
    route_types_controller.update(route_types_id, route_types)
    return make_response("RouteTypes updated", HTTPStatus.OK)


@route_types_bp.patch('/<int:route_types_id>')
def patch_route_types(route_types_id: int) -> Response:
    """
    Partially update route type by ID
    ---
    tags:
      - RouteTypes
    parameters:
      - in: path
        name: route_types_id
        type: integer
        required: true
        description: Route type ID
      - in: body
        name: route_type
        description: Partial route type data
        required: true
        schema:
          type: object
          properties:
            type_name:
              type: string
              description: Route type name
    responses:
      200:
        description: Route type updated successfully
      404:
        description: Route type not found
    """
    content = request.get_json()
    route_types_controller.patch(route_types_id, content)
    return make_response("RouteTypes updated", HTTPStatus.OK)


@route_types_bp.delete('/<int:route_types_id>')
def delete_route_types(route_types_id: int) -> Response:
    """
    Delete route type by ID
    ---
    tags:
      - RouteTypes
    parameters:
      - in: path
        name: route_types_id
        type: integer
        required: true
        description: Route type ID
    responses:
      200:
        description: Route type deleted successfully
      404:
        description: Route type not found
    """
    route_types_controller.delete(route_types_id)
    return make_response("RouteTypes deleted", HTTPStatus.OK)

