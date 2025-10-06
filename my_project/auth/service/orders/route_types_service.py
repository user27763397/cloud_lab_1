from my_project.auth.dao import route_types_dao
from my_project.auth.service.general_service import GeneralService


class RouteTypesService(GeneralService):
    _dao = route_types_dao

    def insert_route_type(self, type_name: str):
        self._dao.insert_route_type(type_name)
