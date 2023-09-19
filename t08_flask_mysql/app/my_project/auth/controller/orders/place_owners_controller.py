from t08_flask_mysql.app.my_project.auth.service import place_owners_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController

class PlaceOwnersController(GeneralController):
    """
    Realization of Place Owners controller.
    """
    _service = place_owners_service
