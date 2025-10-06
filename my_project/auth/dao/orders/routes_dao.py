from typing import List, Dict, Any

import sqlalchemy

from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import Routes


class RoutesDAO(GeneralDAO):
    _domain_type = Routes

    def get_routes_after_route_type(self, route_type_id: int) -> List[Dict[str, Any]]:
        result = self._session.execute(sqlalchemy.text("CALL get_routes_after_route_type(:p1)"),
                                       {'p1': route_type_id}).mappings().all()
        return [dict(row) for row in result]
