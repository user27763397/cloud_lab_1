from typing import List

from my_project.auth.service import hotel_info_service
from my_project.auth.controller.general_controller import GeneralController


class HotelInfoController(GeneralController):
    _service = hotel_info_service

    def get_hotels_after_route(self, route_id: int) -> List[object]:
        return self._service.get_hotels_after_route(route_id)
