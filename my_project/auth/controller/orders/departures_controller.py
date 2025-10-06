from typing import List

from my_project.auth.service import departures_service
from my_project.auth.controller.general_controller import GeneralController


class DeparturesController(GeneralController):
    _service = departures_service

    def get_departures_after_route(self, route_id: int) -> List[object]:
        return self._service.get_departures_after_route(route_id)
