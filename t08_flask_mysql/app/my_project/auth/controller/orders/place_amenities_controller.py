from t08_flask_mysql.app.my_project.auth.service import place_amenities_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController

class PlaceAmenitiesController(GeneralController):
    """
    Realization of Place Reviews controller.
    """
    _service = place_amenities_service
