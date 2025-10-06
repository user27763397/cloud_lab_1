from typing import List

from my_project.auth.service import hiking_info_service
from my_project.auth.controller.general_controller import GeneralController


class HikingInfoController(GeneralController):
    _service = hiking_info_service

    def get_hiking_after_route(self, route_id: int) -> List[object]:
        return self._service.get_hiking_after_route(route_id)

