from typing import List, Dict, Any

import sqlalchemy

from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import RouteGuides


class RouteGuidesDAO(GeneralDAO):
    _domain_type = RouteGuides

    def get_routes_in_rg(self, route_id: int) -> List[Dict[str, Any]]:
        result = self._session.execute(sqlalchemy.text("CALL get_routes_in_rg(:p1)"),
                                       {'p1': route_id}).mappings().all()
        return [dict(row) for row in result]

    def get_guides_in_rg(self, guide_id: int) -> List[Dict[str, Any]]:
        result = self._session.execute(sqlalchemy.text("CALL get_guides_in_rg(:p1)"),
                                       {'p1': guide_id}).mappings().all()
        return [dict(row) for row in result]
