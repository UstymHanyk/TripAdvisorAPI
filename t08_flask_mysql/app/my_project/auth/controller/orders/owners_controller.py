from t08_flask_mysql.app.my_project.auth.service import owners_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController

class OwnersController(GeneralController):
    """
    Realization of Owners controller.
    """
    _service = owners_service
