from .orders.bus_info_service import BusInfoService
from .orders.cruise_info_service import CruiseInfoService
from .orders.departures_service import DeparturesService
from .orders.guides_service import GuidesService
from .orders.hiking_info_service import HikingInfoService
from .orders.hotel_info_service import HotelInfoService
from .orders.route_guides_service import RouteGuidesService
from .orders.route_stops_service import RouteStopsService
from .orders.route_types_service import RouteTypesService
from .orders.routes_service import RoutesService
from .orders.stops_service import StopsService
from .orders.hotel_owner_service import HotelOwnerService

bus_info_service = BusInfoService()
cruise_info_service = CruiseInfoService()
departures_service = DeparturesService()
guides_service = GuidesService()
hiking_info_service = HikingInfoService()
hotel_info_service = HotelInfoService()
route_guides_service = RouteGuidesService()
route_stops_service = RouteStopsService()
route_types_service = RouteTypesService()
routes_service = RoutesService()
stops_service = StopsService()
hotel_owner_service = HotelOwnerService()
