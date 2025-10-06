import sqlalchemy

from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import RouteTypes


class RouteTypesDAO(GeneralDAO):
    _domain_type = RouteTypes

    def insert_route_type(self, type_name: str):
        result = self._session.execute(
            sqlalchemy.text("CALL insert_route_type(:type_name)"),
            {"type_name": type_name}
        )
        self._session.commit()
        return result
