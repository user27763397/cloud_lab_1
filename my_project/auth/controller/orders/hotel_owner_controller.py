from my_project.auth.service import hotel_owner_service
from my_project.auth.controller.general_controller import GeneralController


class HotelOwnerController(GeneralController):
    _service = hotel_owner_service

