from my_project.auth.service import guides_service
from my_project.auth.controller.general_controller import GeneralController


class GuidesController(GeneralController):
    _service = guides_service
