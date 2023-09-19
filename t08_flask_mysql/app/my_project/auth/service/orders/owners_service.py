from t08_flask_mysql.app.my_project.auth.dao import OwnerDAO
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService

class OwnersService(GeneralService):
    """
    Realization of Owners service.
    """
    _dao = OwnerDAO
