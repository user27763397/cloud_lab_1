from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import Guides


class GuidesDAO(GeneralDAO):
    _domain_type = Guides
