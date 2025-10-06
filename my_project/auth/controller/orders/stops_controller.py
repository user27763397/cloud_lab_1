from my_project.auth.service import stops_service
from my_project.auth.controller.general_controller import GeneralController


class StopsController(GeneralController):
    _service = stops_service
