from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import route_guides_controller
from my_project.auth.domain import RouteGuides

route_guides_bp = Blueprint('route_guides', __name__, url_prefix='/route-guides')


@route_guides_bp.get('')
def get_all_route_guides() -> Response:
    """
    Get all route guides
    ---
    tags:
      - RouteGuides
    responses:
      200:
        description: List of all route guides
    """
    return make_response(jsonify(route_guides_controller.find_all()), HTTPStatus.OK)


@route_guides_bp.post('')
def create_route_guides() -> Response:
    """
    Create new route guide
    ---
    tags:
      - RouteGuides
    parameters:
      - in: body
        name: route_guide
        description: Route guide data
        required: true
        schema:
          type: object
          properties:
            route_id:
              type: integer
              description: Route ID
            guide_id:
              type: integer
              description: Guide ID
            work_date:
              type: string
              format: date
              description: Work date
    responses:
      201:
        description: Route guide created successfully
    """
    content = request.get_json()
    route_guides = RouteGuides.create_from_dto(content)
    route_guides_controller.create(route_guides)
    return make_response(jsonify(route_guides.put_into_dto()), HTTPStatus.CREATED)


@route_guides_bp.get('/<int:route_guides_id>')
def get_route_guides(route_guides_id: int) -> Response:
    """
    Get route guide by ID
    ---
    tags:
      - RouteGuides
    parameters:
      - in: path
        name: route_guides_id
        type: integer
        required: true
        description: Route guide ID
    responses:
      200:
        description: Route guide data
      404:
        description: Route guide not found
    """
    return make_response(jsonify(route_guides_controller.find_by_id(route_guides_id)), HTTPStatus.OK)


@route_guides_bp.put('/<int:route_guides_id>')
def update_route_guides(route_guides_id: int) -> Response:
    """
    Update route guide by ID
    ---
    tags:
      - RouteGuides
    parameters:
      - in: path
        name: route_guides_id
        type: integer
        required: true
        description: Route guide ID
      - in: body
        name: route_guide
        description: Updated route guide data
        required: true
        schema:
          type: object
          properties:
            route_id:
              type: integer
              description: Route ID
            guide_id:
              type: integer
              description: Guide ID
            work_date:
              type: string
              format: date
              description: Work date
    responses:
      200:
        description: Route guide updated successfully
      404:
        description: Route guide not found
    """
    content = request.get_json()
    route_guides = RouteGuides.create_from_dto(content)
    route_guides_controller.update(route_guides_id, route_guides)
    return make_response("RouteGuides updated", HTTPStatus.OK)


@route_guides_bp.patch('/<int:route_guides_id>')
def patch_route_guides(route_guides_id: int) -> Response:
    """
    Partially update route guide by ID
    ---
    tags:
      - RouteGuides
    parameters:
      - in: path
        name: route_guides_id
        type: integer
        required: true
        description: Route guide ID
      - in: body
        name: route_guide
        description: Partial route guide data
        required: true
        schema:
          type: object
          properties:
            route_id:
              type: integer
              description: Route ID
            guide_id:
              type: integer
              description: Guide ID
            work_date:
              type: string
              format: date
              description: Work date
    responses:
      200:
        description: Route guide updated successfully
      404:
        description: Route guide not found
    """
    content = request.get_json()
    route_guides_controller.patch(route_guides_id, content)
    return make_response("RouteGuides updated", HTTPStatus.OK)


@route_guides_bp.delete('/<int:route_guides_id>')
def delete_route_guides(route_guides_id: int) -> Response:
    """
    Delete route guide by ID
    ---
    tags:
      - RouteGuides
    parameters:
      - in: path
        name: route_guides_id
        type: integer
        required: true
        description: Route guide ID
    responses:
      200:
        description: Route guide deleted successfully
      404:
        description: Route guide not found
    """
    route_guides_controller.delete(route_guides_id)
    return make_response("RouteGuides deleted", HTTPStatus.OK)


@route_guides_bp.get('/find-routes/<int:route_id>')
def get_routes_in_rg(route_id: int) -> Response:
    """
    Find route guides by route ID
    ---
    tags:
      - RouteGuides
    parameters:
      - in: path
        name: route_id
        type: integer
        required: true
        description: Route ID
    responses:
      200:
        description: List of route guides for the route
      404:
        description: Route not found
    """
    return make_response(jsonify(route_guides_controller.get_routes_in_rg(route_id)), HTTPStatus.OK)


@route_guides_bp.get('/find-guides/<int:guide_id>')
def get_guides_in_rg(guide_id: int) -> Response:
    """
    Find route guides by guide ID
    ---
    tags:
      - RouteGuides
    parameters:
      - in: path
        name: guide_id
        type: integer
        required: true
        description: Guide ID
    responses:
      200:
        description: List of route guides for the guide
      404:
        description: Guide not found
    """
    return make_response(jsonify(route_guides_controller.get_guides_in_rg(guide_id)), HTTPStatus.OK)
