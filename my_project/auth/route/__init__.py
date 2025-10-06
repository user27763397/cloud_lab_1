from flask import Flask

from .error_handler import err_handler_bp


def register_routes(app: Flask) -> None:

    app.register_blueprint(err_handler_bp)

    from .orders.bus_info_route import bus_info_bp
    from .orders.cruise_info_route import cruise_info_bp
    from .orders.departures_route import departures_bp
    from .orders.guides_route import guides_bp
    from .orders.hiking_info_route import hiking_info_bp
    from .orders.hotel_info_route import hotel_info_bp
    from .orders.route_guides_route import route_guides_bp
    from .orders.route_stops_route import route_stops_bp
    from .orders.route_types_route import route_types_bp
    from .orders.routes_route import routes_bp
    from .orders.stops_route import stops_bp
    from .orders.hotel_owner_route import hotel_owner_bp

    app.register_blueprint(bus_info_bp)
    app.register_blueprint(cruise_info_bp)
    app.register_blueprint(departures_bp)
    app.register_blueprint(guides_bp)
    app.register_blueprint(hiking_info_bp)
    app.register_blueprint(hotel_info_bp)
    app.register_blueprint(route_guides_bp)
    app.register_blueprint(route_stops_bp)
    app.register_blueprint(route_types_bp)
    app.register_blueprint(routes_bp)
    app.register_blueprint(stops_bp)
    app.register_blueprint(hotel_owner_bp)
