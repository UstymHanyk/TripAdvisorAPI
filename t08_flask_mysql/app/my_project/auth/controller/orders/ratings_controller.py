from t08_flask_mysql.app.my_project.auth.service import ratings_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController

class RatingsController(GeneralController):
    """
    Realization of Ratings controller.
    """
    _service = ratings_service
