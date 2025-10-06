from my_project.auth.service import route_types_service
from my_project.auth.controller.general_controller import GeneralController


class RouteTypesController(GeneralController):
    _service = route_types_service

    def insert_route_type(self, type_name: str):
        self._service.insert_route_type(type_name)
