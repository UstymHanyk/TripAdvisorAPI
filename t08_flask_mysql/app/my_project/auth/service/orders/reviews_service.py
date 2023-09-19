from t08_flask_mysql.app.my_project.auth.dao import reviews_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService

class ReviewsService(GeneralService):
    """
    Realization of Reviews service.
    """
    _dao = reviews_dao
