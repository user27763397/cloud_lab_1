from my_project.auth.dao import guides_dao
from my_project.auth.service.general_service import GeneralService


class GuidesService(GeneralService):
    _dao = guides_dao
