from t08_flask_mysql.app.my_project.auth.service import user_details_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController

class UserDetailsController(GeneralController):
    """
    Realization of User Details controller.
    """
    _service = user_details_service
