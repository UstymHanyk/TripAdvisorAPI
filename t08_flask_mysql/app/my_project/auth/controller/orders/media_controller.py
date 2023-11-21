from t08_flask_mysql.app.my_project.auth.service import media_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController

class MediaController(GeneralController):
    """
    Realization of Media controller.
    """
    _service = media_service

