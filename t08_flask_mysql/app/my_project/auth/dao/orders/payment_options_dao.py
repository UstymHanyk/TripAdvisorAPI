from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import PaymentOptions
from typing import List

class PaymentOptionsDAO(GeneralDAO):
    """
    Realization of Review data access layer for TripAdvisor's reviews.
    """
    _domain_type = PaymentOptions
