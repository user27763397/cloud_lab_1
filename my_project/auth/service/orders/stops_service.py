from my_project.auth.dao import stops_dao
from my_project.auth.service.general_service import GeneralService


class StopsService(GeneralService):
    _dao = stops_dao
