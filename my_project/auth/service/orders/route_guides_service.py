from typing import List

from my_project.auth.dao import route_guides_dao
from my_project.auth.service.general_service import GeneralService


class RouteGuidesService(GeneralService):
    _dao = route_guides_dao

    def get_routes_in_rg(self, route_id: int) -> List[object]:
        return self._dao.get_routes_in_rg(route_id)

    def get_guides_in_rg(self, guide_id: int) -> List[object]:
        return self._dao.get_guides_in_rg(guide_id)
