from typing import List

from my_project.auth.service import routes_service
from my_project.auth.controller.general_controller import GeneralController


class RoutesController(GeneralController):
    _service = routes_service

    def get_routes_after_route_type(self, route_type_id: int) -> List[object]:
        return self._service.get_routes_after_route_type(route_type_id)
