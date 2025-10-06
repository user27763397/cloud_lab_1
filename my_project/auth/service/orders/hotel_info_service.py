from typing import List

from my_project.auth.dao import hotel_info_dao
from my_project.auth.service.general_service import GeneralService


class HotelInfoService(GeneralService):
    _dao = hotel_info_dao

    def get_hotels_after_route(self, route_id: int) -> List[object]:
        return self._dao.get_hotels_after_route(route_id)

