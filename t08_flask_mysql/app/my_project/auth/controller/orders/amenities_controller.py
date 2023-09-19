from t08_flask_mysql.app.my_project.auth.service import amenities_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController

class AmenitiesController(GeneralController):
    """
    Realization of Place Reviews controller.
    """
    _service = amenities_service
