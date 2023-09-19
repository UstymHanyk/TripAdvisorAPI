from t08_flask_mysql.app.my_project.auth.dao import users_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService

class UsersService(GeneralService):
    """
    Realization of Users service.
    """
    _dao = users_dao
