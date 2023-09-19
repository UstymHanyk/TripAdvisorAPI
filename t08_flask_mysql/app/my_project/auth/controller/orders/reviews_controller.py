from t08_flask_mysql.app.my_project.auth.service import reviews_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController

class ReviewsController(GeneralController):
    """
    Realization of Reviews controller.
    """
    _service = reviews_service
