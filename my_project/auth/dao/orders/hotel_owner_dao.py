from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import HotelOwner


class HotelOwnerDAO(GeneralDAO):
    _domain_type = HotelOwner

