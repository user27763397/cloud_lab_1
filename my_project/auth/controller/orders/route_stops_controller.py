from typing import List

from my_project.auth.service import route_stops_service
from my_project.auth.controller.general_controller import GeneralController


class RouteStopsController(GeneralController):
    _service = route_stops_service

    def get_routes_in_rs(self, route_id: int) -> List[object]:
        return self._service.get_routes_in_rs(route_id)

    def get_stops_in_rs(self, stop_id: int) -> List[object]:
        return self._service.get_stops_in_rs(stop_id)

    def insert_route_type(self, route_id: int, stop_id: int, stop_order: int):
        return self._service.insert_route_type(route_id, stop_id, stop_order)
