from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import route_stops_controller
from my_project.auth.domain import RouteStops

route_stops_bp = Blueprint('route_stops', __name__, url_prefix='/route-stops')


@route_stops_bp.get('')
def get_all_route_stops() -> Response:
    """
    Get all route stops
    ---
    tags:
      - RouteStops
    responses:
      200:
        description: List of all route stops
    """
    return make_response(jsonify(route_stops_controller.find_all()), HTTPStatus.OK)


@route_stops_bp.post('')
def create_route_stops() -> Response:
    """
    Create new route stop
    ---
    tags:
      - RouteStops
    parameters:
      - in: body
        name: route_stop
        description: Route stop data
        required: true
        schema:
          type: object
          properties:
            route_id:
              type: integer
              description: Route ID
            stop_id:
              type: integer
              description: Stop ID
            stop_order:
              type: integer
              description: Stop order
    responses:
      200:
        description: Route stop created successfully
    """
    content = request.get_json()
    route_id = content['route_id']
    stop_id = content['stop_id']
    stop_order = content['stop_order']
    route_stops_controller.insert_route_type(route_id, stop_id, stop_order)
    return make_response(jsonify(route_stops_controller.find_all()), HTTPStatus.OK)


@route_stops_bp.get('/<int:route_stops_id>')
def get_route_stops(route_stops_id: int) -> Response:
    """
    Get route stop by ID
    ---
    tags:
      - RouteStops
    parameters:
      - in: path
        name: route_stops_id
        type: integer
        required: true
        description: Route stop ID
    responses:
      200:
        description: Route stop data
      404:
        description: Route stop not found
    """
    return make_response(jsonify(route_stops_controller.find_by_id(route_stops_id)), HTTPStatus.OK)


@route_stops_bp.put('/<int:route_stops_id>')
def update_route_stops(route_stops_id: int) -> Response:
    """
    Update route stop by ID
    ---
    tags:
      - RouteStops
    parameters:
      - in: path
        name: route_stops_id
        type: integer
        required: true
        description: Route stop ID
      - in: body
        name: route_stop
        description: Updated route stop data
        required: true
        schema:
          type: object
          properties:
            route_id:
              type: integer
              description: Route ID
            stop_id:
              type: integer
              description: Stop ID
            stop_order:
              type: integer
              description: Stop order
    responses:
      200:
        description: Route stop updated successfully
      404:
        description: Route stop not found
    """
    content = request.get_json()
    route_stops = RouteStops.create_from_dto(content)
    route_stops_controller.update(route_stops_id, route_stops)
    return make_response("RouteStops updated", HTTPStatus.OK)


@route_stops_bp.patch('/<int:route_stops_id>')
def patch_route_stops(route_stops_id: int) -> Response:
    """
    Partially update route stop by ID
    ---
    tags:
      - RouteStops
    parameters:
      - in: path
        name: route_stops_id
        type: integer
        required: true
        description: Route stop ID
      - in: body
        name: route_stop
        description: Partial route stop data
        required: true
        schema:
          type: object
          properties:
            route_id:
              type: integer
              description: Route ID
            stop_id:
              type: integer
              description: Stop ID
            stop_order:
              type: integer
              description: Stop order
    responses:
      200:
        description: Route stop updated successfully
      404:
        description: Route stop not found
    """
    content = request.get_json()
    route_stops_controller.patch(route_stops_id, content)
    return make_response("RouteStops updated", HTTPStatus.OK)


@route_stops_bp.delete('/<int:route_stops_id>')
def delete_route_stops(route_stops_id: int) -> Response:
    """
    Delete route stop by ID
    ---
    tags:
      - RouteStops
    parameters:
      - in: path
        name: route_stops_id
        type: integer
        required: true
        description: Route stop ID
    responses:
      200:
        description: Route stop deleted successfully
      404:
        description: Route stop not found
    """
    route_stops_controller.delete(route_stops_id)
    return make_response("RouteStops deleted", HTTPStatus.OK)


@route_stops_bp.get('/find-routes/<int:route_id>')
def get_routes_in_rs(route_id: int) -> Response:
    """
    Find route stops by route ID
    ---
    tags:
      - RouteStops
    parameters:
      - in: path
        name: route_id
        type: integer
        required: true
        description: Route ID
    responses:
      200:
        description: List of route stops for the route
      404:
        description: Route not found
    """
    return make_response(jsonify(route_stops_controller.get_routes_in_rs(route_id)), HTTPStatus.OK)


@route_stops_bp.get('/find-stops/<int:stop_id>')
def get_stops_in_rs(stop_id: int) -> Response:
    """
    Find route stops by stop ID
    ---
    tags:
      - RouteStops
    parameters:
      - in: path
        name: stop_id
        type: integer
        required: true
        description: Stop ID
    responses:
      200:
        description: List of route stops for the stop
      404:
        description: Stop not found
    """
    return make_response(jsonify(route_stops_controller.get_stops_in_rs(stop_id)), HTTPStatus.OK)
