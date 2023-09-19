from t08_flask_mysql.app.my_project.auth.service import places_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController

class PlacesController(GeneralController):
    """
    Realization of Places controller.
    """
    _service = places_service
