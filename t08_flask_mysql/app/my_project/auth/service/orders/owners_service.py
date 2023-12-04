from t08_flask_mysql.app.my_project.auth.dao import owners_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService

class OwnersService(GeneralService):
    """
    Realization of Owners service.
    """
    _dao = owners_dao
    def create_10_timestampt_tables(self):
        result = self._dao.create_10_timestampt_tables()
        return result