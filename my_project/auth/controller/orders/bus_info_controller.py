from typing import List

from my_project.auth.service import bus_info_service
from my_project.auth.controller.general_controller import GeneralController


class BusInfoController(GeneralController):
    _service = bus_info_service

    def get_busses_after_route(self, route_id: int) -> List[object]:
        return self._service.get_busses_after_route(route_id)
