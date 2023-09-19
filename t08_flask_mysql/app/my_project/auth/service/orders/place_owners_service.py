from t08_flask_mysql.app.my_project.auth.dao import place_owners_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService

class PlaceOwnersService(GeneralService):
    """
    Realization of Place Owners service.
    """
    _dao = place_owners_dao
