from typing import List

from my_project.auth.dao import hiking_info_dao
from my_project.auth.service.general_service import GeneralService


class HikingInfoService(GeneralService):
    _dao = hiking_info_dao

    def get_hiking_after_route(self, route_id: int) -> List[object]:
        return self._dao.get_hiking_after_route(route_id)
