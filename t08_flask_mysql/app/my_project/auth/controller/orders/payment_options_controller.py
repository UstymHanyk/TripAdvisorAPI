from t08_flask_mysql.app.my_project.auth.service import payment_options_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController

class PaymentOptionsController(GeneralController):
    """
    Realization of Places controller.
    """
    _service = payment_options_service
