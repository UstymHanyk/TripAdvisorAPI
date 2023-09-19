from t08_flask_mysql.app.my_project.auth.dao import amenities_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService

class AmenityService(GeneralService):
    """
    Service class for handling Amenities.
    """
    _dao = amenities_dao
