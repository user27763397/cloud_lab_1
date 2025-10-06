from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import routes_controller
from my_project.auth.domain import Routes

routes_bp = Blueprint('routes', __name__, url_prefix='/routes')


@routes_bp.get('')
def get_all_routes() -> Response:
    """
    Get all routes
    ---
    tags:
      - Routes
    responses:
      200:
        description: List of all routes
    """
    return make_response(jsonify(routes_controller.find_all()), HTTPStatus.OK)


@routes_bp.post('')
def create_routes() -> Response:
    """
    Create new route
    ---
    tags:
      - Routes
    parameters:
      - in: body
        name: route
        description: Route data
        required: true
        schema:
          type: object
          properties:
            route_type_id:
              type: integer
              description: Route type ID
            name:
              type: string
              description: Route name
            description:
              type: string
              description: Route description
            duration_days:
              type: integer
              description: Duration in days
            price_per_person:
              type: number
              format: float
              description: Price per person
            next_departure_date:
              type: string
              format: date
              description: Next departure date
    responses:
      201:
        description: Route created successfully
    """
    content = request.get_json()
    routes = Routes.create_from_dto(content)
    routes_controller.create(routes)
    return make_response(jsonify(routes.put_into_dto()), HTTPStatus.CREATED)


@routes_bp.get('/<int:routes_id>')
def get_routes(routes_id: int) -> Response:
    """
    Get route by ID
    ---
    tags:
      - Routes
    parameters:
      - in: path
        name: routes_id
        type: integer
        required: true
        description: Route ID
    responses:
      200:
        description: Route data
      404:
        description: Route not found
    """
    return make_response(jsonify(routes_controller.find_by_id(routes_id)), HTTPStatus.OK)


@routes_bp.put('/<int:routes_id>')
def update_routes(routes_id: int) -> Response:
    """
    Update route by ID
    ---
    tags:
      - Routes
    parameters:
      - in: path
        name: routes_id
        type: integer
        required: true
        description: Route ID
      - in: body
        name: route
        description: Updated route data
        required: true
        schema:
          type: object
          properties:
            route_type_id:
              type: integer
              description: Route type ID
            name:
              type: string
              description: Route name
            description:
              type: string
              description: Route description
            duration_days:
              type: integer
              description: Duration in days
            price_per_person:
              type: number
              format: float
              description: Price per person
            next_departure_date:
              type: string
              format: date
              description: Next departure date
    responses:
      200:
        description: Route updated successfully
      404:
        description: Route not found
    """
    content = request.get_json()
    routes = Routes.create_from_dto(content)
    routes_controller.update(routes_id, routes)
    return make_response("Routes updated", HTTPStatus.OK)


@routes_bp.patch('/<int:routes_id>')
def patch_routes(routes_id: int) -> Response:
    """
    Partially update route by ID
    ---
    tags:
      - Routes
    parameters:
      - in: path
        name: routes_id
        type: integer
        required: true
        description: Route ID
      - in: body
        name: route
        description: Partial route data
        required: true
        schema:
          type: object
          properties:
            route_type_id:
              type: integer
              description: Route type ID
            name:
              type: string
              description: Route name
            description:
              type: string
              description: Route description
            duration_days:
              type: integer
              description: Duration in days
            price_per_person:
              type: number
              format: float
              description: Price per person
            next_departure_date:
              type: string
              format: date
              description: Next departure date
    responses:
      200:
        description: Route updated successfully
      404:
        description: Route not found
    """
    content = request.get_json()
    routes_controller.patch(routes_id, content)
    return make_response("Routes updated", HTTPStatus.OK)


@routes_bp.delete('/<int:routes_id>')
def delete_routes(routes_id: int) -> Response:
    """
    Delete route by ID
    ---
    tags:
      - Routes
    parameters:
      - in: path
        name: routes_id
        type: integer
        required: true
        description: Route ID
    responses:
      200:
        description: Route deleted successfully
      404:
        description: Route not found
    """
    routes_controller.delete(routes_id)
    return make_response("Routes deleted", HTTPStatus.OK)


@routes_bp.get('/find-routes-after-route-type/<int:route_type_id>')
def get_routes_after_route_type(route_type_id: int) -> Response:
    """
    Find routes by route type ID
    ---
    tags:
      - Routes
    parameters:
      - in: path
        name: route_type_id
        type: integer
        required: true
        description: Route type ID
    responses:
      200:
        description: List of routes for the route type
      404:
        description: Route type not found
    """
    return make_response(jsonify(routes_controller.get_routes_after_route_type(route_type_id)), HTTPStatus.OK)
