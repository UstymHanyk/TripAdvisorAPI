from t08_flask_mysql.app.my_project.auth.service import users_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController

class UsersController(GeneralController):
    """
    Realization of Users controller.
    """
    _service = users_service
