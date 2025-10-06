from typing import List

from my_project.auth.service import cruise_info_service
from my_project.auth.controller.general_controller import GeneralController


class CruiseInfoController(GeneralController):
    _service = cruise_info_service

    def get_cruises_after_route(self, route_id: int) -> List[object]:
        return self._service.get_cruises_after_route(route_id)
