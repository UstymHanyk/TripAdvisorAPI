from t08_flask_mysql.app.my_project.auth.dao import payment_options_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService

class PaymentOptionsService(GeneralService):
    """
    Realization of Owners service.
    """
    _dao = payment_options_dao
