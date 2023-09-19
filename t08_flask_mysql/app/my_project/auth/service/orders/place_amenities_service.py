from t08_flask_mysql.app.my_project.auth.dao import place_amenities_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService

class PlaceAmenityService(GeneralService):
    """
    Service class for handling Place Amenities.
    """
    _dao = place_amenities_dao
