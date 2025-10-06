from typing import List

from my_project.auth.dao import routes_dao
from my_project.auth.service.general_service import GeneralService


class RoutesService(GeneralService):
    _dao = routes_dao

    def get_routes_after_route_type(self, route_type_id: int) -> List[object]:
        return self._dao.get_routes_after_route_type(route_type_id)
