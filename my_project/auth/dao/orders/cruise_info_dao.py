from typing import List, Dict, Any

import sqlalchemy

from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import CruiseInfo


class CruiseInfoDAO(GeneralDAO):
    _domain_type = CruiseInfo

    def get_cruises_after_route(self, route_id: int) -> List[Dict[str, Any]]:
        result = self._session.execute(sqlalchemy.text("CALL get_cruises_after_route(:p1)"),
                                       {'p1': route_id}).mappings().all()
        return [dict(row) for row in result]
