from my_project.auth.dao import hotel_owner_dao
from my_project.auth.service.general_service import GeneralService


class HotelOwnerService(GeneralService):
    _dao = hotel_owner_dao


