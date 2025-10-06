from typing import List

from my_project.auth.dao import bus_info_dao
from my_project.auth.service.general_service import GeneralService


class BusInfoService(GeneralService):
    _dao = bus_info_dao

    def get_busses_after_route(self, route_id: int) -> List[object]:
        return self._dao.get_busses_after_route(route_id)
