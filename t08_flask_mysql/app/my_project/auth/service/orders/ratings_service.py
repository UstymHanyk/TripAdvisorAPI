from t08_flask_mysql.app.my_project.auth.dao import ratings_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService

class RatingsService(GeneralService):
    """
    Realization of Ratings service.
    """
    _dao = ratings_dao
