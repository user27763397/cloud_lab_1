from typing import List, Dict, Any

import sqlalchemy

from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import RouteStops


class RouteStopsDAO(GeneralDAO):
    _domain_type = RouteStops

    def get_routes_in_rs(self, route_id: int) -> List[Dict[str, Any]]:
        result = self._session.execute(sqlalchemy.text("CALL get_routes_in_rs(:p1)"),
                                       {'p1': route_id}).mappings().all()
        return [dict(row) for row in result]

    def get_stops_in_rs(self, stop_id: int) -> List[Dict[str, Any]]:
        result = self._session.execute(sqlalchemy.text("CALL get_stops_in_rs(:p1)"),
                                       {'p1': stop_id}).mappings().all()
        return [dict(row) for row in result]

    def insert_route_type(self, route_id: int, stop_id: int, stop_order: int):
        result = self._session.execute(
            sqlalchemy.text("CALL insert_route_stops(:route_id, :stop_id, :stop_order)"),
            {"route_id": route_id, "stop_id": stop_id, "stop_order": stop_order}
        )
        self._session.commit()
        return result
