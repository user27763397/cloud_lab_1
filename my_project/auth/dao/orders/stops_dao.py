from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import Stops


class StopsDAO(GeneralDAO):
    _domain_type = Stops
