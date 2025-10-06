from typing import List

from my_project.auth.dao import departures_dao
from my_project.auth.service.general_service import GeneralService


class DeparturesService(GeneralService):
    _dao = departures_dao

    def get_departures_after_route(self, route_id: int) -> List[object]:
        return self._dao.get_departures_after_route(route_id)
