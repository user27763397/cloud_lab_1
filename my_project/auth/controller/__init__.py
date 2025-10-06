from .orders.bus_info_controller import BusInfoController
from .orders.cruise_info_controller import CruiseInfoController
from .orders.departures_controller import DeparturesController
from .orders.guides_controller import GuidesController
from .orders.hiking_info_controller import HikingInfoController
from .orders.hotel_info_controller import HotelInfoController
from .orders.route_guides_controller import RouteGuidesController
from .orders.route_stops_controller import RouteStopsController
from .orders.route_types_controller import RouteTypesController
from .orders.routes_controller import RoutesController
from .orders.stops_controller import StopsController
from .orders.hotel_owner_controller import HotelOwnerController

bus_info_controller = BusInfoController()
cruise_info_controller = CruiseInfoController()
departures_controller = DeparturesController()
guides_controller = GuidesController()
hiking_info_controller = HikingInfoController()
hotel_info_controller = HotelInfoController()
route_guides_controller = RouteGuidesController()
route_stops_controller = RouteStopsController()
route_types_controller = RouteTypesController()
routes_controller = RoutesController()
stops_controller = StopsController()
hotel_owner_controller = HotelOwnerController()
