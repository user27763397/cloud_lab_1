from .orders.bus_info_dao import BusInfoDAO
from .orders.cruise_info_dao import CruiseInfoDAO
from .orders.departures_dao import DeparturesDAO
from .orders.guides_dao import GuidesDAO
from .orders.hiking_info_dao import HikingInfoDAO
from .orders.hotel_info_dao import HotelInfoDAO
from .orders.route_guides_dao import RouteGuidesDAO
from .orders.route_stops_dao import RouteStopsDAO
from .orders.route_types_dao import RouteTypesDAO
from .orders.routes_dao import RoutesDAO
from .orders.stops_dao import StopsDAO
from .orders.hotel_owner_dao import HotelOwnerDAO

bus_info_dao = BusInfoDAO()
cruise_info_dao = CruiseInfoDAO()
departures_dao = DeparturesDAO()
guides_dao = GuidesDAO()
hiking_info_dao = HikingInfoDAO()
hotel_info_dao = HotelInfoDAO()
route_guides_dao = RouteGuidesDAO()
route_stops_dao = RouteStopsDAO()
route_types_dao = RouteTypesDAO()
routes_dao = RoutesDAO()
stops_dao = StopsDAO()
hotel_owner_dao = HotelOwnerDAO()
