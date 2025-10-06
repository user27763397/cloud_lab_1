from typing import List

from my_project.auth.service import route_guides_service
from my_project.auth.controller.general_controller import GeneralController


class RouteGuidesController(GeneralController):
    _service = route_guides_service

    def get_routes_in_rg(self, route_id: int) -> List[object]:
        return self._service.get_routes_in_rg(route_id)

    def get_guides_in_rg(self, guide_id: int) -> List[object]:
        return self._service.get_guides_in_rg(guide_id)
